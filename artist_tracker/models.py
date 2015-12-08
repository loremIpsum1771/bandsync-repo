from django.db import models
from django.contrib.auth.models import User #AbstractBaseUser, BaseUserManager

# Create your models here.
class SignUp(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length = 120, blank = True, null = True)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)


	def __unicode__(self):
		return self.email


# class UserManager(BaseUserManager):
# 	def create_user(self, email,password= None):
# 		user = self.model(email=email)
# 		return user 
# 	def create_superuser(slef, email,password):
# 		user = self.create_user(email,password=password)
# 		user.save()
# 		return user 

# class User(AbstractBaseUser):
# 	email = models.EmailField()
# 	# full_name = models.CharField(max_length = 120, blank = True, null = True)
# 	user_name = models.CharField(max_length = 40, unique =True)
# 	USERNAME_FIELD = "user_name"
# 	REQUIRED_FIELDS = ['email']
# 	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
# 	updated = models.DateTimeField(auto_now_add = False, auto_now = True)
# 	invites = models.ManyToManyField(
# 		'self', through = 'Invite', 
# 		symmetrical = False )

# 	def __unicode__(self):
# 		return self.full_name

# 	def get_full_name():
# 		return self.






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
		
class Artist(models.Model):
	artist_name = models.CharField(max_length = 120, blank = True, null = True)
	genre = models.CharField(max_length = 64, blank = True, null = True)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	description = models.CharField(max_length = 200, blank = True, null = True)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)
	#followers = models.ManyToManyField(Users, through= 'Follow')
	concerts = models.ManyToManyField(Concert, through = 'ConcertOf')

	def __unicode__(self):
		return self.full_name

# class Follow(models.Model):
# 	user = models.ForeignKey(Users, on_delete = models.CASCADE)
# 	artist = models.ForeignKey(Artist, on_delete = models.CASCADE)
# 	date_followed = models.DateField()
class Invite(models.Model):
	sender = models.ForeignKey(User, related_name= "invite_sender", on_delete = models.CASCADE )
	recipient = models.ForeignKey(User, related_name= "invite_recipient", on_delete = models.CASCADE)
	concert = models.ForeignKey(Concert, on_delete = models.CASCADE)
	artist = models.ForeignKney(Artist, on_delete = models.CASCADE)
	message = models.CharField(max_length = 120, blank = True, null = True)
	date_sent = models.DateTimeField(auto_now_add = True, auto_now = False)


class ConcertOf(models.Model):
	artist = models.ForeignKey(Artist, on_delete = models.CASCADE)
	concert = models.ForeignKey(Concert, on_delete = models.CASCADE)
	date_added = models.DateField()

	
# class calendar(models.Model):
# 	email = models.EmailField()
# 	full_name = models.CharField(max_length = 120, blank = True, null = True)
# 	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
# 	updated = models.DateTimeField(auto_now_add = False, auto_now = True)

# 	def __unicode__(self):
# 		return self.email



