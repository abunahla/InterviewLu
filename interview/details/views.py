from __future__ import unicode_literals# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required


from django.shortcuts import render

# Create your views here.
def home(request):
	context= locals()
	template = 'home.html'
	return render(request,template,context)
@login_required
def about(request):
	user= request.user
	context= {'user': user}
	template = 'about.html'
	return render(request,template,context)
	
def signup(request):
	context= locals()
	template = 'account/signup.html'
	return render(request,template,context)


def login(request):
	context= locals()
	template = 'account/login.html'
	return render(request,template,context)

def logout(request):
	user= request.user
	context= locals()
	template = 'account/logout.html'
	return render(request,template,context)

def password_change(request):
	context= locals()
	template = 'account/password_change.html'
	return render(request,template,context)

def password_set(request):
	context= locals()
	template = 'account/password_set.html'
	return render(request,template,context)

def account_inactive(request):
	context= locals()
	template = 'account/inactive.html'
	return render(request,template,context)

def email(request):
	context= locals()
	template = 'account/email.html'
	return render(request,template,context)

def email_verification_sent(request):
	context= locals()
	template = 'account/email_verification_sent.html'
	return render(request,template,context)

def confirm_email(request):
	context= locals()
	template = 'account/confirm_email.html'
	return render(request,template,context)

def password_reset(request):
	context= locals()
	template = 'account/password_reset.html'
	return render(request,template,context)

def password_reset_done(request):
	context= locals()
	template = 'account/password_reset_done.html'
	return render(request,template,context)

def password_reset_from_key(request):
	context= locals()
	template = 'account/password_reset_from_key.html'
	return render(request,template,context)		

def password_reset_from_key_done(request):
	context= locals()
	template = 'account/password_reset_from_key_done.html'
	return render(request,template,context)											




