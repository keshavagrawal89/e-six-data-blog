from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from posts.models import Post

class PostAPITests(APITestCase):
    def setUp(self):
        # Create a user
        self.user = get_user_model().objects.create_user(
            email='testuser',
            password='testpass',
            first_name='John',
            last_name='Doe'
        )
        # Create an authentication token for the user
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')  
        
        self.url_register = reverse('register')  
        self.url_login = reverse('login')  
        self.url_posts = reverse('posts-list')  

    def test_register_user(self):
        response = self.client.post(self.url_register, {
            'email': 'newuser',
            'password': 'newpass',
            'first_name': 'Jane',
            'last_name': 'Doe'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(get_user_model().objects.count(), 2)

    def test_login_user(self):
        response = self.client.post(self.url_login, {
            'email': 'testuser',
            'password': 'testpass'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_create_post(self):
        # Now that token is set in credentials, create a post
        response = self.client.post(self.url_posts, {
            'title': 'My First Post',
            'content': 'This is the content of my first post.'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().title, 'My First Post')

    def test_get_post(self):
        # Create a post to retrieve
        post = Post.objects.create(
            title='Another Post',
            content='Content of another post.',
            author=self.user
        )
        post_detail_url = reverse('posts-detail', kwargs={'pk': post.uuid})
        response = self.client.get(post_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], post.title)

    def test_edit_post(self):
        # Create a post to edit
        post = Post.objects.create(
            title='Editable Post',
            content='Editable content.',
            author=self.user
        )
        post_detail_url = reverse('posts-detail', kwargs={'pk': post.uuid})
        response = self.client.patch(post_detail_url, {
            'title': 'Updated Post Title'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Post.objects.get(uuid=post.uuid).title, 'Updated Post Title')

    def test_get_all_posts(self):
        # Create two posts
        Post.objects.create(
            title='First Post',
            content='Content of the first post.',
            author=self.user
        )
        Post.objects.create(
            title='Second Post',
            content='Content of the second post.',
            author=self.user
        )
        response = self.client.get(self.url_posts)
    
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 2)

    def test_create_post_unauthenticated(self):
        # Remove the token to test unauthenticated access
        self.client.credentials()
        response = self.client.post(self.url_posts, {
            'title': 'My Second Post',
            'content': 'This should not be allowed.'
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
