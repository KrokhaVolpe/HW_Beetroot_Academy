from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)


class Category(models.Model):
    title = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title


class Notes(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, null=True, blank=True)
    text = models.TextField()
    reminder = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.title}: {self.text[:50]}"
    
    def save(self, *args, **kwargs):
        if self.reminder is None:
            self.reminder = timezone.now()
        super().save(*args, **kwargs)
        


