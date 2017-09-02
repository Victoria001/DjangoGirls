from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
	titulo=models.CharField(max_length=100)
	contenido=models.TextField()
	fecha_creacion=models.DateTimeField(default=timezone.now)
	fecha_publicacion=models.DateTimeField(blank=True, null=True) # puede ser nulo o vacio
	autor=models.ForeignKey('auth.User')


	# metodos
	#metodo para imprimir el titulo del post
	def __str__(self):
		return self.titulo

	#metodo para publicar el post
	def __publicar__(self): #con self digo mio, osea mi fecha de publicacion
		self.fecha_publicacion=timezone.now() #va actualizar la hora de publicacion
		self.save() #save para guardar la publicacion en la bd
