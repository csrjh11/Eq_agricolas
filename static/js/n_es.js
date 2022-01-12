"use strict"

const btnAceptar = document.querySelector(".b-acp");
const btnALV = document.querySelector(".b-rec");
const elValor = document.getElementById("wwmd");
const fAceptar = document.getElementById("forma-SN");


btnAceptar.addEventListener("click", function(){
    elValor.value = true;
    alert("Transacción aceptada, a continuación se muestran los datos de contacto del interesado");
    fAceptar.submit();
});

btnALV.addEventListener("click", function(){
    elValor.value = false;
    alert("Transacción no aceptada, se notificara al interesado. Gracias");
    fAceptar.submit();
})