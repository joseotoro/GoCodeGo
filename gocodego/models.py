from django.db import models

class Problem(models.Model):
	# Title of the problem
	title = models.CharField(max_length=200)

	# Description of the problem	
	description = models.CharField(max_length=2000)

	# Template with initial code for start coding
	template = models.CharField(max_length=2000)

	# Code for check the solution
	test_cases = models.CharField(max_length=2000)

	# Publication date
	pub_date = models.DateTimeField('date published')
