'use strict'

const btnGenerales = document.getElementById("btn-generales");
const btnEspecificos = document.getElementById("btn-especificos");
const formaGenerales = document.getElementById("generales");
const formaEspecificos = document.getElementById("especificos");

const hijosGenerales = formaGenerales.querySelectorAll("input, select, textarea")
let presionadoGr = false

const hijosEspecificos = formaEspecificos.querySelectorAll("input, select")
let presionadoEsp= false

btnGenerales.addEventListener("click", function(){    
    if(!presionadoGr){
        hijosGenerales.forEach( hijo => hijo.disabled = false)
        btnGenerales.textContent = "Guardar Cambios";
        btnGenerales.classList.add("btn-primary");
        presionadoGr = true;
    }else{
        formaGenerales.submit()
    }
})

btnEspecificos.addEventListener("click", function(){    
    if(!presionadoEsp){
        hijosEspecificos.forEach( hijo => hijo.disabled = false)
        btnEspecificos.textContent = "Guardar Cambios";
        btnEspecificos.classList.add("btn-primary");
        presionadoEsp = true;
    }else{
        formaEspecificos.submit()
    }
})