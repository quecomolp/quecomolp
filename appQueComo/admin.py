from django.contrib import admin
from appQueComo.models import singleRestaurante, menu, tipoComidas, ServiciosParaOfrecer, DatosRestaurante, DatosPersonaRegistrada, ImagenComida

admin.site.register(singleRestaurante)
admin.site.register(menu)
admin.site.register(tipoComidas)
admin.site.register(ServiciosParaOfrecer)
admin.site.register(DatosRestaurante)
admin.site.register(DatosPersonaRegistrada)
admin.site.register(ImagenComida)