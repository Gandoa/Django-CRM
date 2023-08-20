from django.db import models

# Create your models here.

class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	prénom = models.CharField(max_length=50)
	nom =  models.CharField(max_length=50)
	email =  models.CharField(max_length=100)
	numéro = models.CharField(max_length=15)
	addresse =  models.CharField(max_length=100)

	def __str__(self):
		return(f"{self.prénom} {self.nom}")
