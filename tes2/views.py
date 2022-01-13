from PIL import Image
from django.contrib.auth.models import User
from django.db.models.query import RawQuerySet
from django.forms.forms import Form
from django.contrib import messages
from django.shortcuts import redirect, render
from django.core.exceptions import PermissionDenied
from .forms import FormaArado, FormaEquipo, FormaPulverizadora, FormaRastra, FormaTractor, Forma_Imagen, Forma_Registro_Usuario, Forma_Registro_Ubicacion, Forma_Datos_Interesado, FromaCosechadora, FromaSembradora, Forma_Edicion_Ubicacion
from django.http import JsonResponse, request
from .models import Arado, Cosechadora, Equipo, Imagen, Pulverizadora, Rastra, Sembradora, Solicitud, Ubicacion, Usuario, Tractor, Transaccion, Conversacion, Mensaje
from django.contrib.auth import authenticate, login
from django.db.models import Q
from django.core.paginator import Paginator
from django.core.files.uploadedfile import InMemoryUploadedFile


import random, math, json, os, io, sys
from datetime import date
hoy = date.today()


letras = ["a","b","c","d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s"
, "t", "u", "v", "w", "x", "y", "z"]
lista_estado = ["buena", "regular", "excelente"]

poligono = [[32.590371430865,-115.353230967552] , [32.1687552225146,-115.130849517825] , [31.2504059514186,-113.023707252242] , [28.2864362723137,-110.987817321236] , [27.9774834479049,-110.665480712793],
[27.2041059542213,-110.331452118913] , [27.1055766021287,-109.961168677345] , [27.0523006935245,-109.898849485091] , [26.7970761363627,-109.842759907393] , [26.7189496140147,-109.74158342766],
[26.7715488198678,-109.49835174255] , [26.5204326281206,-109.230053862614] , [26.2936428372166,-109.071235906813] , [26.1240509440741,-109.146969758509] , [26.0621889353586,-109.379663530705],
[25.8414115297344,-109.40665592121] , [25.6609943793566,-109.066718922228] , [25.6918251788766,-108.91251969624] , [25.3103626721964,-108.453596949896] , [25.356552698236,-108.331521242865],
[24.8965914652215,-107.849816054414] , [24.7020010623742,-107.952938001995] , [24.5464166693237,-107.547776715395] , [24.1649853137244,-107.160715240295] , [22.3992947120164,-105.59362394487],
[22.0901929055445,-105.320724424331] , [21.5245405307161,-105.017905005444] , [20.0515855401093,-105.37939442891] , [18.4404254295469,-103.213617189345] , [16.4177163270322,-98.1103445798246],
[15.906024618437,-96.4802266683131] , [16.4798350111372,-94.9213773075974] , [15.4134766974572,-92.3186111338674] , [18.0134957367909,-91.0022123115147] , [18.2090975693009,-88.8831723201567],
[18.536108737744,-88.3859216971196] , [21.395305974255,-87.1687010217969] , [20.9437805204484,-90.2503353637974] , [18.9412193843968,-90.6075994323124] , [17.9510758687793,-94.6508034880085],
[20.1191001618559,-97.3205086711438] , [22.1369994715173,-97.9139853617719] , [25.7883360369662,-97.5946679929352] , [25.9080747138249,-98.4593719612581] , [27.7187120282154,-100.225234466866],
[29.5782631009026,-101.454897432954] , [29.595864342362,-102.547477909065] , [28.7997244956289,-103.164931233286] , [29.0446303707273,-103.690295585339] , [29.5230276254138,-104.638137361869],
[30.324422415936,-104.861944060879] , [31.6320139573958,-106.541857701487] , [31.6435738384791,-108.073042844429] , [31.2254308838856,-108.006927351132] , [31.2289831530016,-111.101959040849],
[32.590371430865,-115.353230967552]
]

listaMarcas = ['Case', 'Claas', 'Deutz-Fahr', 'Fendt', 'Ford', 'John Deere', 'Kubota', 'Massey Ferguson', 'New Holland', 'Valtra']

modelos = {
  "Case": {
    "tractor" : ["Steiger", "Magnum AFS", "Puma", "Maxxum", "Farmall", ],
    "arado" : ['1-F194', '1-F296', '10', '125', '140', '145', '155', '165', '189', '193', '194', '1AV-193', '203S', '204S', '210',  '213S',  '214S', '215', '295', '296', '30 SERIES','58C SERIES', '60',
    '600 SERIES', '6000', '60L', '620', '641', '642', '6500', '6650', '70', '700-SERIES', '70L', '710', ],
    "rastra" : ['122', '310', '350', '370', '3800', '3850', '3900', '3950', '475', '485', '496', '501', '596', '696', '760', '770', '780', ],
    "sembradora": ['30', '40', '500', '510', '5100', '5200', '5300', '620', '6200', '6300', '7100', '7200', '8500', '8600', 'CONCORD', 'SDX30', 'SDX40', ],
    "pulverizadora": ["CIH", "Patriot", "SP", "SPX", "Trident", "TS"],
    "cosechadora" : ["Axial-Flow", "A8000", "A8800", ]
  },
  "Claas": {
    "tractor" : ["Xerion", "Axion", "Arion", "Elios", "Nexos", ],
    "cosechadora" : ["Lexion", "Trion"]
  },
  'Deutz-Fahr' : {
    "tractor" : ['5DF TTV ActiveSteer', '6145W HD', '6W Profi', '7250 TTV Agrotron', '8280 TTV', '9340 TTV Agrotron', 'Agroclimber', 'Agroclimber F/V', 'Agrofarm C', 'Agrofarm G', 'Agrofarm G - ROPS',
    'grolux', 'Agrolux', 'Agromaxx', 'Agroplus F Ecoline', 'Agroplus F Keyline', 'Agroplus F-V-S', 'Serie 2W', 'Serie 4E', 'Serie 4W', 'Serie 5G LRC', 'Serie 6', 'Serie 6', 'Serie 6G', 'Serie 6W', 'Serie 6W ', 'Series 4E', ],
    "cosechdora": ["C7206 TS", "Serie C6000", ]
  },
  "Fendt" : {
    "tractor" : ['Fendt 1100 Vario MT', 'Fendt 1000 Vario', 'Fendt 900 Vario', 'Fendt 800 Vario', 'Fendt 700 Vario', 'Fendt 500 Vario', 'Fendt 300 Vario', 'Fendt 200 Vario', ],
    "pulverizador" : ["Rogator 300", "Rogator 600", ],
    "cosechadora" : ["Ideal", "Serie C", "Serie SL", "Serie L", "Serie E"]
  },
  "Ford" : {
    "tractor" : ["7610", "7840", "5000", "2000", "6610", "6600", "3000", "4000", "7810", "TW25", "TW35"]
  },
  "John Deere" : {
    "tractor": ["1023E", "1025R", "2025R", "2032R", "2038R", "3025D", "3025E", "3032E", "3033R", "3035D", "3038E",  "3039R", "3043D", "3046R", "4044M", "4044R", "4052M", "4052M Heavy Duty", "4052R", "4066M", "4066M Heavy Duty", "4066R",
    "5075GL", "5075GL", "5075GN", "5075GV", "5090EL", "5090GN", "5090GV", "5100GN", "5100MH", "5100ML", "5115ML", "5115RH", "5125ML", "6120EH", "6155MH", "6155RH", "6R 175", "6R 195", "6R 215", "6R 230", "6R 250", "7R 210",
    "7R 230", "7R 250", "7R 270", "7R 290", "7R 310", "7R 330", "7R 350", "8R 230", "8R 250", "8R 280", "8R 310", "8R 340", "8R 370", "8R 410", "8RT 310", "8RT 340", "8RT 370", "8RT 410", "8RX 310", "8RX 340", "8RX 370",
    "8RX 410", "9R 390", "9R 440", "9R 490", "9R 540", "9R 590", "9R 640", "9RT 470", "9RT 520", "9RT 570", "9RX 490", "9RX 540", "9RX 590", "9RX 640", ],
    "arado" : ["624", "635", "645", "945", "975", "995", "3745", "3755", ],
    "rastra" : ["660", "670", "2633VT", "2660VT","MX225", "MX425", ],
    "sembadora" : ['1590', '1715', '1725', '1735', '1745', '1755', '1765', '1775', '1775NT', '1795', 'BD11', 'C650', 'DB44', 'DB60', 'DB66', 'DB80', 'DB90', 'DR12', 'DR16', 'DR24', ],
    "pulverizadora" : ['4630', '4730', 'Serie 400', 'Serie 600', 'Serie 800R', 'Serie Hagie', 'Serie PV', ],
    "cosechadora" : ["Serie CH", "Serie S", "Serie T", "Serie X", ]
  },
  "Kubota" : {
    "tractor" : ["Serie B", "Serie L", "Serie M", ]
  },
  "Massey Ferguson" : {
    "tractor" : ['MF 1500', 'MF1600 E', 'MF SERIE CLASSIC', 'MF 2600 LR', 'MF 4700', 'MF 2600 MR', 'MF 2600 E', 'MF 5700', 'MF 2600 HR', 'MF 6700', 'MF 7600', 'MF 7700 S', 'MF 8700', 'MF 8700 S', ],
    "arado" :["MF-AH03", "MF-AH04", "MF-AV200", "MF-S1", "MF-S3-5", "MF-S5-9", "MF-BR06",  ],
    "rastra" : ["MF-RT1824", "MF-RT2024", "MF-RT3224", "MF-RL1822	", "MF-RL1824", "MF-RL2024",  ],
    "pulverizadora" : ["MF9030", "MFA600", ],
    "cosechadora" : ["MF 6690", ],
  },
  "New Holland" :{
    "tractor" : ["Serie 10s", "Boomer-25", "Workmaster 40", "TT3", "Serie TT", "T3F", "LDF LP", "TS600", "6810", "Genesis T8", ],
    "pulverizadora" : ["Serie SA", ],
    "cosechadora" : ["Serie TC", "Serie FR", "Serie FP", ]
  },
  "Valtra" : {
    "tractor" : ["Serie A", "Serie F", "Serie G", "Serie N", "Serie S", "Serie T", ]
  },
  "Otra" :[]
}
arf = "RRRRR"

dic_formas = {
    "tractor": FormaTractor,
    "arado": FormaArado,
    "rastra": FormaRastra,
    "sembradora": FromaSembradora,
    "pulverizadora": FormaPulverizadora,
    "cosechadora": FromaCosechadora,

}
lista_tipos_equipo = ["Tractor", "Arado", "Rastra", "Sembradora", "Pulverizadora", "Cosechadora"]
lista_colores = ["azul", "amarillo", "rojo", "verde"]

dic_tablas = {
    "tractor": Tractor,
    "arado": Arado,
    "rastra": Rastra,
    "sembradora": Sembradora,
    "pulverizadora": Pulverizadora,
    "cosechadora": Cosechadora,
}

def get_referer(request):
    referer = request.META.get('HTTP_REFERER')
    if not referer:
        return None
    return referer


def genera_punto():
    x_punto = random.uniform(15.4134766974572, 32.590371430865)
    y_punto = random.uniform(-115.353230967552, -87.1687010217969)
    punto = [x_punto, y_punto]
    
    dentro = False
    totl = 0

    for i in range(len(poligono) - 1):
        x1 = poligono[i][0]
        x2 = poligono[i+1][0]
        y1 = poligono[i][1]
        y2 = poligono[i+1][1]


        if ((y_punto < y1) != (y_punto < y2)) and (x_punto < (x2-x1) * (y_punto-y1) / (y2-y1) + x1):
            totl += 1
            dentro = not dentro

    return [dentro, punto]




##################################################### Empiezan Vistas #################################################3
def pruebas_html(request):

    lista_nombres = ["Juan", "Santiago","Mateo","Sebastian","Leonardo","Matias","Emiliano","Diego","Miguel Ángel","Daniel","Alexander", "José Luis", "José", "María Guadalupe", "Francisco", "Guadalupe", "María",
    "Juana", "Antonio", "Jesús", "Miguel Ángel", "Pedro", "Alejandro", "Manuel", "Margarita", "María del Carmen", "Juan Carlos", "Roberto", "Fernando", "Daniel", "Carlos", "Jorge", "Ricardo", "Miguel","Eduardo",]
    lista_apellidos = ["Hernández","García","Martínez","López ","González ","Pérez","Rodríguez ","Sánchez","Ramírez","Cruz"]
    lista_usuarios = []
    lista_ub = []
    lista_puntos = []
    for i in range(1000):
        gp = genera_punto()
        while not gp[0]:
            gp = genera_punto()
        punto = gp[1]
        lista_puntos.append(punto)
    if request.method == "POST":
        
        #Creación de USER 
        for i in range(1000):
            cont = "ContraUs" + str(i)
            obj = User.objects.create_user(
            # obj = User(
                username = "usuario" + str(i+1),
                email = "correousuario" + str(i+1) + "@correos.com",
                password = cont,
            )
            obj.is_staff = False
            obj.is_superuser = False
            obj.save()

        # Creación de USUARIO
            usuario = Usuario(
                id_usuario = obj,
                nombre = random.choice(lista_nombres),
                apellido_1 = random.choice(lista_apellidos),
                apellido_2 = random.choice(lista_apellidos),
                telefono = "55-10-22-99-88",
            )
            usuario.save()
            lista_usuarios.append(usuario)

        #Creación de UBICACIÓN
        for i in range(len(lista_usuarios)):
            ltr = random.choice(letras) + random.choice(letras)
            ultimo = Ubicacion.objects.count()
            if ultimo == None:
                ultimo =  1
            else:
                ultimo += 1
            id_f = str(ultimo) + ltr
            nueva_ub = Ubicacion(
                id_ubicacion = id_f,
                id_usuario = lista_usuarios[i],
                alias = "Parcela 1",
                referencias = "Pequeña parcela en",
                coord_x = lista_puntos[i][0],
                coord_y = lista_puntos[i][1]
            )
            nueva_ub.save()
            lista_ub.append(nueva_ub)

        for i in range(len(lista_ub)):
            datos = request.POST.dict()
            lugares = datos["datos"]
            lista_coo = list(lugares.split(","))
            lista_ub[i].municipio = lista_coo[i * 2]
            lista_ub[i].estado = lista_coo[(i * 2) + 1]
            lista_ub[i].referencias = f"Pequeña parcela en {lista_ub[i].municipio}, {lista_ub[i].estado}"
            lista_ub[i].alias = f"Parcela {lista_ub[i].municipio}"
            lista_ub[i].save()

            # Creación de EQUIPO
            ulti_equipos = Equipo.objects.count()
            if ulti_equipos == None:
                ulti_equipos =  1
            else:
                ulti_equipos += 1
            id_equipos = str(ulti_equipos) +  random.choice(letras) + random.choice(letras)
            tipo = random.choice(lista_tipos_equipo).lower()
            nombre = f"{tipo} {random.choice(lista_colores)}"
            estado = random.choice(lista_estado)
            des = f"{tipo} en {estado} estado, listo para cualquier trabajo"
            marca = random.choice(listaMarcas)
            if tipo.lower() in modelos[marca]:
                el_modelo = random.choice(modelos[marca][tipo.lower()])
            else:
                el_modelo = f"Serie {random.choice(letras).upper()}"
            año_r = random.randrange(1960,2021)
            has = random.randrange(1,6)
            pre_v = random.randrange(90000, 1000000)
            pre_r = random.randrange(1000, 5000)
            nuevo_equipo = Equipo(
                num_equipo = id_equipos,
                nombre_equipo = nombre,
                id_dueño = lista_ub[i].id_usuario.id_usuario,
                tipo_equipo = tipo,
                descripcion = des,
                marca = marca,
                modelo = el_modelo,
                año = año_r,
                estado_equipo = estado,
                donde_esta = lista_ub[i],
                ubicacion_base = lista_ub[i],
                para_que = "ambos",
                hecatreas_trabajadas = has,
                precio_venta = pre_v,
                precio_renta_dia = pre_r,
                status = "activo"
            )
            nuevo_equipo.save()

            #Creacion de Equipo Especifico
            if tipo == "tractor":
                ptn = random.randrange(40,300)
                estrias = random.choice(["6", "21"])
                tracc = random.choice(["trasera", "4WD"])
                cbn = random.choice([True, False])
                el_t = Tractor(
                    id_equipo = nuevo_equipo,
                    potencia = ptn,
                    estrias_PTO = estrias,
                    enganche_tres_puntos = True,
                    cabina = cbn,
                    traccion = tracc
                )
                el_t.save()
            elif tipo == "sembradora":
                tp = random.choice(["Voleo", "Chorrillo", "Monograno"])
                no_tolv = random.choice([8,16,24,32])
                neu_m = random.choice(["neumatica", "mecanica"])
                el_t = Sembradora(
                    id_equipo = nuevo_equipo,
                    tipo = tp,
                    fertilizadora = True,
                    no_tolvas = no_tolv,
                    neumatica_mecanica = neu_m
                )
                el_t.save()
            elif tipo == "arado":
                tp = random.choice(["Cinceles", "Discos", "Subsuelo", "Vertederas"])
                no_cuer = random.choice([4,6,8,12])
                neu_m = random.choice(["neumatica", "mecanica"])
                el_t = Arado(
                    id_equipo = nuevo_equipo,
                    tipo = tp,
                    reversible = True,
                    no_cuerpos = no_cuer,
                    neumatica_mecanica = neu_m
                )
                el_t.save()
            elif tipo == "pulverizadora":
                auto = random.choice([True, False])
                t_tan = random.choice([60,80,120,200])
                n_b = random.choice([20, 40, 60])
                cap_b = random.randrange(300,1000)
                el_t = Pulverizadora(
                    id_equipo = nuevo_equipo,
                    autopropulsada = auto,
                    tamaño_tanque = t_tan,
                    no_boquillas = n_b,
                    capacidad_bomba = cap_b
                )
                el_t.save()
            elif tipo == "rastra":
                aco = random.choice(["Integral", "De Tiro"])
                tipo = random.choice(["Disco Liso", "Disco Dentado", "Discos Combinados"])
                disposicion = random.choice(["Simple", "Tandem", "Offset"])
                no_cu = random.choice([16,18,20,28,36,40])
                el_t = Rastra(
                    id_equipo = nuevo_equipo,
                    acople = aco,
                    tipo_cuerpo = tipo,
                    no_cuerpos = no_cu,
                    disposicion_cuerpos = disposicion
                )
                el_t.save()
            elif tipo == "cosechadora":
                cult = random.choice(["Maíz", "Granos Pequeños", "Caña"])
                pot = random.choice([250,300,400,500])
                capa = random.randrange(1000,2000)
                tasa_des = random.randrange(50,100)
                el_t = Cosechadora(
                    id_equipo = nuevo_equipo,
                    tipo_cultivo = cult,
                    potencia = pot,
                    capacidad_granos = capa,
                    tasa_descarga = tasa_des
                )
                el_t.save()
            
            #Creacion de Imágen
            nm_m = nombre.replace(" ","")
            urele = os.path.join("D:\imagenes_equipos", f"{nm_m}.jpg")
            img_io = io.BytesIO()
            img = Image.open(urele)
            img.save(img_io, format = "JPEG")

            n_img = InMemoryUploadedFile(img_io,"ImageField", nm_m + ".jpg", "JPEG", sys.getsizeof(img_io), None)
            la_imagen = Imagen(
                id_equipo = nuevo_equipo,
                imagen = n_img,
                es_principal = True
            )
            la_imagen.save()
        print("YA")



    return render(request, "tes2/pruebas.html", context = {"ubicacion" : lista_puntos})


def pagina_principal(request):
    user = request.user
    print(user)
    print(user.is_authenticated)
    if user.is_authenticated:
        return render(request, "tes2/index_login.html")
    return render(request, "tes2/index.html", context = {"user":user})


#Vista Para forma de creación de nuevo equipo
def creacion_equipo(request):
    user = request.user
    usuario = Usuario.objects.get(id_usuario = user)
    if user.is_anonymous:
        raise PermissionDenied
    ltr = random.choice(letras) + random.choice(letras)
    ultimo = Equipo.objects.count()
    if ultimo == None:
        ultimo =  1
    else:
        ultimo += 1
    id_f = str(ultimo) + ltr
    Ub_usr = Ubicacion.objects.filter(id_usuario = usuario).exclude(eliminado = True)
    context = {
        "ubicaciones":Ub_usr
    }
    if request.method == "POST":
        datos = request.POST.dict()
        donde = datos["donde_esta"]
        la_ub = Ub_usr.get(id_ubicacion = donde)
        del datos["csrfmiddlewaretoken"], datos["donde_esta"]
        print(datos)
        obj = Equipo(**datos, id_dueño = user, status = "activo", num_equipo = id_f, donde_esta = la_ub, ubicacion_base = la_ub)
        obj.save()
        next_url = "registro_equipo/" + str(obj.tipo_equipo) + "/" + str(id_f)
        return redirect(next_url)
    return render(request, "tes2/forma_equipo.html", context)
        


#Vista del mapa para locaización
def mapa(request):
    return render(request, "tes2/mapa_modal.html")


#Genera un Json para AJAX en busqueda de equipos
def lista_equipos(request):
    qs = Equipo.objects.all()
    print(qs)
    lista_equipo = [{
        # "dueño": x.id_dueño.,
        "nombre": x.nombre_equipo,
        "marca": x.marca,
        "modelo": x.modelo,
        # "donde": x.donde_esta,
        }
        for x in qs]
    data = {
        "response": lista_equipo
    }
    return JsonResponse(data)


# Forma para datos especificos del equipo
def forma_equipos(request, tipo_maq, id):
    form = dic_formas[tipo_maq](request.POST or None)
    if form.is_valid():
        eq = Equipo.objects.get(num_equipo = id)
        imagenes = request.FILES.getlist("images")
        print(imagenes)
        conta = 0
        for equipo in imagenes:
            print(equipo)
            if conta == 0:
                img = Imagen(id_equipo = eq, imagen = equipo, es_principal=True)
                img.save()
                conta += 1
            else:
                img = Imagen(id_equipo = eq, imagen = equipo)
                img.save()
                conta+=1
        obj = dic_tablas[tipo_maq](**form.cleaned_data, id_equipo = eq)
        obj.save()
        return redirect("mi-maq")
    return render(request,"tes2/forma_especifica.html", {"forma":form})


#Busqueda principal
def busq_principal(request):
    usr = request.user
    llaves = request.GET.dict()
    filtro = {}
    context = {}
    print(llaves)
    url = ""
    for llave in llaves:
        url += llave + "=" + llaves[llave] + "&"
    context["url"] = url
    pagina = request.GET.get("page")
    if "page" in llaves:
        del llaves["page"]
    if "fecha_1" in llaves:
        rango_años = [llaves["fecha_1"], llaves["fecha_2"]]
        del llaves["fecha_1"], llaves["fecha_2"]
        filtro["año__range"] = rango_años
    for llave in llaves:
        if llaves[llave]:
            filtro[llave] = llaves[llave]
    print(filtro)
    equipos = Equipo.objects.exclude(status = "eliminado")
    if filtro:
        equipos = equipos.filter(**filtro)
        context["filtro"] = filtro
    if usr.is_authenticated:
        equipos = equipos.exclude(id_dueño = usr)
    equipos_Pag = Paginator(equipos, 40)
    los_equipos_pag = equipos_Pag.get_page(pagina)
    lista_eq = [x.num_equipo for x in los_equipos_pag]
    imagenes= Imagen.objects.filter(id_equipo__in = lista_eq).filter(es_principal = True)
    print(lista_eq)
    print(imagenes)
    context["imagenes"] = imagenes
    context["equipos"] = los_equipos_pag
    return render(request, "tes2/lista_equipos.html", context)


#Vista de detalle de un equipo, para publico general
def vista_detalle_todos(request, num_eq):
    equipo = Equipo.objects.filter(num_equipo = num_eq).select_related("donde_esta")
    imagenes = Imagen.objects.filter(id_equipo = num_eq)
    detalle = dic_tablas[equipo[0].tipo_equipo].objects.get(id_equipo= num_eq)
    print(imagenes)
    context = {
        "equipo" : equipo[0],
        "detalle": detalle,
        "imagenes": imagenes,
    }
    return render(request, "tes2/detalles_equipo_cliente.html", context)



def pag_principlal_usuario(request): #Pagina de "control de perfil"
    usuario = request.user
    if usuario.is_anonymous:
        raise PermissionDenied
    nombre_usu = Usuario.objects.get(id_usuario = usuario)
    galactus(nombre_usu)
    context = {
        "usuario": nombre_usu
    }
    return render(request, "tes2/cuenta.html", context)


#Lista de los equipos de un usuario especifico
def lista_equipos_usuario(request):
    user = request.user
    if user.is_anonymous:
        raise PermissionDenied
    else:
        equipos = Equipo.objects.filter(id_dueño = user).exclude(status = "eliminado")
        if equipos:
            context = {
                "equipo":equipos
            }
            return render(request, "tes2/equipos_usuario.html", context)
        else:
            return render(request,"tes2/sin_equipos.html")


def registro_usuario(request):
    usr = request.user
    if usr.is_authenticated:
        return redirect("mi-cuenta")
    form = Forma_Registro_Usuario(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        obj = form.save()
        usuario_forma = form.cleaned_data["username"]
        contra = form.cleaned_data["password1"]
        usuario_autenticado = authenticate(request, username= usuario_forma, password = contra)
        login(request, usuario_autenticado)
        return redirect("datos-interesado")
    context = {
        "form" : form
    }
    return render(request, "tes2/registro.html", context)


def datos_interesado(request):
    usr = request.user
    print(usr)
    busq = Usuario.objects.filter(id_usuario = usr.id)
    if busq.exists():
        print("Ya existe!")
        return redirect("Pagina Principal")
    if usr.is_anonymous:
        return redirect("Pagina Principal")
    form = Forma_Datos_Interesado(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        print(data)
        obj = Usuario(
            id_usuario = usr,
            nombre = data["nombre"],
            apellido_1 = data["apellido_1"],
            apellido_2 = data["apellido_2"],
            telefono = data["apellido_1"],
            celular = data["celular"]
        )
        obj.save()
        return redirect("mi-cuenta")
    context = {
        "form" : form
    }
    return render(request, "tes2/datos_especificos_usuario.html", context)



def registro_ubicacion(request):
    user = request.user
    if user.is_anonymous:
        raise PermissionDenied
    ltr = random.choice(letras) + random.choice(letras)
    ultimo = Ubicacion.objects.count()
    el_usuario = Usuario.objects.get(id_usuario = user.id)
    form = Forma_Registro_Ubicacion(request.POST or None)

    if ultimo == None:
        ultimo =  1
    else:
        ultimo += 1

    id_f = str(ultimo) + ltr
    context = {
        "id": id,
        "usuario": user,
        "form": form
    }
    if request.method == "POST":
        if form.is_valid():
            datos = request.POST.dict()
            print(datos["coord_x"],",", datos["coord_y"], datos["estado"], datos["municipio"])
            obj = Ubicacion(
                id_ubicacion = id_f,
                id_usuario = el_usuario,
                alias = datos["alias"],
                coord_x = datos["coord_x"],
                coord_y = datos["coord_y"],
                referencias = datos["referencias"],
                municipio = datos["municipio"],
                estado = datos["estado"]
            )
            obj.save()
            messages.info(request, "Nueva ubicación creada")
            return redirect("ubicaciones")
    return render(request, "tes2/mapa_modal.html", context)


#Genera una transacción de tipo renta para un equipo
def renta_inicial(request, num_eq):
    equipo = Equipo.objects.select_related("donde_esta").filter(num_equipo = num_eq)
    imagen = Imagen.objects.get(id_equipo = equipo[0], es_principal = True)
    usuario = Usuario.objects.get(id_usuario = equipo[0].id_dueño)
    interesado = Usuario.objects.get(id_usuario = request.user)
    ub_interesado = Ubicacion.objects.filter(id_usuario = interesado, eliminado= False)
    context = {
        "equipo": equipo[0],
        "imagen":imagen,
        "usuario":usuario,
        "op_ub":ub_interesado,
    }
    if request.method == "POST":
        d_post = request.POST.dict()
        el_eq = equipo[0]
        fs = d_post["f-inicial"].split("/")
        fecha_inicial = f"{fs[2]}-{fs[1]}-{fs[0]}"
        ft = d_post["f-final"].split("/")
        fecha_fin = f"{ft[2]}-{ft[1]}-{ft[0]}"
        print(d_post)
        print(hoy)
        a_dnd = Ubicacion.objects.filter(alias = d_post["ubicacion"]).filter(id_usuario = interesado)
        print(a_dnd)
        sol = Solicitud(
            id_solicitante      = interesado,
            id_equipo           = el_eq,
            id_dueño_eq         = usuario,
            tipo_operacion      = "renta",
            a_donde             = a_dnd[0],
            desde_donde         = el_eq.donde_esta,
            fecha_solicitud     = hoy,
            fecha_inicio        = fecha_inicial,
            fecha_final         = fecha_fin,
            estatus             = "1"
            )
        print(sol)
        sol.save()
        
        return redirect("busqueda")
    return render(request, "tes2/renta_inicial.html", context)

#Regresa un JSON con las fechas de las transacciones de un equipo
def api_fechas(request,num_eq):
    print(hoy)
    datos = Transaccion.objects.filter(id_equipo = num_eq, tipo_transaccion = "renta", estatus__in = "3,4").filter(fecha_inicial__gte= hoy)
    lista_equipo = [{
        "inicial": x.fecha_inicial,
        "final": x.fecha_final,
        }
        for x in datos]
    data = {
        "response": lista_equipo
    }
    return JsonResponse(data)


def solicitudes_usuario(request):
    usr = request.user
    if usr.is_anonymous:
        raise PermissionDenied
    el_usu = Usuario.objects.get(id_usuario = usr)
    print(el_usu)
    soli = Solicitud.objects.filter(id_dueño_eq = el_usu).filter(estatus = "1")
    print(soli)
    if soli.count() == 0:
        soli = "na"
    context = {
        "solicitudes":   soli,
    }
    return render(request, "tes2/notificaciones.html", context)


def solicitudes_especificas(request, id_sol):
    usr = request.user
    if usr.is_anonymous:
        raise PermissionDenied
    sol = Solicitud.objects.select_related("id_solicitante").select_related("id_equipo").filter(id_solicitud = id_sol)
    la_sol = sol[0]
    print(la_sol)
    context = {
        "sol" : la_sol,
    }
    if la_sol.tipo_operacion == "venta":
        costo = la_sol.id_equipo.precio_venta
    elif la_sol.tipo_operacion == "renta":
        costo = calcula_precio(la_sol.fecha_inicio, la_sol.fecha_final, la_sol.id_equipo.precio_renta_dia)
    if request.method == "POST":
        print("postiao")
        si_no = request.POST.dict()
        if si_no["wwmd"] == "true":
            la_sol.estatus = "3"
            n_tr = Transaccion(
                    id_equipo           = la_sol.id_equipo,
                    id_dueño            = la_sol.id_dueño_eq,
                    id_arrendatario     = la_sol.id_solicitante,
                    desde_donde         = la_sol.desde_donde,
                    hacia_donde         = la_sol.a_donde,
                    estatus             = "3",
                    fecha_inicial       = la_sol.fecha_inicio,
                    importe_total       = costo,
                    tipo_transaccion    = la_sol.tipo_operacion
            )
            if la_sol.tipo_operacion == "renta":
                n_tr.fecha_final = la_sol.fecha_final
            n_tr.save()
            crea_conversa(n_tr)
            #Avisar al Solicitante +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        elif si_no["wwmd"] == "false":
            print("negao")
            la_sol.estatus = "4"
            print(sol[0].estatus)
            #Avisar al Solicitante +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        print("acabao")
        la_sol.save()
        print (sol[0].estatus)
        return redirect("noti")
    return render(request, "tes2/notif_especifica.html", context)

def crea_conversa(tr):
    n_co = Conversacion(
        fecha_creacion  = hoy,
        id_transaccion  = tr,
        usuario_1       = tr.id_dueño,
        usuario_2       = tr.id_arrendatario,
    )
    n_co.save()
    texto_msj = f"Esta es una conversación entre el dueño del '{tr.id_equipo.tipo_equipo} {tr.id_equipo.marca} {tr.id_equipo.modelo}' y el arrendador"
    usu = User.objects.get(username = "cesar")
    m_msj = Mensaje(
        contenido = texto_msj,
        remitente = usu,
        id_conversacion = n_co
    )    
    m_msj.save()


def calcula_precio(f1,f2, cash):
    dias = (f2 - f1)
    print(dias)
    dia_c = math.trunc(dias.days) +1
    print(dia_c)
    precio = dia_c * cash
    return precio


def lista_transacciones_usuario(request):
    usr = request.user
    el_usu = Usuario.objects.get(id_usuario = usr)
    if usr.is_anonymous:
        raise PermissionDenied
    tr_mis_equipos_activos = Transaccion.objects.filter(estatus__in = "3,1").filter(id_dueño = el_usu).filter(fecha_final__gte = hoy).filter(tipo_transaccion = "renta")
    tr_yo_rento_activos = Transaccion.objects.filter(estatus__in = "3,1").filter(id_arrendatario = el_usu).filter(fecha_final__gte = hoy).filter(tipo_transaccion = "renta")
    context = {
        "tr_mias" : tr_mis_equipos_activos,
        "tr_renta": tr_yo_rento_activos,
    }
    if tr_mis_equipos_activos.count() == 0:
        context["tr_mias"] = "nh"
    if tr_yo_rento_activos.count() == 0:
        context["tr_renta"] = "nh"
    return render(request, "tes2/transacciones_usuario.html", context)


def ubicaciones_usuario(request):
    usr = request.user
    if usr.is_anonymous:
        raise PermissionDenied
    usua = Usuario.objects.get(id_usuario = usr)
    las_ubi = Ubicacion.objects.filter(id_usuario = usua, eliminado = False)
    if las_ubi.count() == 0:
        las_ubi = "na"
    context = {
        "ubicacion":las_ubi,
    }
    return render(request, "tes2/ubicaciones_usuario.html", context)

def ubicacion_especifica(request, id_ub):
    usr = request.user
    if usr.is_anonymous:
        raise PermissionDenied
    ubic = Ubicacion.objects.get(id_ubicacion = id_ub)
    if ubic.eliminado == True:
        raise PermissionDenied
    form = Forma_Edicion_Ubicacion(initial={'alias': ubic.alias, 'referencias':ubic.referencias })
    if request.method == "POST":
        dts = request.POST.dict()
        del dts['csrfmiddlewaretoken']
        print(dts)
        for key, value in dts.items():
            setattr(ubic, key, value)
        ubic.save()
        messages.success(request, 'Ubicación editada')
        return redirect(f"/mi_cuenta/ubicaciones/{id_ub}")
    context = {
        "form" : form,
        "ubicacion" : ubic
    }
    return render(request, "tes2/ubicacion_especifica.html", context)

####################################### Eliminaciones ######################################

def elimina_ubicacion(request, id_ub):
    usr = request.user
    if usr.is_anonymous:
        raise PermissionDenied
    usuario = Usuario.objects.get(id_usuario = usr)
    las_ubicaciones = Ubicacion.objects.filter(id_usuario = usuario, eliminado = False)
    los_equipos = Equipo.objects.filter(id_dueño = usr).exclude(status = "eliminado")
    ubic = Ubicacion.objects.get(id_ubicacion = id_ub)
    eq = Equipo.objects.filter(donde_esta = ubic).exclude(status = "eliminado")

    if len(las_ubicaciones) == 1 and len(los_equipos) > 0:
        messages.info(request, "No se puede eliminar esta ubicación ya que tiene equipos asignados a esta ubicación y no cuenta con otra.")
        return redirect("ubicaciones")

    if len(eq)> 0:
        messages.info(request, "Tiene equipos asignados a esta ubicación, se deben cambiar antes de eliminar la ubicación. ")
        return redirect(f"/mi_cuenta/ubicaciones/{id_ub}/eliminar/equipos")
    else:
        ubic.eliminado = True
        ubic.save()
        messages.info(request, "Ubicación eliminada correctamente")
        return redirect("ubicaciones")


#vista para cambiar los equipos de ubicación al intentar eliminar una ubicación con equipos asignados.
def elim_equipos_ub(request, id_ub):
    usr = request.user
    if usr.is_anonymous:
        raise PermissionDenied
    usuario = Usuario.objects.get(id_usuario = usr)
    ubic = Ubicacion.objects.get(id_ubicacion = id_ub)
    ubic_todas = Ubicacion.objects.exclude(id_ubicacion = id_ub).filter(eliminado = False, id_usuario = usuario)
    eq = Equipo.objects.filter(donde_esta = ubic).exclude(status = "eliminado")
    context = {
        "ubicacion": ubic,
        "opciones": ubic_todas,
        "equipos" : eq,
    }
    if request.method == "POST":
        data = request.POST.dict()
        del data['csrfmiddlewaretoken']
        equipos = []
        for key, value in data.items():
            eq =(key.split("-")[1], value)
            equipos.append((key.split("-")[1], value))

        for eq in equipos:
            ub = Ubicacion.objects.get(alias = eq[1], id_usuario = usuario)
            el_equipo = Equipo.objects.get(num_equipo = eq[0])
            el_equipo.donde_esta = ub
            el_equipo.save()
        ubic.eliminado = True
        ubic.save()
        messages.info(request, "Ubicación eliminada correctamente")
        return redirect("ubicaciones")
    return render(request, "tes2/eq_ubicacion.html", context)


def elimina_eqipo(request, id_eq):
    usr = request.user
    if usr.is_anonymous:
        raise PermissionDenied
    equipo = Equipo.objects.get(num_equipo = id_eq)
    trn = Transaccion.objects.filter(id_equipo = id_eq, estatus = 3)
    if len(trn) > 0:
        messages.info(request, "El equipo tiene transacciones en curso y/o agendadas. No puede ser eliminado")
        return redirect("mi-maq")
    else:
        equipo.status = "eliminado"
        equipo.save()
        messages.info(request, "Equipo eliminado.")
        return redirect("mi-maq")

def cancela_transaccion(request, id_tr):
    usr = request.user
    if usr.is_anonymous:
        raise PermissionDenied
    transa = Transaccion.objects.get(id_transaccion = id_tr)
    transa.estatus = 2
    transa.save()
    #Generar notificacion para el usuario afectado y modificar equipo
    print(transa.estatus)
    return redirect("mis-contratos")

###################################### Termina Eliminaciones ############################

#Vista de detalle de un equipo para el dueño
def vista_eq_usuario(request, id_eq):
    usr = request.user
    if usr.is_anonymous:
        raise PermissionDenied
    el_eq = Equipo.objects.filter(num_equipo = id_eq).select_related("donde_esta")
    detalle = dic_tablas[el_eq[0].tipo_equipo].objects.get(id_equipo= id_eq)
    tabla_detalle = dic_formas[el_eq[0].tipo_equipo]
    imagenes = Imagen.objects.filter(id_equipo = id_eq)
    if usr != el_eq[0].id_dueño:
        raise PermissionDenied
    context = {
        "equipo":el_eq[0],
        "img": imagenes,
        "det": detalle,
        "forma": tabla_detalle,
    }
    return render(request, "tes2/detalles_equipo_dueño.html", context)


def vista_individual_transaccion(request, id_tr):
    usr = request.user
    if usr.is_anonymous:
        raise PermissionDenied
    usuar = Usuario.objects.get(id_usuario = usr)
    la_tr = Transaccion.objects.filter(id_transaccion = id_tr).select_related("id_dueño").select_related("id_arrendatario")
    if usuar != la_tr[0].id_dueño and usuar != la_tr[0].id_arrendatario:
        raise PermissionDenied
    context = {
        "trn" : la_tr[0],
    }
    if usuar == la_tr[0].id_dueño:
        context["quien"] = "dueño"
    elif usuar == la_tr[0].id_arrendatario:
        context["quien"] =  "arren"
    return render(request, "tes2/transaccion_especifica.html", context)


def galactus(el_usuario):
    trr = Transaccion.objects.filter(Q(id_dueño = el_usuario) | Q(id_arrendatario = el_usuario))
    #Combinar celery para automatizar (async)
    print(trr)


def mensajes(request):
    usr = request.user
    if usr.is_anonymous:
        raise PermissionDenied
    el_usuario = Usuario.objects.get(id_usuario = usr)
    conversaciones = Conversacion.objects.select_related("id_transaccion").select_related("usuario_1").select_related("usuario_2").filter((Q(usuario_1 = el_usuario) | Q(usuario_2 = el_usuario)))
    print(usr.id)
    if len(conversaciones) == 0:
        print(len(conversaciones))
        conversaciones = "na"
    context = {
        "conver" : conversaciones,
        "id_us" : usr.id,
    }
    return render(request, "tes2/conversaciones.html", context)

def consigue_mensajes(request, id_conv):
    usr = request.user
    mensajes = Mensaje.objects.filter(id_conversacion = id_conv).select_related("remitente").select_related("id_conversacion")
    lms = [{
        "cont"              : x.contenido,
        "remitente"         : x.remitente.id,
        "id_conversacion"   : x.id_conversacion.id_conversacion,
        "id"                : x.id_mensaje}
        for x in mensajes]
    data = {
        "response" : lms
    }
    if request.method == "POST":
        datos = request.POST.dict()
        print(datos)
    return JsonResponse(data)


def nuevo_msj(request, id_conv):
    usr = request.user
    if request.method == "POST":
        conv = Conversacion.objects.get(id_conversacion = id_conv)
        post_data = json.loads(request.body.decode("utf-8"))
        print(post_data)
        cuerpo = post_data.get("msg")
        nuevo_mensaje = Mensaje(
            contenido           = cuerpo,
            remitente           = usr,
            id_conversacion     = conv
        )
        nuevo_mensaje.save()
    data = {"reponse" : {}}
    return JsonResponse(data)
