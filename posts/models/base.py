import uuid


from django.db import models


class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    meta = models.JSONField(default=dict, blank=True, null=True)
    is_active = models.BooleanField(default=True)    