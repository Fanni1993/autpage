from django.db import models

class Cards (models.Model):
	def __str__(self):
		return self.card_title
	
	card_title= models.CharField(max_length=50)
	card_content = models.CharField(max_length=200)
	


