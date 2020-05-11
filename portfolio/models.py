from django.db import models
#pip3 install pillow


class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    image = models.ImageField(upload_to='images')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
