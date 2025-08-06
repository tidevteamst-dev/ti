from django.db import models

# Create your models here.

class Project(models.Model):
    thumbnail = models.ImageField(upload_to="thumbnails_images")
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    customer = models.CharField(max_length=75)
    category = models.CharField(max_length=75)
    date = models.CharField(max_length=75)
    tech = models.CharField(max_length=120)
    project_url = models.URLField(max_length=200)
    picture1 = models.ImageField(upload_to="projects_images")
    picture2 = models.ImageField(upload_to="projects_images")
    picture3 = models.ImageField(upload_to="projects_images")
    picture4 = models.ImageField(upload_to="projects_images")
