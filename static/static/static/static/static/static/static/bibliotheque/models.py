from django.db import models
from users.models import Profile
import uuid
# Create your models here.


class Category(models.Model):
    label = models.CharField(max_length=30)
    slug = models.SlugField(null=True, max_length=50, blank=True)

    def __str__(self):
        return f"{self.label} "

    class Meta:
        ordering = ["label"]


Tag = (
    ('P', "Pret"),
    ('H-P', "Hors-Pret")
)


class Book(models.Model):
    manager = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    title = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    body = models.TextField()
    image = models.URLField()
    avaible = models.BooleanField(default=True)
    tag = models.CharField(max_length=30, choices=Tag, default="P")
    exemplaire = models.IntegerField(default=10)

    def __str__(self):
        return f"{self.title} {self.id}"

    class Meta:
        ordering = ["title"]
