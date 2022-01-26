"use strict"

//Componentes modal vista equipo
const btnEquipo = document.getElementById("btnEquipo");
const btnCerrarEquipo = document.getElementById("btn-cerrar-equipo");
const modalEquipo = document.getElementById("modal-equipo");


//Elementos de  Fechas
const fechaInicialModal = document.getElementById("fecha-incial-m");
const fechaFinalModal = document.getElementById("fecha-final-m");
const modalFechas = document.getElementById("modal-cambio-fechas");
const btnFechas = document.getElementById("btn-fechas");
const btnCierraFechas = document.getElementById("btn-c-fechas");
const displayFechaIncial = document.getElementById("fecha-i-display");
const displayFechaFinal = document.getElementById("fecha-f-display");
const inputFechaInicial = document.getElementById("in-fecha-i");
const inputFechaFinal = document.getElementById("in-fecha-f");


//Elementos modal Costo
const btnCosto = document.getElementById("btn-costo");
const modalCosto = document.getElementById("modal-cambio-costo");
const btnCierraCosto = document.getElementById("btn-c-costo");
const inputModalCosto = document.getElementById("costo-modal");
const costoForma = document.getElementById("in-costo");
const costoDisplay = document.getElementById("costo-display")



//Controladores modal Vista Equipo

btnEquipo.addEventListener("click", function(){
    modalEquipo.classList.remove("hidden");
})

btnCerrarEquipo.addEventListener("click", function(){
    modalEquipo.classList.add("hidden")
})


//Controladores modal Fechas

btnFechas.addEventListener("click", function(){
    modalFechas.classList.remove("hidden");
})

btnCierraFechas.addEventListener("click", function(){
    if(fechaInicialModal.value && fechaFinalModal.value ){
        if(fechaInicialModal.value > fechaFinalModal.value){
            alert("Seleccionar Fecha Final mayor a Fecha Inicial")
            fechaFinalModal.value = ""
        }else{
            console.log(fechaInicialModal.value, fechaFinalModal.value)
            const valInicial = armaFechas(fechaInicialModal.value)
            const valFinal = armaFechas(fechaFinalModal.value)
            console.log(valInicial, valFinal)
            displayFechaIncial.innerText = valInicial
            displayFechaFinal.innerText = valFinal
            inputFechaInicial.value = valInicial
            inputFechaFinal.value = valFinal
            modalFechas.classList.add("hidden")
        }
    }
})

const armaFechas = function(fecha){
    const arrF = fecha.split("-")
    let armado = `${arrF[2]}/${arrF[1]}/${arrF[0]}`
    return armado
}


// Controlador de Costos
btnCosto.addEventListener("click", function(){
    modalCosto.classList.remove("hidden");
})



btnCierraCosto.addEventListener("click", function(){
    if(inputModalCosto.value){
        costoDisplay.innerText = `$ ${inputModalCosto.value}`
        costoForma.value = inputModalCosto.value
        modalCosto.classList.add("hidden")
    }else{
        alert("Introduzca un nuevo Costo")
    }

})




//Control tecla Escape
document.addEventListener("keydown", function(e){
    if(e.key === "Escape"){
        modalEquipo.classList.add("hidden")
        modalFechas.classList.add("hidden")
        modalCosto.classList.add("hidden")
    }
})

//Control envío Formula

const btnGo = document.getElementById("btn-go");
const forma = document.getElementById("forma-sol");

btnGo.addEventListener("click", function(){
    forma.submit()
})