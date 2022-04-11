"use strict"

//Objetos a manipular en Documento
const elEquipo = document.getElementById("eq").value;
const elCalendario1 = document.querySelector(".cl-1");
const fInicio = document.querySelector("#inicio");
const precio = document.querySelector("#precio");
const precioFloat = precio.innerHTML.split(" ")[1];
const elCalendario2 = document.querySelector(".cl-2");
const fFinal = document.querySelector("#final");




/////////////////////////Comienza validación de datos y formas ///////////////////////////////////////

const forUb = document.getElementById("forma-ub");
const forFechas= document.getElementById("forma-fechas");
const ubic = document.getElementById("op-ub");
const ubicOculto = document.getElementById("lugar");


// Obtención y muestra de datos de distancia entre ubicaciones

ubic.addEventListener("change", async function(){
    const llAPI = "AIzaSyA6BgqA2oKejfHVnFodwFPmIDJZDIH6YeE"
    const coordsEq = document.getElementById("coords-eq").value;
    const coordsInt = document.getElementById(`${ubic.value}-crd`).value;
    ubicOculto.value =  ubic.value

    let directionsService = new google.maps.DirectionsService();

    let request = {
        origin      : coordsEq,
        destination : coordsInt,
        travelMode  : google.maps.DirectionsTravelMode.DRIVING,
        unitSystem  : google.maps.UnitSystem.METRIC
    };

    directionsService.route(request, function(response, status) {
        if ( status == google.maps.DirectionsStatus.OK ) {
            const distancia = response.routes[0].legs[0].distance.text
            const tiempo = response.routes[0].legs[0].duration.text
            const tiempoCalc = response.routes[0].legs[0].duration
            const elHTML = `<tr><td>Distancia estimada(km) = </td> <td class="right"><strong> ${distancia} </strong></td> </tr>
            <tr><td>Tiempo estimado de transporte  = </td> <td class="right"><strong> ${tiempo} </strong></td> </tr>`
            if((tiempo *2)/60/60 > 9) document.getElementById("tabla-d").innerHTML += "<h2>El timepo estimado de transporte ida y vuelta excede las 9 horas, se recomienda considerar un dia extra de renta para el traslado del equipo</h2>"
            document.querySelector("#tabla-ub").innerHTML = elHTML
            document.querySelector(".detalles-ub").classList.remove("hidden")

        }
        else {
          // Hay problema con las ubicaciones
        }
    });
}) 

//Control de botón de Submit

const botSub = document.querySelector(".bot-sub")


botSub.addEventListener("click", function(){
    
    if (!ubic.value){
        alert("Seleccione una ubicación");
        return
    }
    forUb.submit()
    forFechas.submit()

})

 