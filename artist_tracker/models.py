from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class SignUp(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length = 120, blank = True, null = True)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)


	def __unicode__(self):
		return self.email



class Concert(models.Model):
	user = models.ForeignKey(User, null = True, on_delete = models.CASCADE)
	concert_name = models.CharField(max_length = 120, blank = True, null = True)
	venue = models.CharField(max_length = 120, blank = True, null = True)
	city = models.CharField(max_length = 120, blank = True, null = True)
	state = models.CharField(max_length = 120, blank = True, null = True)
	country = models.CharField(max_length = 120, blank = True, null = True)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)

	def __unicode__(self):
		return self.email
		
class Artist(models.Model):
	artist_name = models.CharField(max_length = 120, blank = True, null = True)
	genre = models.CharField(max_length = 64, blank = True, null = True)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	description = models.CharField(max_length = 200, blank = True, null = True)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)
	concerts = models.ManyToManyField(Concert, through = 'ConcertOf')

	def __unicode__(self):
		return self.full_name

class Follow(models.Model):
	artist = models.ForeignKey(Artist, on_delete = models.CASCADE)
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	date_followed = models.DateField()

class Invite(models.Model):
	sender = models.ForeignKey(User, related_name= "invite_sender", on_delete = models.CASCADE)
	recipient = models.EmailField()
	concert = models.ForeignKey(Concert, on_delete = models.CASCADE)
	artist = models.ForeignKey(Artist, on_delete = models.CASCADE)
	message = models.CharField(max_length = 120, blank = True, null = True)
	date_sent = models.DateTimeField(auto_now_add = True, auto_now = False)


class ConcertOf(models.Model):
	artist = models.ForeignKey(Artist, on_delete = models.CASCADE)
	concert = models.ForeignKey(Concert, on_delete = models.CASCADE)
	date_added = models.DateField()

	



