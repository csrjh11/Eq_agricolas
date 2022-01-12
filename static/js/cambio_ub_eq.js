"use strict"

const btnSi = document.getElementById("btn-si");
const btnNo = document.getElementById("btn-no");
const laForma = document.getElementById("forma-princ");
const losCampos = document.querySelectorAll("#op-ub");

let arrVal = [];

btnSi.addEventListener("click", function(){
    losCampos.forEach(vl => arrVal.push(vl.value))
    if(arrVal.every(v => v !== "")){
        laForma.submit();
    }
    else{
        alert("Por favor seleccione una nueva ubicación para todos los equipos")
        arrVal = []
    };
});

btnNo.addEventListener("click", function(){
    window.location.replace(`/mi_cuenta/ubicaciones`)
})