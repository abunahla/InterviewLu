# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required

from django.shortcuts import render

# Create your views here.
def home(request):
	context= locals()
	template = 'home.html'
	return render(request,template,context)
@login_required
def details(request):
	context= locals()
	template = 'details.html'
	return render(request,template,context)
