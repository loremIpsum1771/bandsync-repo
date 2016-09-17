from django.shortcuts import render
from django.conf import settings
from .forms import ContactForm, SignUpForm, SearchForm, ModalForm
import json
import urllib2
from django.contrib.auth.decorators import login_required
from .models import SignUp, Concert, Artist, ConcertOf, Follow, Invite

# Create your views here.

from django.core.mail import send_mail


def home(request):
	title = "Welcome"

	#add a form
	form = SignUpForm(request.POST or None)

	context = {
		"title" : title,
		"form" : form
	}


	if form.is_valid():
		form.save()
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
	queryform = SearchForm(request.POST or None)
	modalform = ModalForm(request.POST or None)
	if queryform.is_valid():
		form_artistSelect = urllib2.quote(queryform.cleaned_data.get("artist_select"))
		form_city =   urllib2.quote(queryform.cleaned_data.get("city"))
		form_state = urllib2.quote(queryform.cleaned_data.get("state"))
		mile_radius = urllib2.quote(queryform.cleaned_data.get("radius"))
		url = "http://api.bandsintown.com/artists/" + form_artistSelect + "/events/search.json?api_version=2.0&app_id=YOUR_APP_ID&location=" +form_city+","+ form_state+"&radius="+ mile_radius
		data = json.load(urllib2.urlopen(url))

		context = {
			"queryform" : queryform,
			"modalform" : modalform,
			"data": data
		}
		titles = json.dumps([i.get("title") for i in data])
		ticket_urls = json.dumps([i.get("ticket_url").encode("utf-8") for i in data])
		ticket_statuses = json.dumps([i.get("ticket_status").encode("utf-8") for i in data])
		venues = json.dumps([i["venue"] for i in data])

		print "\ntitles\n"
		print titles
		print "\nformatted_dts\n"
		print ticket_urls
		print "\nticket_statuses\n"
		print ticket_statuses
	
	else:
		context = {
			"queryform" : queryform	

		}
	if modalform.is_valid():
		form_recipient = modalform.cleaned_data.get("rec_email")
	 	form_message = modalform.cleaned_data.get("message")
		form_recname = modalform.cleaned_data.get("rec_name")
	 	print form_recipient
	 	print form_message
	 	print form_recname
	 	concert_venue = modalform.cleaned_data.get("additionalValues[venue]")
	 	concert_date= modalform.cleaned_data.get("additionalValues[uf_date]")
	 	concert_url = modalform.cleaned_data.get("additionalValues[ticket_url]")
	 	artist = modalform.cleaned_data.get("additionalValues[artist]")
	 	print "concert venue"
	 	print concert_venue
	 	print "concert date"
	 	print concert_date
	 	print "concert_url"
	 	print concert_url
	 	print "artist"
	 	print artist

	return render(request,"searchform.html" , context)




def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_full_name = form.cleaned_data.get("full_name")
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
	return render(request, "profilepage.html")#, context)
