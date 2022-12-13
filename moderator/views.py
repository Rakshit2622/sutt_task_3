from django.shortcuts import render
from django.http import HttpResponse 
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
def mod_home(request):
	return HttpResponse("<h1>Hello moderator </h1>")
