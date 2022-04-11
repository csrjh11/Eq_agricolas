
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import PositiveSmallIntegerField


# Create your models here.

OPCIONES_TIPO = (
    ("tractor","TRACTOR"),
    ("arado","ARADO"),
    ("rastra","RASTRA"),
    ("sembradora", "SEMBRADORA"),
    ("pulverizadora","PULVERIZADORA"),
    ("cosechadora","COSECHADORA"),
    ("otros","OTROS"),    
)
OPCIONES_USO = (
    ("venta", "Venta"),
    ("renta", "Renta"),
    ("ambos", "Ambos")
)

OPCIONES_ESTADO = (
    ("malo", "Malo"),
    ("regular", "Regular"),
    ("buena", "Buena"),
    ("excelente", "Excelente"),
)

OPCIONES_STATUS = (
    ("activo", "Activo"),
    ("apartado", "Apartado"),
    ("rentado", "Rentado"),
    ("inactivo", "Inactivo"),
    ("eliminado", "Eliminado"),
)

OPCIONES_STATUS_TRANSACCION = (
    ("1", "Completada"),
    ("2", "Abortada"),
    ("3", "En Ejecución"),
    ("4", "En Espera"),
)

OPCIONES_STATUS_SOLICITUD = (
    ("1", "En Espera"),
    ("2", "Aceptada"),
    ("3", "Rechazada"),
)


class Usuario(models.Model):
    id_usuario = models.OneToOneField(User, null = True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=25, null = True, blank= True)
    apellido_1 = models.CharField(max_length=30, null = True)
    apellido_2 = models.CharField(max_length= 30, null = True, blank=True)
    telefono = models.CharField(max_length= 20, null = True, blank=True)
    celular = models.CharField(max_length= 20)
    nivel_permisos = models.PositiveSmallIntegerField(default=1)
    usuario_activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Ubicacion(models.Model):
    id_ubicacion = models.CharField(max_length=200, primary_key=True)
    id_usuario   = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    alias = models.CharField(max_length=200)
    coord_x = models.CharField(max_length= 20)
    coord_y = models.CharField(max_length= 20)
    estado = models.CharField(max_length=70, null= True)
    municipio = models.CharField(max_length=100, null= True)
    referencias = models.CharField(max_length=200)
    area = models.PositiveSmallIntegerField(default= 1)
    eliminado = models.BooleanField(default= False)

    def __str__(self):
        return self.alias


class Equipo(models.Model):
    num_equipo = models.CharField(max_length= 10, primary_key= True)
    nombre_equipo = models.CharField(max_length=100, default= "")
    id_dueño = models.ForeignKey(User, on_delete= models.CASCADE)
    tipo_equipo = models.CharField(max_length=20, choices= OPCIONES_TIPO, null = True, blank= False)
    descripcion = models.CharField(max_length= 200)
    marca = models.CharField(max_length= 20, default= "")
    modelo = models.CharField(max_length= 20, default= "")
    año = models.PositiveSmallIntegerField(default=1993)
    estado_equipo = models.CharField(choices=OPCIONES_ESTADO, max_length=10)
    donde_esta = models.ForeignKey(Ubicacion,null = True, on_delete= models.SET_NULL, related_name= "donde_esta")
    ubicacion_base = models.ForeignKey(Ubicacion, on_delete= models.SET_NULL, null = True, related_name= "ubcacion_base")
    para_que = models.CharField(choices= OPCIONES_USO, max_length= 10)
    hecatreas_trabajadas = models.FloatField( default = 1)
    precio_venta = models.FloatField(null=True)
    precio_renta_dia = models.FloatField(null=True)
    status = models.CharField(choices=OPCIONES_STATUS, max_length=10)

    def __str__(self):
        return self.nombre_equipo
    
    @property
    def que_es(self):
        return self.tipo_equipo.capitalize()


###################################################################################### Equipos "de apoyo" #############################################################################
class Tractor(models.Model):
    id_equipo = models.OneToOneField(Equipo, max_length=10, on_delete= models.CASCADE, primary_key=True)
    potencia = models.CharField(max_length=4)
    estrias_PTO = models.CharField(max_length= 2)
    enganche_tres_puntos = models.BooleanField()
    traccion = models.CharField(max_length=9)
    cabina = models.CharField(max_length=10)

    @property
    def tipo_tractor(self):
        if self.potencia <= 115:
            return "Pequeño"
        if self.potencia > 115 and self.potencia <= 165:
            return "Mediano"
        if self.potencia > 165:
            return "Grande"


class Sembradora(models.Model):
    id_equipo = models.OneToOneField(Equipo, max_length=10, on_delete= models.CASCADE, primary_key=True)    
    tipo = models.CharField(max_length= 20)
    fertilizadora = models.BooleanField(default=False)
    no_tolvas = models.PositiveSmallIntegerField()
    neumatica_mecanica = models.CharField(max_length=15)


class Arado(models.Model):
    id_equipo = models.OneToOneField(Equipo, max_length=10, on_delete= models.CASCADE, primary_key=True) 
    tipo = models.CharField(max_length= 20)
    reversible = models.BooleanField(default= False)
    no_cuerpos = PositiveSmallIntegerField()
    neumatica_mecanica = models.CharField(max_length= 15, null = True)


class Pulverizadora(models.Model):
    id_equipo = models.OneToOneField(Equipo, max_length=10, on_delete= models.CASCADE, primary_key=True)
    autopropulsada = models.BooleanField(default= False)
    tamaño_tanque = models.PositiveSmallIntegerField()
    no_boquillas = PositiveSmallIntegerField()
    capacidad_bomba = models.PositiveSmallIntegerField()


class Rastra(models.Model):
    id_equipo = models.OneToOneField(Equipo, max_length=10, on_delete= models.CASCADE, primary_key=True)
    acople = models.CharField(max_length= 20)
    tipo_cuerpo = models.CharField(max_length=20)
    no_cuerpos = PositiveSmallIntegerField()
    disposicion_cuerpos = models.CharField(max_length= 15)


class Cosechadora(models.Model):
    id_equipo = models.OneToOneField(Equipo, max_length=10, on_delete= models.CASCADE, primary_key=True)
    tipo_cultivo = models.CharField(max_length= 20)
    potencia = PositiveSmallIntegerField()
    capacidad_granos = models.PositiveSmallIntegerField(null = True)
    tasa_descarga = models.PositiveSmallIntegerField(null = True)


class Otros_equipos(models.Model):
    id_equipo = models.OneToOneField(Equipo, max_length=10, on_delete= models.CASCADE, primary_key=True)
    potencia = models.PositiveSmallIntegerField(null = True)
    producto_agricola = models.CharField(max_length=30)

########################################### Termina Equipos "de apoyo" ####################################

class Transaccion(models.Model):
    id_transaccion = models.AutoField(max_length = 10, primary_key=True)
    id_equipo = models.ForeignKey(Equipo, on_delete = models.SET_DEFAULT, default = "0001")
    id_dueño = models.ForeignKey(Usuario, on_delete=models.SET_DEFAULT, default="0001", related_name="dueño_usuario")
    id_arrendatario = models.ForeignKey(Usuario, on_delete = models.SET_DEFAULT, default="0001", related_name="arrendatario_usuario")
    desde_donde = models.ForeignKey(Ubicacion, on_delete = models.SET_DEFAULT, default = "0001", related_name = "desde_donde_ubicacion")
    hacia_donde = models.ForeignKey(Ubicacion, on_delete = models.SET_DEFAULT, default = "0002", related_name = "hacia_donde_ubicacion")
    estatus = models.CharField(choices = OPCIONES_STATUS_TRANSACCION, max_length = 12)
    fecha_inicial = models.DateField(default= "2021-06-22")
    fecha_final = models.DateField(null =True, blank=True)
    importe_total = models.FloatField()
    numero_hectareas = models.IntegerField(default=1)
    tipo_transaccion = models.CharField(max_length = 5)


class Imagen(models.Model):
    id_imagen = models.AutoField(primary_key=True)
    id_equipo = models.ForeignKey(Equipo, on_delete= models.CASCADE, null = True)
    id_usuario = models.ForeignKey(Usuario, on_delete= models.CASCADE, null = True)
    imagen = models.ImageField(upload_to="images/", blank = True)
    es_principal = models.BooleanField(default=False)
    es_identificacion = models.BooleanField(default = False)

    @property
    def imageURL(self):
        try:
            url = self.imagen.url
        except:
            url = ""
        return url


class Solicitud(models.Model):
    """Solicitud de renta o compra de un equipo"""
    id_solicitud = models.AutoField(primary_key = True)
    id_solicitante = models.ForeignKey(Usuario, on_delete= models.CASCADE, related_name = "sol_sol")
    id_dueño_eq = models.ForeignKey(Usuario,on_delete = models.CASCADE, related_name = "sol_dueño", blank=True,null =True)
    id_equipo = models.ForeignKey(Equipo, on_delete=models.SET_NULL, blank=True,null = True)
    tipo_equipo = models.CharField(null = True, blank=True, max_length = 30)
    parametro_1 = models.CharField(null = True, blank=True, max_length = 30)
    parametro_2 = models.CharField(null = True, blank=True, max_length = 30)
    parametro_3 = models.CharField(null = True, blank=True, max_length = 30)
    parametro_4 = models.CharField(null = True, blank=True, max_length = 30)
    parametro_5 = models.CharField(null = True, blank=True, max_length = 30)
    comentario = models.CharField(max_length = 255, null = True, blank = True)
    tipo_operacion = models.CharField(max_length=10)
    a_donde = models.ForeignKey(Ubicacion, on_delete=models.SET_DEFAULT, default="", related_name = "hacia_donde_sol")
    desde_donde = models.ForeignKey(Ubicacion, on_delete=models.SET_NULL, related_name = "dsde_donde_sol", null = True)
    fecha_solicitud = models.DateField()
    fecha_inicio = models.DateField(blank=True,null =True)
    fecha_final = models.DateField(null =True, blank=True)
    estatus = models.CharField( max_length=10, default = "1")
    costo = models.IntegerField(blank=True,null =True)
    hectareas_trabajar = models.PositiveSmallIntegerField(blank=True,null = True)
    tipo_solicitud = models.PositiveSmallIntegerField(default= 1)
        # Tipo de solicitud
        # 1 = "normal",
        # 2 = "solicitud sin equipo"
        # 3 = "solicitud respuesta"
    sol_respondida = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True,null = True)
    quien_manda = models.ForeignKey(Usuario, on_delete=models.SET_NULL, related_name= "sol_remitente",blank=True, null = True)

    @property
    def estatus_sol(self):
        if self.estatus == "1":
            return "En Espera de Respuesta"
        if self.estatus == "2":
            return "Aceptada"
        if self.estatus == "3":
            return "Rechazada"
        if self.estatus == "4":
            return "Respondida"
        if self.estatus == "5":
            return "Finalizada"

class Conversacion(models.Model):
    id_conversacion = models.AutoField(primary_key=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    id_transaccion = models.ForeignKey(Transaccion, on_delete=models.CASCADE, null = True, blank = True)
    id_solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE, null = True, blank = True)
    usuario_1 = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name= "usr_1_convo")
    usuario_2 = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name= "usr_2_convo")


class Mensaje(models.Model):
    id_mensaje = models.AutoField(primary_key=True)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    remitente = models.ForeignKey(User, on_delete= models.CASCADE)
    id_conversacion = models.ForeignKey(Conversacion, on_delete=models.CASCADE)
