from django.db import models

class projects(models.Model):
  link = models.CharField(max_length=255)
  image_property = models.FileField(upload_to='members',max_length=255,null=True,blank=True,default=None)
  catagory = models.CharField(max_length=255,null=True,blank=True)
  name=models.CharField(max_length=255,null=True,blank=True)

class contact_model(models.Model):
  email = models.EmailField(max_length=100,null=True,blank=True)
  full_name = models.CharField(max_length=255)
  subject = models.CharField(max_length=255,null=True,blank=True)
  message = models.TextField(null=True,blank=True)

def __str__(self):
    return f"{self.name} {self.catagory} "