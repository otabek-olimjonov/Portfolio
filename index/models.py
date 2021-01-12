from django.db import models

# Create your models here.

class About(models.Model):
    fname = models.CharField(max_length = 20)
    lname = models.CharField(max_length = 20)
    img = models.ImageField(upload_to = 'Images')
    position = models.CharField(max_length = 100)
    info = models.TextField()
    email = models.CharField(max_length = 50)
    adress = models.CharField(max_length = 50)
    number = models.CharField(max_length = 20)
    comment = models.CharField(max_length = 150)

    def __str__(self):
        return self.fname

class Social_networks(models.Model):
    name = models.CharField(max_length = 20)
    link = models.URLField(max_length = 100)

    def __str__(self):
        return self.name

class Skill_Categories(models.Model):
    name = models.CharField(max_length = 50)
    def __str__(self):
        return self.name


class Skills(models.Model):
    name = models.CharField(max_length = 50)
    category = models.ForeignKey(Skill_Categories, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Projects(models.Model):
    name = models.CharField(max_length = 50)
    link = models.URLField(max_length = 100)
    img = models.ImageField(upload_to = 'Images')

    
    def __str__(self):
        return self.name