from django.shortcuts import render
from .models import profile_list
def home(request):
	profile = profile_list.objects.all()
	return render(request , 'dating/f1.html', {'profile' : profile})
