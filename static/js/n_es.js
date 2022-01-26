"use strict"

const btnAceptar = document.querySelector(".b-acp");
const btnALV = document.querySelector(".b-rec");
const elValor = document.getElementById("wwmd");
const fAceptar = document.getElementById("forma-SN");
const btnModalEquipo = document.getElementById("ver-equipo");
const btnCerrarEquipo = document.getElementById("btn-cerrar-equipo");
const modalEquipo = document.getElementById("modal-equipo");

btnAceptar.addEventListener("click", function(){
    elValor.value = true;
    alert("Transacción aceptada, a continuación se muestran los datos de contacto del interesado");
    fAceptar.submit();
});

btnALV.addEventListener("click", function(){
    elValor.value = false;
    alert("Transacción rechazada, se notificara al interesado. Gracias");
    fAceptar.submit();
})

//Control Botones Modal Equipo
btnModalEquipo.addEventListener("click", function(){
    modalEquipo.classList.remove("hidden")
})

btnCerrarEquipo.addEventListener("click", function(){
    modalEquipo.classList.add("hidden")
})


//Control tecla Escape
document.addEventListener("keydown", function(e){
    if(e.key === "Escape"){
        modalEquipo.classList.add("hidden")
    }
})