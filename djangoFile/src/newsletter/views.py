from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import SignUpForm,ContactForm
from .models import SignUp

# Create your views here.
def JoinUs(request):
	title = 'Sign up'
	form = SignUpForm(request.POST or None)
	context = {
		"title": title,
		"form": form,
	}

	if form.is_valid():
		form.save()
		context = {
				"title": "Thank you"
		}

	if request.user.is_authenticated  and request.user.is_staff:
		queryset = SignUp.objects.all().order_by('-timestamp')
		context = {
			"queryset": queryset,
		}	
	return render(request, "JoinUs.html", context)

def home(request):
	title = 'Sign up'
	form = SignUpForm(request.POST or None)
	context = {
		"title": title,
		"form": form,
	}

	if form.is_valid():
		form.save()
		context = {
				"title": "Thank you"
		}

	if request.user.is_authenticated  and request.user.is_staff:
		queryset = SignUp.objects.all().order_by('-timestamp')
		context = {
			"queryset": queryset,
		}	
	return render(request, "home.html", context)

def contact(request):
	title = 'Contact Us'
	title_align_center = True
	form = ContactForm(request.POST or None)
	if form.is_valid():
		for key,value in form.cleaned_data.iteritems() :
			#print key,value
			form_email = form.cleaned_data.get("email")
			form_message = form.cleaned_data.get("message")
			form_full_name = form.cleaned_data.get("full_name")

			subject = 'site contact form'
			from_email =  settings.EMAIL_HOST_USER
			to_email = [from_email, 'youotheremail@email.com']
			contact_message = "%s: %s via %s" %(form_full_name,form_message, form_email)

			send_mail(subject,contact_message,from_email, to_email, fail_silently=True)
	context = {
		"title" :title,
		"form": form,
		"title_align_center":title_align_center,
		
	}
	return render(request, "forms.html", context)