from django.db import models

class Cliente(models.Model):
	nombre		= models.CharField(max_length=50)
	apellido 	= models.CharField(max_length=50)
	cedula 		= models.CharField(max_length=2)
	teléfono 	= models.CharField(max_length=10)
	correoElectrónico = models.EmailField()
    

	def __str__(self):
		return self.nombre