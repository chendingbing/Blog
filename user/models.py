from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=20,null=False)
    email = models.EmailField()
    mobile = models.CharField(max_length=16)
    create_time = models.DateTimeField(auto_now=True)
    password = models.CharField(max_length=100)
    friend_id = models.IntegerField()

    class Meta:
        unique_together = ('email', 'mobile')