from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class AuthUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


class AuthUser(AbstractUser):
    class UserType(models.IntegerChoices):
        MODERATOR = 0, _('Moderator')
        NORMAL = 1, _('Normal')

    email = models.EmailField(unique=True) 
    user_type = models.IntegerField(choices=UserType.choices, default=UserType.NORMAL)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    # profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    meta = models.JSONField(default=dict, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AuthUserManager()
    
    def __str__(self):
        return f"{self.email} ({self.get_user_type_display()})"
