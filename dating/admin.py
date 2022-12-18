from django.contrib import admin
from .models import MessageRequest , FriendList , profile_list

class FriendListAdmin(admin.ModelAdmin):
	list_filter = ['user']
	list_display = ['user']
	search_fields = ['user']
	readonly_fields = ['user']

	class Meta:
		model =FriendList

admin.site.register(profile_list)

admin.site.register(FriendList,FriendListAdmin)

class MessageRequestAdmin(admin.ModelAdmin):
	list_filter = ['sender','reciever']
	list_display = ['sender','reciever']
	search_fields = ['sender__username','sender__email','reciever__email','reciever__username']

	class Meta:
		model = MessageRequest

admin.site.register(MessageRequest,MessageRequestAdmin) 
	
