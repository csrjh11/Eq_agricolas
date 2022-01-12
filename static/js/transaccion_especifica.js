"use strict"

const elBtnCancel = document.getElementById("cancel");
const divB = document.getElementById("divB");
const laForma = document.getElementById("cancelar");
const elIde = document.getElementById("wwmd").value;

const fechaInicio = document.querySelector(".f-ini").innerHTML.split("/");
const fechaRmada = `${fechaInicio[1]}/${fechaInicio[0]}/${fechaInicio[2]}`;
const hoy = new Date();
const prueba = Date.parse(fechaRmada);
const laFechaInicio = new Date(prueba);

if(laFechaInicio > hoy){
    divB.classList.remove("hidden");
}



elBtnCancel.addEventListener("click", function(){
    if(laFechaInicio > hoy){
        const diferencia = Math.trunc((laFechaInicio - hoy)/1000/60/60/24);
        if(diferencia >= 3){
            if (confirm("Seguro que desea cancelar esta transacción?")){
                window.location.replace(`/mi_cuenta/mis_tr/${elIde}/cancelar`)
            }
        }else{
            if(confirm("Esta transacción inicia en menos de 3 dias, cancelarla generará un costo. ¿Desea continuar? ")){
                window.location.replace(`/mi_cuenta/mis_tr/${elIde}/cancelar`)
            }
        }
    }
})