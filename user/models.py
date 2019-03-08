from django.db import models

# Create your models here.

class User(models.Model):
    nickname=models.CharField(max_length=20,null=True)
    email = models.EmailField(max_length=50, null=True)
    create_time = models.DateTimeField(auto_now=True)
    password = models.CharField(max_length=100)
    # friend_id = models.IntegerField()

    class Meta:
        unique_together = ('email',)
        db_table = 'user'
