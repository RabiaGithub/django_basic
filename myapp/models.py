from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=30)
    phone = models.IntegerField()
    email = models.EmailField()
    body = models.TextField()

    def __str__(self):
        return self.name