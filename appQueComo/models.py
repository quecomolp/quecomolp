from django.db import models

class menu (models.Model):
	"""
	Clase para cada comida, nombre, el precio, una imagen y la puntuacion
	"""
	nombre = models.CharField ( max_length = 250 )
	precio = models.IntegerField ()
	class Meta:
		ordering = ['nombre']
	def __unicode__ (self):
		return unicode(self.nombre)

class tipoComidas (models.Model):
	"""
	Clase para los distintos tipos de comida
	"""
	nombre = models.CharField ( max_length = 250 )
	class Meta:
		ordering = ['nombre']
	def __unicode__ (self):
		return unicode (self.nombre)

class ServiciosParaOfrecer (models.Model):
	"""
	Tipos de servicios servicios ofrecidos
	"""
	delivery = models.BooleanField()
	restaurante = models.BooleanField()

class DatosRestaurante (models.Model):
	"""
	Datos que conciernen al restaurante
	"""

	#listado de Categorias
	categorias = (
		('nivel1', 'una'),
		('nivel2', 'dos'),
		('nivel3', 'tres'),
		('nivel4', 'cuatro'),
		('nivel5', 'cinco'),
		('nivel6', 'seis'),
		)

	nombre = models.CharField ( max_length = 250 )
	telefono = models.CharField ( max_length = 250 )
	sitioWeb = models.CharField (max_length = 250)
	correoElectronico = models.CharField (max_length=250)
	calle = models.CharField ( max_length = 250 )
	altura = models.IntegerField ()
	localidad = models.CharField ( max_length = 250 )
	provincia = models.CharField ( max_length = 250 )
	serviciosOfrecidos = models.ForeignKey (ServiciosParaOfrecer)
	zonaEntrega = models.TextField()
	informacionResturante = models.TextField()
	diasLaboralesyHorarios = models.TextField()
	categoriaRestaurante = models.CharField ( max_length = 6, choices = categorias, default = 'nivel1' )
	tipoDeComidas = models.ForeignKey ( tipoComidas )
	class Meta:
		ordering = ['nombre']
	def __unicode__ (self):
		return unicode (self.nombre)

class DatosPersonaRegistrada (models.Model):
	"""
	Datos de la persona que se registra 
	"""
	nombreContacto = models.CharField ( max_length = 250 )
	mailContacto = models.CharField ( max_length = 250 )
	contrasenaContacto = models.CharField (max_length = 250)
	class Meta:
		ordering = ['nombreContacto']
	def __unicode__(self):
		return unicode(self.nombreContacto)


class singleRestaurante (models.Model):
	"""
	Clase Parent
	"""
	datosRestaurante = models.ForeignKey ( DatosRestaurante )
	datosPersonaRegistrada = models.ForeignKey ( DatosPersonaRegistrada )

class ImagenComida (models.Model):
	"""
	Imagen de cada una de las comidas que forman parte del menu
	"""
	property = models.ForeignKey(menu)
	imagenComida = models.FileField(upload_to='comidas/%m', blank = True)

	class Admin:
		pass