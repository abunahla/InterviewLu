# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.mail import send_mail
from twilio.rest import TwilioRestClient
from django.conf import settings
from .forms import contactForm


# Create your views 
def contact(request):
	title='Leave a feedback '
	name='name'
	form=contactForm(request.POST or None)
	confirm_message=None
	if form.is_valid():
		name=form.cleaned_data['name']
		email=form.cleaned_data['email']
		comment=form.cleaned_data['comment']
		subject='message from my Ogas.com'
		message='%s %s' %(comment, name)
		emailFrom=[settings.EMAIL_HOST_USER]
		emailTo=[email]
		send_mail(subject,message,emailFrom,emailTo, fail_silently=False)
		title = "Thanks !!!!"
		confirm_message="Thanks for your feedback. We are working on it & we  will get intouch soonest"

		form=None

	context={'title':title, 'form': form,'confirm_message': confirm_message, 'name':name}	
	template = 'contact.html'
	return render(request,template,context)