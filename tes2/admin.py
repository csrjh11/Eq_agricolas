from django.contrib import admin
from .models import(
    Equipo,
    Imagen,
    Usuario,
    Tractor,
    Transaccion,
    Ubicacion,
    Solicitud,
    Mensaje,
    Arado,
    Rastra,
    Sembradora,
    Pulverizadora,
    Cosechadora,



)

# Register your models here.
admin.site.register(Equipo)
admin.site.register(Usuario)
admin.site.register(Tractor)
admin.site.register(Imagen)
admin.site.register(Transaccion)
admin.site.register(Ubicacion)
admin.site.register(Solicitud)
admin.site.register(Mensaje)
admin.site.register(Arado)
admin.site.register(Rastra)
admin.site.register(Sembradora)
admin.site.register(Pulverizadora)
admin.site.register(Cosechadora)
