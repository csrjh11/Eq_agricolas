'use strict'

const listaBotones =document.getElementById("botones").querySelectorAll("button")
const listaContenidos = document.querySelectorAll(".cont");

listaBotones.forEach(btn => btn.addEventListener("click", function(){

    const indice = Array.prototype.indexOf.call(listaBotones,this)
    listaContenidos.forEach((el, i) => {
        if(i == indice){
            el.classList.remove("hidden");
        }else{
            el.classList.add("hidden");
        }
    })
    listaBotones.forEach((el,i) =>{
        if(i == indice){
            el.classList.add("btn-primary")
            el.classList.remove("btn-light")
        }else{
            el.classList.add("btn-light")
            el.classList.remove("btn-primary")
        }
    })
}))

//////////// Contro de respuestas

const listaBotonesRespuestas = document.querySelectorAll("#boton-respuestas")
console.log(listaBotonesRespuestas)
const listaRespuestas = document.querySelectorAll(".row-resp");
console.log(listaRespuestas)



listaBotonesRespuestas.forEach( btn => btn.addEventListener("click", function(){

    const indice = Array.prototype.indexOf.call(listaBotonesRespuestas,this)
    if(btn.classList.contains("btn-outline-danger")){
        listaRespuestas.forEach((el, i) => {
            if(i == indice){
                el.classList.add("hidden");
            }
        })
        btn.classList.add("btn-outline-success")
        btn.classList.remove("btn-outline-danger")
        btn.textContent = "Ver Respuestas"
        
    }else{
        listaRespuestas.forEach((el, i) => {
            if(i == indice){
                el.classList.remove("hidden");
            }
        })
        btn.classList.remove("btn-outline-success")
        btn.classList.add("btn-outline-danger")
        btn.textContent = "Ocultar Respuestas"
    }
}))
