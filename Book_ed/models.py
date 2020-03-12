from django.db import models
from phone_field import PhoneField

class User(models.Model):
	username = models.CharField(max_length = 30)
	name = models.CharField(max_length = 200)
	email_id = models.EmailField(max_length = 255)
	mobile = PhoneField(blank = True, help_text = 'Contact_number')
	address = models.TextField()
	
class Book(models.Model):
	types = [('R', 'Romantic'), ('T', 'Thriller'), ('S', 'Study_Books')] #and others obviously
	lender = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length = 200)
	author = models.CharField(max_length = 200)
	available = models.BooleanField()
	genre = models.CharField(max_length = 1, choices = types)
	


