from django.contrib import admin
from .models import(
    Equipo,
    Imagen,
    Usuario,
    Tractor,
    Transaccion,
    Ubicacion,
    Solicitud,
    Mensaje
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