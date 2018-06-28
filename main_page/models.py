from django.db import models

# Create your models here.
from django.db import models

class Article(models.Model):
    file_obj = models.FileField(upload_to='media/')