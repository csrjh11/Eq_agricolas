from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import  ChoiceWidget, NumberInput
from .models import Arado, Cosechadora, Equipo, Imagen, Pulverizadora, Rastra, Sembradora, Tractor, Ubicacion, Usuario
import datetime

OPCIONES_TIPO_ARADO = (
    ("vertedera", "Vertedera"),
    ("disco","Disco"),
    ("cincel", "Cincel"),
    ("subsuelo", "Subsuelo"),
)

OPCIONES_TIPO_SEM = (
    ("de_voleo", "De Voleo"),
    ("chorrillo","A chorrillo"),
    ("presicion", "De Precisión"),

)

OPCIONES_NEU_MEC = (
    ("neumatico", "Neumática"),
    ("mecanico", "Mecánica"),
)

ahora = datetime.datetime.now()
año = ahora.year

class FormaEquipo(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop("usu")
        super().__init__(*args,**kwargs)
        ubi = Ubicacion.objects.filter(id_usuario = user).exclude(eliminado = True)
        self.fields["donde_esta"].queryset = ubi
    
    año = forms.IntegerField(widget = forms.NumberInput(attrs={"class":"form-control"}), min_value=1930, max_value = año + 1 )
    precio_venta = forms.FloatField(widget = forms.NumberInput(attrs={"class":"form-control"}), min_value=0 )
    precio_renta_dia = forms.FloatField(widget = forms.NumberInput(attrs={"class":"form-control"}), min_value=0 )
    marca = forms.ChoiceField(widget= forms.Select(attrs={"class":"form-control"}))
    modelo = forms.ChoiceField(widget= forms.Select(attrs={"class":"form-control"}))

    class  Meta:
        model = Equipo
        exclude = ["num_equipo", "id_dueño", "status", "ubicacion_base"]

        widgets = {
            "nombre_equipo": forms.TextInput(attrs={"class":"form-control"}),
            "tipo_equipo": forms.Select(attrs = {"class": "form-control"}),
            "descripcion": forms.Textarea(attrs = {"class":"form-control"}),
            "estado_equipo": forms.Select(attrs = {"class":"form-control"}),
            "donde_esta": forms.Select(attrs = {"class":"form-control"}),
            "para_que": forms.Select(attrs = {"class":"form-control"}),
        }



#################################################### Formas especificas de equipos ###########################
class FormaTractor(forms.ModelForm):
    potencia = forms.IntegerField(widget=NumberInput(attrs={"class":"form-control"}), min_value=1, label= "Potencia del Motor (HP)")
    estrias_PTO = forms.ChoiceField(choices = [6,21], widget= forms.Select(attrs={"class":"form-control"}), label= "Estrias de la Toma de Fuerza")
    enganche_tres_puntos = forms.BooleanField(label = "Tiene enganche de tres puntos?")
    traccion = forms.ChoiceField(choices= ["Delantera", "Trasera", "4WD"], label= "Tipo de Tracción", widget= forms.Select(attrs={"class":"form-control"}))
    cabina = forms.BooleanField(label = "Tiene Cabina?")

    class Meta:
        model = Tractor
        exclude = ["id_equipo"]


class FormaArado(forms.ModelForm):
    tipo = forms.ChoiceField(choices = OPCIONES_TIPO_ARADO, widget=forms.Select(attrs={"class":"form-control"}))
    no_cuerpos = forms.IntegerField(widget=NumberInput(attrs={"class":"form-control"}), min_value=1)
    neumatica_mecanica = forms.ChoiceField(choices=OPCIONES_NEU_MEC, widget=forms.Select(attrs = {"class":"form-control"}))


    class Meta:
        model = Arado
        exclude = ["id_equipo"]


class FormaRastra(forms.ModelForm):

    class Meta:
        model = Rastra
        exclude = ["id_equipo"]


class FromaSembradora(forms.ModelForm):
    tipo = forms.ChoiceField(choices = OPCIONES_TIPO_SEM, widget=forms.Select(attrs={"class":"form-control"}))
    neumatica_mecanica = forms.ChoiceField(choices=OPCIONES_NEU_MEC, widget=forms.Select(attrs = {"class":"form-control"}))
    no_tolvas = forms.IntegerField(widget=NumberInput(attrs={"class":"form-control"}), min_value=1)


    class Meta:
        model = Sembradora
        exclude = ["id_equipo"]


class FormaPulverizadora(forms.ModelForm):
    autopropulsada = forms.BooleanField( label= "Es Autopropulsada?")
    tamaño_tanque = forms.IntegerField(widget = forms.NumberInput(attrs={"class":"form-control"}), min_value=1, label= "Capacidad del Tanque (Litros)" )
    no_boquillas = forms.IntegerField(widget = forms.NumberInput(attrs={"class":"form-control"}), min_value=1, label= "Número de Boquillas" )
    capacidad_bomba = forms.IntegerField(widget = forms.NumberInput(attrs={"class":"form-control"}), min_value=1, label= "Capacidad de la Bomba" )

    class Meta:
        model = Pulverizadora
        exclude = ["id_equipo"]


class FromaCosechadora(forms.ModelForm):
    tipo_cultivo = forms.CharField( widget=forms.TextInput(attrs={"class":"form-control"}))
    potencia = forms.IntegerField(widget=NumberInput(attrs={"class":"form-control"}), min_value=1)
    capacidad_granos = forms.IntegerField(widget=NumberInput(attrs={"class":"form-control"}), min_value=1)
    tasa_descarga = forms.IntegerField(widget=NumberInput(attrs={"class":"form-control"}), min_value=1)

    class Meta:
        model = Cosechadora
        exclude = ["id_equipo"]
 #################################################### Terminan Formas especificas de equipos ###########################
      

class Forma_Registro_Usuario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label = "contraseña", widget = forms.PasswordInput)
    password2 = forms.CharField(label = "Confirma contraseña", widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}

class Forma_Registro_Ubicacion(forms.ModelForm):

    class Meta:
        model = Ubicacion
        fields = ["alias", "referencias"]
        help_texts = {k:"" for k in fields}
        widgets = {
            "alias": forms.TextInput(attrs={"class":"form-control"}),
            "referencias": forms.Textarea(attrs={"class":"form-control"})
        }

class Forma_Edicion_Ubicacion(forms.ModelForm):

    class Meta:
        model = Ubicacion
        fields = ["alias", "referencias"]
        help_texts = {k:"" for k in fields}
        widgets = {
            "alias": forms.TextInput(attrs={"class":"form-control", "disabled":True}),
            "referencias": forms.Textarea(attrs={"class":"form-control", "disabled":True})
        }



class Forma_Datos_Interesado(forms.ModelForm):

    nombre = forms.TextInput(attrs={"class": "form-control"})

    class Meta:
        model = Usuario
        exclude = ["id_usuario", "nivel_permisos", "usuario_activo"]


class Forma_Imagen(forms.ModelForm):


    class Meta:
        model = Imagen
        fields = ["imagen"]
