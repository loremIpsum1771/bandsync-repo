from django.db import models

# Create your models here.
class SignUp(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length = 120, blank = True, null = True)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)


	def __unicode__(self):
		return self.email

class User(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length = 120, blank = True, null = True)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)
	invites = models.ManyToManyField('self', through = 'Invite', 
		symmetrical = False )

	def __unicode__(self):
		return self.full_name

class Invite(models.Model):
	sender_id = models.Foreignkey(User, on_delete = models.CASCADE )
	recipient_id = models.Foreignkey(User,on_delete = models.CASCADE)
	concert_id = models.AutoField()
	artist_id = models.AutoField()
	message = models.CharField(max_length = 120, blank = True, null = True)
	date_sent = models.DateTimeField(auto_now_add = True, auto_now = False)


class Artist(models.Model):
	artist_name = models.CharField(max_length = 120, blank = True, null = True)
	genre = models.CharField(max_length = 64, blank = True, null = True)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	description = models.CharField(max_length = 200, blank = True, null = True)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)
	followers = models.ManyToManyField(Users, through= 'Follow')
	concerts = models.ManyToManyField(Concert, through = 'ConcertOf')

	def __unicode__(self):
		return self.full_name

class Follow(models.Model):
	user = models.Foreignkey(Users, on_delete = models.CASCADE)
	artist = models.Foreignkey(Artist, on_delete = models.CASCADE)
	date_followed = models.DateField()

class Concert(models.Model):
	email = models.EmailField()
	concert_name = models.CharField(max_length = 120, blank = True, null = True)
	venue = models.CharField(max_length = 120, blank = True, null = True)
	city = models.CharField(max_length = 120, blank = True, null = True)
	state = models.CharField(max_length = 120, blank = True, null = True)
	country = models.CharField(max_length = 120, blank = True, null = True)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)

	def __unicode__(self):
		return self.email

class ConcertOf(models.Model):
	artist = models.Foreignkey(Artist, on_delete = models.CASCADE)
	concert = models.Foreignkey(Concert, on_delete = models.CASCADE)
	date_added = models.DateField()

	
# class calendar(models.Model):
# 	email = models.EmailField()
# 	full_name = models.CharField(max_length = 120, blank = True, null = True)
# 	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
# 	updated = models.DateTimeField(auto_now_add = False, auto_now = True)

# 	def __unicode__(self):
# 		return self.email



