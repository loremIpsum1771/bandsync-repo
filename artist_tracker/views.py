from django.shortcuts import render
from django.conf import settings
from .forms import ContactForm, SignUpForm, SearchForm, ModalForm
import json
import urllib2
from django.contrib.auth.decorators import login_required

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
	queryform = SearchForm(request.POST or None)
	modalform = ModalForm(request.POST or None)
	#print "query form is valid = " + str(modalform.is_valid())
	if queryform.is_valid():
		form_artistSelect = urllib2.quote(queryform.cleaned_data.get("artist_select"))
		form_city =   urllib2.quote(queryform.cleaned_data.get("city"))
		form_state = urllib2.quote(queryform.cleaned_data.get("state"))
		mile_radius = urllib2.quote(queryform.cleaned_data.get("radius"))

		#print "testing"
		url = "http://api.bandsintown.com/events/search?artists[]=" + form_artistSelect + "&location=" +form_city+","+ form_state+"&radius="+ mile_radius + "&format=json&app_id=YOUR_APP_ID"
		data = json.load(urllib2.urlopen(url))

		#titles = [ i.get("title") for i in data]
		raw_dts = json.dumps([i.get("datetime") for i in data])
		
		#formatted_dts = [i.get("formatted_datetime") for i in data]
		ticket_urls = json.dumps([i.get("ticket_url").encode("utf-8") for i in data])
		ticket_statuses = json.dumps([i.get("ticket_status").encode("utf-8") for i in data])
		venues = json.dumps([i["venue"] for i in data])
		# venue_names = [i.get("venue").get("name").encode("utf-8") for i in data]
		# venue_cities = [i.get("venue").get("city").encode("utf-8") for i in data]
		# venue_region = [i.get("venue").get("region").encode("utf-8") for i in data]



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
		# print "\nvenue names\n"
		# print venue_names
		# print "\nvenue cities\n"
		# print venue_cities
		# print "\nvenue region\n"
		# print venue_region
	
		context = {
			"queryform" : queryform,
			"modalform" : modalform,
			"form_artistSelect" : form_artistSelect,
			"raw_dts" : raw_dts,
			"ticket_urls" : ticket_urls,
			"ticket_statuses" : ticket_statuses,
			"venues" : venues,
		}

	else:
		context = {
			"queryform" : queryform	

		}
	#print "modal form is valid = " + str(modalform.is_valid())
	if modalform.is_valid():
		form_recipient = modalform.cleaned_data.get("rec_email")
	     	form_message = modalform.cleaned_data.get("message")
     		form_recname = modalform.cleaned_data.get("rec_name")
	     	print form_recipient
	     	print form_message
	     	print form_recname

	return render(request,"searchform.html" , context)


# def invite(request, invite_name_url):
# 	context = RequestContext(request)
# 	invite_data = get_invite_Info()

# 	context_dict = {'invite_data': invite_data }

# 	try:

# 	return render(request, "searchform.html")

# @login_required
# def invite_sender(request):
# 	context = RequestContext(request)
# 	concertDate = None
# 	recipient = None
# 	concert_id = None
# 	artist_id = None
# 	message = None
# 	rec_name = None
# 	ticket_url = None
# 	if request.method == 'GET':
# 		concertDate = request.GET['raw_dts']
# 		recipient = request.GET['rec_email']
# 		concert_id = request.GET['concert_id']
# 		artist_id = request.GET['artist_id']
# 		message = request.GET['message']
# 		rec_name = request.GET['rec_name']
# 		ticket_url = request.GET['ticket_url']

# 	rec_email = recipient
# 	message = message
# 	rec_full_name = rec_name
# 	concert_url = ticket_url

	
# 	subject = "Site contact form"
# 	from_email = settings.EMAIL_HOST_USER
# 	to_email = [rec_email, from_email, 'celijahh@gmail.com']
# 	contact_message = ''' You have received a Concert Invite
# 	%s: %s concert tickets url: %s via %s
# 	'''%(rec_full_name, message,concert_url ,rec_email)
# 	send_mail(subject, contact_message, from_email, to_email, fail_silently =False)

# 	if request.user.is_authenticated():
# 		user_id = request.user.id
# 	if user_id:
# 		user = User.objects.get(id=int(user_id))
# 		concert = Concert.objects.get(id = int(concert_id))
# 		artist = Artist.objects.get(id = int(artist_id))
# 		if user:
# 			invite = Invite(user, rec_email, concert, artist, message )
# 			invite.save()
# 	return render(request,"searchform.html")

# def save(request):

# 	return render(request, "searchform.html")


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
