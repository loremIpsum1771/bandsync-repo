from django.shortcuts import render
from django.conf import settings
from .forms import ContactForm, SignUpForm, SearchForm
# Create your views here.

from django.core.mail import send_mail


def home(request):
	title = "Welcome"
	# if request.user.is_authenticated():
	# 	title = "My Title %s" % (request.user)	

	#add a form
	form = SignUpForm(request.POST or None)

	context = {
		"title" : title,
		"form" : form
	}


	if form.is_valid():
		form.save()
		# instance = form.save(commit =False)

		instance = form.save(commit = False)

		full_name = form.cleaned_data.get("full_name")

		if not full_name:
			full_name = "new full name"
		instance.full_name = full_name

		instance.save()
		context = {
			"title" : "Thank you"
		
		}
	return render(request, "home.html", context)



def search(request):
	form = SearchForm(request.POST or None)
	if form.is_valid():
		form_artistSelect = form.cleaned_data.get("artist_select")
		form_city = form.cleaned_data.get("city")
		form_state = form.cleaned_data.get("state")
		

	context = {
		"form" : form
	}
	return render(request,"searchform.html" , context)


def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		# for key, value in form.cleaned_data.iteritems():
		# 	print key, value
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_full_name = form.cleaned_data.get("full_name")
		# print form.cleaned_data
		subject = "Site contact form"
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email, 'celijahh@gmail.com']
		contact_message = ''' 
		%s: %s via %s
		'''%(form_full_name, form_message, form_email)
		send_mail(subject, contact_message, from_email, to_email, fail_silently =False)

	context = {
		"form": form
	}
	return render(request, "forms.html", context)

def profile(request):

	return render(request, "profilepage.html")