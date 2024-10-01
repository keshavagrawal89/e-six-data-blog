from django.db import models


from .base import BaseModel
from .user import AuthUser


class Post(BaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(AuthUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title