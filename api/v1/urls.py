from django.urls import include, path

from api.v1.auth.views import LoginView, RegisterView


urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    
    path("", include("api.v1.posts.urls")),    # Include auth's URLs
]
