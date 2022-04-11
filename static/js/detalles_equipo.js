"use strict"

const btnRenta = document.getElementById("b-renta");
const btnCompra = document.getElementById("b-compra");
const numeroEquipo = document.getElementById("num-eq");
const usuario = document.getElementById("usr").value;
const elModal = document.querySelector(".modal");
const btnCerrar = document.querySelector(".close");
const btnEspecificos = document.getElementById("btn-especificos");
const datsEspecificos = document.getElementById("especificos")

if(btnRenta){
    btnRenta.addEventListener("click", function(){
        if(usuario !== "AnonymousUser"){
            window.location.href = `/renta/${numeroEquipo.value}`
        }else{
            elModal.style.display = "block"
        }
    })
}

if(btnCompra){
    btnCompra.addEventListener("click", function(){
        if(usuario !== "AnonymousUser"){
            window.location.href = `/venta/${numeroEquipo.value}`
        }else{
            elModal.style.display = "block"
        }
    })
}

btnCerrar.addEventListener("click", function(){elModal.style.display = "none"})
document.addEventListener("keydown", function(e){
    if(e.key === "Escape"){
        elModal.style.display = "none"
    }
})

btnEspecificos.addEventListener("click", function(){
    datsEspecificos.classList.toggle("hidden")
})