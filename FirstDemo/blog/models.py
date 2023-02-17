from django.db import models

# Create your models here.


class Post(models.Model):
    author = models.TextField()
    text = models.TextField()

    def __str__(self):
        return self.text[:50]
