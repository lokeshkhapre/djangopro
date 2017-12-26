# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def signup1(request):
	return render(request, 'signup1.html')




# def valdate(request):
# 	username = request.Get.get('username',none)
# 	data = {
# 			'is_taken' : User.object.filter(username_iexact=username).exists()
# 			}
# 	return render(request, 'signup.html')


# Create your views here.
