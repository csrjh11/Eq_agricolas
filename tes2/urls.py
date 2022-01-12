from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [
    path("", views.pagina_principal, name = "Pagina Principal"),
    path("pruebas", views.pruebas_html, name = "pruebas"),
    path("login", LoginView.as_view(template_name = "tes2/login.html", redirect_authenticated_user=True), name = "login" ),
    path("logout", LogoutView.as_view(template_name = "tes2/logout.html"), name  = "logout"),
    path("registro_equipo", views.creacion_equipo, name = "Registro de Equipo"),
    path("mapa",views.mapa ),
    path("equipos", views.lista_equipos),
    path("browse/<num_eq>", views.vista_detalle_todos),
    path("registro_equipo/<str:tipo_maq>/<str:id>", views.forma_equipos),
    path("browse",views.busq_principal, name= "busqueda"),
    path("mi_cuenta", views.pag_principlal_usuario, name = "mi-cuenta"),
    path("mi_cuenta/mis_equipos", views.lista_equipos_usuario, name = "mi-maq"),
    path("mi_cuenta/mis_contratos", views.lista_transacciones_usuario, name = "mis-contratos"),
    path("registro", views.registro_usuario, name = "reg_usuario"),
    path("registro_ubicacion", views.registro_ubicacion, name = "reg_ubicacion"),
    path("registro/datos_int", views.datos_interesado, name ="datos-interesado"),
    path("renta/<num_eq>", views.renta_inicial, name = "renta"),
    path("fechas_renta/<num_eq>",views.api_fechas, name = "API-fechas"),
    path("mis_solicitudes",views.solicitudes_usuario, name = "noti"),
    path("mis_solicitudes/<id_sol>",views.solicitudes_especificas, name = "noti-esp"),
    path("mi_cuenta/ubicaciones",views.ubicaciones_usuario, name = "ubicaciones"),
    path("mi_cuenta/ubicaciones/<id_ub>",views.ubicacion_especifica, name = "ub-esp"),
    path("mi_cuenta/ubicaciones/<id_ub>/eliminar", views.elimina_ubicacion, name ="e-ub"),
    path("mi_cuenta/ubicaciones/<id_ub>/eliminar/equipos", views.elim_equipos_ub, name = "e-ub-eq"),
    path("mi_cuenta/equipos/<id_eq>/eliminar", views.elimina_eqipo, name = "el-eq"),
    path("mi_cuenta/equipos/<id_eq>", views.vista_eq_usuario),
    path("mi_cuenta/mis_tr/<id_tr>", views.vista_individual_transaccion),
    path("mi_cuenta/mis_tr/<id_tr>/cancelar", views.cancela_transaccion),
    path("mi_cuenta/mis_mensajes", views.mensajes, name = "mensajes"),
    path("mensajes/<id_conv>", views.consigue_mensajes),
    path("conv/<id_conv>", views.nuevo_msj),
]
