from django.contrib import admin
from appQueComo.models import singleRestaurante, menu, tipoComidas, ServiciosParaOfrecer, DatosRestaurante, DatosPersonaRegistrada, ImagenComida

class imagenComidaAdmin (admin.StackedInline):
	model = ImagenComida
	extra = 5

class singleRestauranteAdmin (admin.ModelAdmin):
	fieldsets = [
		('Persona registrada', { 'fields': ['datosPersonaRegistrada'] }),
		('Datos del comercio', { 'fields': ['datosRestaurante'] }),
	]
	list_display = ('datosRestaurante', 'datosPersonaRegistrada')

class MenuAdmin (admin.ModelAdmin):
	inlines = [imagenComidaAdmin]

admin.site.register(singleRestaurante, singleRestauranteAdmin)
admin.site.register(menu, MenuAdmin)
admin.site.register(tipoComidas)
admin.site.register(ServiciosParaOfrecer)
admin.site.register(DatosRestaurante)
admin.site.register(DatosPersonaRegistrada)
admin.site.register(ImagenComida)