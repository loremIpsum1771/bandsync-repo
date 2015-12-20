from django.shortcuts import render
from django.conf import settings
from .forms import ContactForm, SignUpForm, SearchForm
import json
import urllib2

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
		form_artistSelect = urllib2.quote(form.cleaned_data.get("artist_select"))
		form_city =   urllib2.quote(form.cleaned_data.get("city"))
		form_state = urllib2.quote(form.cleaned_data.get("state"))
		mile_radius = urllib2.quote(form.cleaned_data.get("radius"))
		#print "testing"
		url = "http://api.bandsintown.com/events/search?artists[]=" + form_artistSelect + "&location=" +form_city+","+ form_state+"&radius="+ mile_radius + "&format=json&app_id=YOUR_APP_ID"
		data = json.load(urllib2.urlopen(url))

		#titles = [ i.get("title") for i in data]
		raw_dts = ["".join(i.get("datetime")) for i in data]
		
		#formatted_dts = [i.get("formatted_datetime") for i in data]
		ticket_urls = ["".join(i.get("ticket_url")) for i in data]
		ticket_statuses = ["".join(i.get("ticket_status")) for i in data]
		venue_names = ["".join(i.get("venue").get("name")) for i in data]
		venue_cities = ["".join(i.get("venue").get("city")) for i in data]
		venue_region = ["".join(i.get("venue").get("region")) for i in data]



		# print "\ntitles\n"
		# print titles
		print "\nraw_dts\n"
		print raw_dts
		print "\nformatted_dts\n"
		# print formatted_dts
		# print "\nticket_urls\n"
		print ticket_urls
		print "\nticket_statuses\n"
		print ticket_statuses
		print "\nvenue names\n"
		print venue_names
		print "\nvenue cities\n"
		print venue_cities
		print "\nvenue region\n"
		print venue_region
	

	context = {
		"form_artistSelect" : form_artistSelect,
		"raw_dts" : raw_dts,
		"ticket_urls" : ticket_urls,
		"ticket_statuses" : ticket_statuses,
		"venue_names" : venue_names,
		"venue_cities" : venue_cities,
		"venue_region" : venue_region,
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