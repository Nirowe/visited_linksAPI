from django.db import models

# Create your models here.


class Link(models.Model):

    addr = models.CharField(max_length=100)
    visited_at = models.DateTimeField(auto_now_add=True)