from django.db import models
from django.contrib.auth.models import User
import uuid
DEFAULT_PROFILE_OBJECT = {}
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.SET_NULL, null=True, default=DEFAULT_PROFILE_OBJECT)
    cin = models.CharField(max_length=10, null=True)
    name = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=30, null=True)
    image = models.ImageField(null=True, upload_to="profile/")
    id = models.UUIDField(primary_key=True, unique=True,
                          default=uuid.uuid4, editable=False)

    def __str__(self):
        return f"{self.user.username}"
