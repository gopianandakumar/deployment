from django.db import models
from datetime import datetime

# Create your models here.

class Article(models.Model):
    title =models.CharField(max_length=120);
    description=models.TextField();
    img=models.ImageField(upload_to='blog/');
    crated_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title;


    class Meta:
        verbose_name="Article"
        verbose_name_plural="Articles"
