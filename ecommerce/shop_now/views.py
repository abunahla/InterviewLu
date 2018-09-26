# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def shop_now(request):
	context= locals()
	template = 'shop_now.html'
	return render(request,template,context)