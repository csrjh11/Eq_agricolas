"use strict"

const fecha1 = new Date
const hoy = new Date
const fecha2 = new Date

const elEquipo = document.getElementById("eq").value;
const elCalendario1 = document.querySelector(".cl-1");
const fInicio = document.querySelector("#inicio");
const precio = document.querySelector("#precio");
const precioFloat = precio.innerHTML.split(" ")[1];
const elCalendario2 = document.querySelector(".cl-2");
const fFinal = document.querySelector("#final");

fInicio.addEventListener("click", function(){
    elCalendario1.classList.toggle("hidden");
})

fFinal.addEventListener("click", function(){
    elCalendario2.classList.toggle("hidden");
})


const rendCalendar = function(num, date){
    
    const month = date.getMonth()
    const dia = date.getDay()
    const año = date.getFullYear()
    const diaInt = date.getDate()
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

    const fechaArmada = `${arrDias[dia]} ${diaInt} de ${arrMeses[month]}, ${año}`;

    date.setDate(1);
    const primerDia = date.getDay();


    const dispMonth = document.querySelector(`.date-${num} h1`)
    dispMonth.innerHTML = arrMeses[month]


    const dispFecha = document.querySelector(`.date-${num} p`)
    dispFecha.innerHTML = fechaArmada


    let losDias = "";

    for(let x = primerDia; x>0; x--){
        losDias += `<div class = "prev-date">${ultimoDiaAnterior - x + 1}</div>`    
    }

    for(let i = 1; i <= ultimoDia; i++){
        if(i === diaInt && month === new Date().getMonth()){
            losDias += `<div class = "today">${i}</div>`;
        }else losDias += `<div class = dn-${num}>${i}</div>`;
    }

    for(let j = 1; j <= sigDias ; j++){
        losDias += `<div class="next-date">${j}</div>`;
    }

    const dispDias = document.querySelector(`.days-${num}`)
    dispDias.innerHTML = losDias;

    const diass1 = document.querySelectorAll(".dn-1, .today")

    diass1.forEach(di => di.addEventListener("click", function(){
        fInicio.value = `${this.innerHTML}/${month + 1}/${año}`;
        elCalendario1.classList.add("hidden");
        fFinal.disabled  = false;
    }))

    const diass2 = document.querySelectorAll(".dn-2, .today")

    diass2.forEach(di => di.addEventListener("click", function(){
        fFinal.value = `${this.innerHTML}/${month + 1}/${año}`;
        elCalendario2.classList.add("hidden");
    }))

}

document.querySelector(".prev-1").addEventListener("click", function(){
    fecha1.setMonth(fecha1.getMonth() -1);
    rendCalendar(1, fecha1)
})

document.querySelector(".next-1").addEventListener("click", function(){
    fecha1.setMonth(fecha1.getMonth() + 1);
    rendCalendar(1, fecha1)
})

document.querySelector(".prev-2").addEventListener("click", function(){
    fecha1.setMonth(fecha1.getMonth() -1);
    rendCalendar(2, fecha1)
})

document.querySelector(".next-2").addEventListener("click", function(){
    fecha1.setMonth(fecha1.getMonth() + 1);
    rendCalendar(2, fecha1)
})

rendCalendar(1,fecha1);
rendCalendar(2,fecha2);

const forUb = document.getElementById("forma-ub");
const forFechas= document.getElementById("forma-fechas");
const ubic = document.getElementById("op-ub");

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
    const diasRenta = (fechaFin - fechaInicio)/ 1000/60/60/24;
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
    datosTr(fechaInicio);

    if (!ubic.value){
        alert("Seleccione una ubicación");
        return
    }

    document.getElementById("tabla-d").innerHTML = `<tr><td>Precio x ${diasRenta} dia(s) = </td> <td class="right"> $ ${precioTotal} </td> </tr>`

    // forUb.submit()
    // forFechas.submit()
})

let arrFechasTr = [];
let arrDes = [];
let arrFinal =  [];

const armaArrTr = function(dato){
    for(const dt in dato){
        const separados = dato[dt].split("-");
        const fecha = new Date(separados[0], `${separados[1] - 1}`, separados[2]);
        arrDes.push(fecha);
    }
}

const getDatos = function(){
    return new Promise((resolve)=> {
        const dat = fetch(`/fechas_renta/${elEquipo}`).then( val => val.json())
        resolve(dat)
    })
}

const datosTr = async function(fechaI, fechaF){
    const dat = await getDatos();
    const responseTr = dat.response;
    responseTr.forEach(tr => {
        armaArrTr(tr);
        arrFechasTr.push(arrDes);
        arrDes = [];
    });
    console.log(arrFechasTr)
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
        arrFinal.push(d[1])
    })
    fechaI.setHours(0,0,0);
    fechaF.setHours(0,0,0);

    if(arrFinal.includes(fechaI)) alert("El equipo seleccionado no esta disponible en las fechas seleccionadas")   
    
}

