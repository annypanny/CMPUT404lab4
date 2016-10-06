from django.db import models

import datetime
from django.utils import timezone

# Create your models here.
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Question(models.Model): #this is going to be a table
	#this is going to be column/field in the Question table
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.question_text
	def was_published_recently(self):
		now = timezone.now()
# want this to return true if the question was published in the last day
		#return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
		# test result: True != False 
		# if publish date - yesterday, then it's true, but it's future
		return now - datetime.timedelta(days=1) <= self.pub_date <= now 

@python_2_unicode_compatible
class Choice(models.Model):
	question = models.ForeignKey(Question,on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text
