from django.db import models

# Create your models here.

class Home(models.Model):

    name = models.CharField(max_length=60)
    job_title = models.CharField( max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=20)
    skills = models.CharField(max_length=20)
    user_image = models.ImageField(upload_to='portfolio/')
    about_me = models.TextField(max_length=10000)
    

    def __str__(self):
        return self.name

   
    


