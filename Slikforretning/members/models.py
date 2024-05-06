from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True)
    postID = models.IntegerField(null=True)
    city = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255, null=True)
    phone = models.IntegerField(null=True)
    favoritecandy = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
# Create your models here.