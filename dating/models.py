from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class profile_list(models.Model):
	name = models.CharField(max_length = 30)
	city = models.CharField(max_length = 40)
	image = models.ImageField(default = 'default.jpg', upload_to='profile_pics')
	user_name = models.ForeignKey(User , on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.name} profile_list'

class FriendList(models.Model):
	user = models.OneToOneField(User , on_delete = models.CASCADE , related_name = 'user')
	friends = models.ManyToManyField(User , blank =True ,related_name='friends')

	def __str__(self):
		return self.user.username

	def add_friend(self , account):
		if not account in self.friends.all():
			self.friends.add(account)

class MessageRequest(models.Model):
	sender = models.ForeignKey(User , on_delete = models.CASCADE , related_name = 'sender')
	reciever = models.ForeignKey(User , on_delete = models.CASCADE , related_name = 'reciever')
	is_active = models.BooleanField(blank = True , null = False , default = True)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.sender.username

	def accept(self):
		reciever_friend_list = FriendList.objects.get(user=self.reciever)
		if reciever_friend_list:
			reciever_friend_list.add_friend(self.sender)
			sender_friend_list = FriendList.objects.get(user=self.sender)
			if sender_friend_list:
				sender_friend_list.add_friend(self.receiver)
				self.is_active=False
				self.save()


	def decline(self):
		self.is_active=False
		self.save()



