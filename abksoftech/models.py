from django.db import models

# Create your models here.
class Banner(models.Model):
	"""Banner db schema"""
	banner_id = models.AutoField
	banner_name = models.CharField(max_length = 100)
	banner_desc = models.CharField(max_length = 200)
	banner_img = models.ImageField(upload_to = "abksoftech/images", default = "")

	def __str__(self):
		return self.banner_name

class Profile(models.Model):
	"""Profile db schema"""
	profile_id = models.AutoField
	profile_username = models.CharField(max_length = 50)
	profile_firstname = models.CharField(max_length = 20)
	profile_lastname = models.CharField(max_length = 20)
	profile_email = models. EmailField(max_length=254)
	profile_contact = models.IntegerField()
	profile_github = models.URLField(max_length=200)
	profile_twitter = models.URLField(max_length=200)
	profile_instagram = models.URLField(max_length=200)
	profile_facebook = models.URLField(max_length=200)
	profile_linkedin = models.URLField(max_length=200)
	profile_about = models.CharField(max_length = 1000)
	def __str__(self):
		return self.profile_username


		