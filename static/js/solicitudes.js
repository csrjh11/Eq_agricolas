'use strict'

//BOTONES
const btnUno = document.getElementById("uno");
const btnDos = document.getElementById("dos");

//Contenidos
const cont1 = document.getElementById("contenido-1");
const cont2 = document.getElementById("contenido-2");

btnUno.addEventListener("click", function(){
    if (!cont2.classList.contains("hidden")){
        cont2.classList.add("hidden")
        cont1.classList.remove("hidden")
        btnUno.classList.add("btn-primary")
        btnDos.classList.remove("btn-primary")
        btnDos.classList.add("btn-light")
        btnUno.classList.remove("btn-light")
    }
});
btnDos.addEventListener("click", function(){
    if (cont2.classList.contains("hidden")){
        cont2.classList.remove("hidden")
        cont1.classList.add("hidden")
        btnUno.classList.remove("btn-primary")
        btnUno.classList.add("btn-light")
        btnDos.classList.remove("btn-light")
        btnDos.classList.add("btn-primary")
    }
});

