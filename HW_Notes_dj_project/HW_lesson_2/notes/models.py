from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class Notes(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True, blank=True)
    text = models.TextField()
    reminder = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        if len(self.text) >= 50:
            return f"{self.title}: {self.text[:50]}..."
        else:
            return f"{self.title}: {self.text}"
