from django.db import models
from django.contrib.auth.models import User


class profile_list(models.Model):
	name = models.CharField(max_length = 30)
	city = models.CharField(max_length = 40)
	image = models.ImageField(default = 'default.jpg', upload_to='profile_pics')
	user_name = models.ForeignKey(User , on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.name} profile_list'


