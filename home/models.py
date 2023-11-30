from django.db import models

# Create your models here.
class Banner(models.Model) :
    title = models.CharField( max_length=30)
    description = models.CharField(max_length=30)
    body= models.CharField( max_length=200)
    
    def __str__(self) -> str:
        return self.title
    
    
class Contact(models.Model) :
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField() 
    
    def __str__(self) -> str:
        return self.name
    
    
class About(models.Model) :
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=555)
    image = models.ImageField(upload_to='about/') 
    # body = models.TextField(max_length=5555)
    
    
    def __str__(self) -> str:
        return self.title  
    
class Service(models.Model) :
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=555)
    image = models.ImageField(upload_to='service/') 
    # body = models.TextField(max_length=5555)
    
    
    def __str__(self) -> str:
        return self.title  

class Testimonial(models.Model) :
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=555)
    image = models.ImageField(upload_to='testimonial/') 
    body = models.TextField()
    
    
    def __str__(self) -> str:
        return self.title 
    
    
class ContactPersonal(models.Model) :
    link = models.CharField(max_length=250)
    image_1 = models.ImageField(upload_to='contact_personal/') 
    image_2 = models.ImageField(upload_to='contact_personal/') 
    
    
    def __str__(self) -> str:
        return self.link 
    
    