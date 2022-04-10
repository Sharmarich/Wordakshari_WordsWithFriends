from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserInfo(models.Model):

	host = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	level = models.IntegerField(default=1)
	words_solved = models.IntegerField(default=0)

class Room(models.Model):

	host = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	opponent = models.CharField(max_length=20,null=True, blank=True)
	is_over = models.BooleanField(default=False)
	turn = models.CharField(max_length=20,null=True, blank=True)
	word = models.CharField(max_length=20,default='AAPLE')