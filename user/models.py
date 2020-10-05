from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.AutoField
    user_name = models.CharField(max_length=50)
    user_password = models.CharField(max_length=20)


    def __str__(self):
        return self.user_name

