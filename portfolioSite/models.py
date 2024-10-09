from django.db import models

class Projects(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=50)
    techUsed = models.TextField()
    github = models.URLField(blank=True)

    def __str__(self):
        return f"{self.name}"

class Skill(models.Model):
    name = models.CharField(max_length=100)
    expertise = models.TextField()  
