from django.db import models
from datetime import date
# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    icon = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(null=False, blank=False, help_text='Content')
    date = models.DateField(default=date.today)
    image = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.name
    