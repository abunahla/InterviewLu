from django import forms
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget

class contactForm(forms.Form):
	name = forms.CharField(required=True, max_length=50, help_text='Maximum 50 characters')
	email = forms.EmailField(required=True,help_text='e.g moha@yahoo.com')
	comment = forms.CharField(required=True, max_length=200, widget=forms.Textarea, help_text='max 200 characters')
	captcha = ReCaptchaField(required=True,widget=ReCaptchaWidget())


 