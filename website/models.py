from django.db import models
from django.db.models import CharField
from django.urls import reverse
from django.contrib.auth import get_user_model
class Member(models.Model):
	fname = models.CharField(max_length=50)
	lname = models.CharField(max_length=50)
	email = models.EmailField(max_length=30)
	passwd = models.CharField(max_length=50)
	age = models.IntegerField()
	phone_num = models.IntegerField()
	address = models.CharField(max_length=100, null=True, blank=True)
	date_join = models.DateTimeField(auto_now_add= True)
	author = models.ForeignKey(
		get_user_model(),
		on_delete=models.CASCADE, null=True, blank=True 	
		)

	def __str__(self):
		return self.fname + ' ' + self.lname


	def get_absolute_url(self):
		return reverse('home', agrs(str[self.pk]))