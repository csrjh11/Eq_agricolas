"use strict"

//Fechas iniciales para claendario
const fecha1 = new Date
const hoy = new Date
const fecha2 = new Date

// opciones para impresión de fecha completa en calendario
const optn = {weekday: 'long', year: 'numeric', month: 'long', day: 'numeric'}
const diaInt = hoy.getDate()

//Objetos a manipular en Documento
const elEquipo = document.getElementById("eq").value;
const elCalendario1 = document.querySelector(".cl-1");
const fInicio = document.querySelector("#inicio");
const precio = document.querySelector("#precio");
const precioFloat = precio.innerHTML.split(" ")[1];
const elCalendario2 = document.querySelector(".cl-2");
const fFinal = document.querySelector("#final");

// Arrays iniciales para API de fechas-transacciones
let arrFechasTr = [];
let arrDes = [];
let arrFinal =  [];


//Controladores de inputs inicio y fin
fInicio.addEventListener("click", function(){
    elCalendario1.classList.toggle("hidden");
})

fFinal.addEventListener("click", function(){
    elCalendario2.classList.toggle("hidden");
})

//Función para obtener los datos de API
const getDatos = function(){
    return new Promise((resolve)=> {
        const dat = fetch(`/fechas_renta/${elEquipo}`).then( val => val.json())
        resolve(dat)
    })
}

//Arma el array de fechas
const armaArrTr = function(dato){
    for(const dt in dato){
        const separados = dato[dt].split("-");
        const fecha = new Date(separados[0], `${separados[1] - 1}`, separados[2]);
        arrDes.push(fecha);
    }
}

//Func para revisar si arr contiene fecha
const comparaFechas = function(arrFe, fe){
    const arrStr = arrFe.map(a => a.toDateString());
    const fechaSt= fe.toDateString()
    return arrStr.includes(fechaSt)
}

//Función de creación de calendario
const rendCalendar = async function(num, date){

    const month = date.getMonth()
    const dia = date.getDay()
    const año = date.getFullYear()
    

    const arrDias = ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
    const arrMeses = [
        "Enero",
        "Febrero",
        "Marzo",
        "Abril",
        "Mayo",
        "Junio",
        "Julio",
        "Agosto",
        "Septiembre",
        "Octubre",
        "Noviembre",
        "Diciembre",
    ]

    const ultimoDia = new Date(date.getFullYear(), date.getMonth() + 1, 0).getDate();
    const indexUltimoDia = new Date(date.getFullYear(), date.getMonth() + 1, 0).getDay();
    const sigDias = 7 - indexUltimoDia - 1;
    let ultimoDiaAnterior = new Date(date.getFullYear(), date.getMonth(), 0).getDate();

    const fechaArmada = hoy.toLocaleDateString("es-MX", optn).toUpperCase();

    date.setDate(1);
    const primerDia = date.getDay();

    const dispMonth = document.querySelector(`.date-${num} h1`)
    dispMonth.innerHTML = `${arrMeses[month]} ${año}`

    const dispFecha = document.querySelector(`.date-${num} p`)
    dispFecha.innerHTML = fechaArmada

    let losDias = "";

    for(let x = primerDia; x>0; x--){
        losDias += `<div class = "prev-date">${ultimoDiaAnterior - x + 1}</div>`    
    }

    const dts = await getDatos();
    const resp = dts.response;
    resp.forEach(tr => {
        armaArrTr(tr);
        arrFechasTr.push(arrDes);
        arrDes = [];
    })
    arrFechasTr.forEach(d => {
        const dias = Math.abs((d[1] - d[0])/1000/60/60/24)
        const elDia = d[1].getDate();
        const elMes = d[1].getMonth();
        const elAño = d[1].getFullYear();
        arrFinal.push(d[0])
        for(let i = 1;dias > i;i++){
            const nFecha = new Date(elAño, elMes, elDia - i )
            arrFinal.push(nFecha);
        }        
        arrFinal.push(d[1]);
    })
    
    for(let i = 1; i <= ultimoDia; i++){
        const fProv = new Date
        fProv.setMonth(month)
        fProv.setDate(i)
        fProv.setHours(0,0,0)

        if(comparaFechas(arrFinal, fProv)){
            if(i< diaInt && month <= hoy.getMonth() && año === hoy.getFullYear()){
                losDias += `<div class = "dn-${num}-ocupado">${i}</div>`;
            }else if(month < hoy.getMonth() && año <= hoy.getFullYear()){
                losDias += `<div class = "dn-${num}-ocupado">${i}</div>`;
            }else if(i === diaInt && month === hoy.getMonth() && año === hoy.getFullYear()){
                losDias += `<div class = "today-${num}-ocupado">${i}</div>`;
            }else if(año >= hoy.getFullYear()){
                losDias += `<div class = "dn-${num}-ocupado">${i}</div>`;}
        }else{
            if(i< diaInt && month <= hoy.getMonth() && año === hoy.getFullYear()){
                losDias += `<div class = "dn-${num}-ocupado">${i}</div>`;
            }else if(month < hoy.getMonth() && año <= hoy.getFullYear()){
                losDias += `<div class = "dn-${num}-ocupado">${i}</div>`;
            }else if(i === diaInt && month === hoy.getMonth() && año === hoy.getFullYear()){
                losDias += `<div class = "today-${num}">${i}</div>`;
            }else losDias += `<div class = "dn-${num}">${i}</div>`;
        }
    }

    for(let j = 1; j <= sigDias ; j++){
        losDias += `<div class="next-date">${j}</div>`;
    }

    const dispDias = document.querySelector(`.days-${num}`)
    dispDias.innerHTML = losDias;
    
    const diass1 = document.querySelectorAll(".dn-1, .today-1");

    diass1.forEach(di => di.addEventListener("click", function(){
        fInicio.value = `${this.innerHTML}/${month + 1}/${año}`;
        elCalendario1.classList.add("hidden");
        fFinal.disabled  = false;
        rendCalendar(2, fecha2);
    }))

    const diass2 = document.querySelectorAll(".dn-2, .today-2");

    diass2.forEach(di => di.addEventListener("click", function(){
        fFinal.value = `${this.innerHTML}/${month + 1}/${año}`;
        elCalendario2.classList.add("hidden");
    }))

    if(num === 2){
        const valFI = fInicio.value;
        const fechaArr = valFI.split("/");
        const fechaII = new Date(fechaArr[2], fechaArr[1] - 1, fechaArr[0]);
        const arrSo = arrFinal.sort((a,b)=> a-b)
        arrSo.push(fechaII);
        const aConT = arrSo.sort((a,b)=> a-b);
        const elI = aConT.indexOf(fechaII);

        if(elI === aConT.length - 1){
            return
        }else{
            const fechaCort = aConT[elI + 1];
            const elNum = fechaCort.getDate();
            const paraCambiar = document.querySelectorAll(".dn-2");
            const arrLosValores = []
            paraCambiar.forEach(div =>{
                if(div.innerHTML > elNum){
                    div.classList.remove("dn-2")
                    div.classList.add("dn-2-ocupado")
                }else if (div.innerHTML <= fechaArr[0] && month > fechaII.getMonth() && año >= fechaII.getFullYear()){
                    div.classList.remove("dn-2")
                    div.classList.add("dn-2-ocupado")
                }else if (div.innerHTML > fechaArr[0] && div.innerHTML <= elNum && month > fechaII.getMonth() && año >= fechaII.getFullYear()){
                    div.classList.remove("dn-2")
                    div.classList.add("dn-2-ocupado")
                }else if(month <= fechaII.getMonth() && año > fechaII.getFullYear()){
                    div.classList.remove("dn-2")
                    div.classList.add("dn-2-ocupado")
                }
            })
        }     
    }
    arrFechasTr = [];
    arrDes = [];
    arrFinal =  [];
}

//Evento para cambio de meses(Control de los iconos de flecha)
document.querySelector(".prev-1").addEventListener("click", function(){
    fecha1.setMonth(fecha1.getMonth() -1);
    rendCalendar(1, fecha1)
})

document.querySelector(".next-1").addEventListener("click", function(){
    fecha1.setMonth(fecha1.getMonth() + 1);
    rendCalendar(1, fecha1)
})

document.querySelector(".prev-2").addEventListener("click", function(){
    fecha2.setMonth(fecha2.getMonth() -1);
    rendCalendar(2, fecha2)
})

document.querySelector(".next-2").addEventListener("click", function(){
    fecha2.setMonth(fecha2.getMonth() + 1);
    rendCalendar(2, fecha2)
})


rendCalendar(1, fecha1);


/////////////////////////Comienza validación de datos y formas ///////////////////////////////////////

const forUb = document.getElementById("forma-ub");
const forFechas= document.getElementById("forma-fechas");
const ubic = document.getElementById("op-ub");
const ubicOculto = document.getElementById("lugar");

const convFecha = function(fecha){
    if (fecha){
        const arFe = fecha.split("/")
        const nueFe = new Date
        nueFe.setDate(arFe[0])
        nueFe.setMonth(arFe[1] - 1)
        nueFe.setFullYear(arFe[2])
        return nueFe
    }else return ""
}

const botNext = document.querySelector(".bot-go")
botNext.addEventListener("click", function(){

    const fechaInicio = convFecha(fInicio.value);
    const fechaFin = convFecha(fFinal.value);
    const diasRenta = Math.trunc(((fechaFin - fechaInicio)/ 1000/60/60/24) + 1);
    const precioTotal = parseFloat(precioFloat) * diasRenta;

    if(!fechaInicio && !fechaFin){ 
        alert("Seleccione fecha de inicio y final.")
        return
    } else if (!fechaInicio) {
        alert("Seleccione fecha de Inicio")
        return
    } else if (!fechaFin) {
        alert("Seleccione fecha final")
        return
    }

    if (fechaInicio < hoy){
        alert("Seleccione una fecha de inicio válida")
        return
    }else if  (fechaInicio > fechaFin || diasRenta < 0) {
        alert("seleccione una fecha final diferente")
        return
    }

    if (!ubic.value){
        alert("Seleccione una ubicación");
        return
    }

    document.querySelector(".detalles").classList.remove("hidden");
    document.getElementById("tabla-d").innerHTML += `<tr><td>Precio x ${diasRenta} dia(s) = </td> <td class="right"><strong> $ ${precioTotal} </strong></td> </tr>`
    document.getElementById("precio-total").value = precioTotal
    document.querySelector(".boton").classList.add("hidden");
    document.querySelector(".btn-dos").classList.remove("hidden")
    


})

// Obtención y muestra de datos de distancia entre ubicaciones

ubic.addEventListener("change", async function(){
    const llAPI = "AIzaSyA6BgqA2oKejfHVnFodwFPmIDJZDIH6YeE"
    const coordsEq = document.getElementById("coords-eq").value;
    const coordsInt = document.getElementById(`${ubic.value}-crd`).value;
    ubicOculto.value =  ubic.value


    // const laPrueba = await fetch(`https://maps.googleapis.com/maps/api/directions/json?origin=${coordsEq}&destination=${coordsInt}&key=${llAPI}`)
    // console.log(laPrueba)

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

    forUb.submit()
    forFechas.submit()

})

 