from django.shortcuts import render
from .models import profile_list,FriendList,MessageRequest
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.http import HttpResponse ,HttpResponseRedirect
from Users.models import Profile

def home(request):
	profile = profile_list.objects.all()
	context = {'profile' : profile}

	return render(request , 'dating/f1.html', context)

class ProfileListView(ListView):
	model = profile_list
	template_name = 'dating/f1.html'
	context_object_name = 'profile'
	ordering = ['user_name']


	