from django.db import models

class ImageKey(models.Model):

    code=models.CharField(max_length=255)

class ImageFile(models.Model):
   
    image = models.ImageField(null=True)
    text=models.TextField()   
    def __str__(self):
        return str(self.id)
