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


// //BOTONES
// const btnUno = document.getElementById("uno");
// const btnDos = document.getElementById("dos");
// const btnTres = document.getElementById("tres");

// //Contenidos
// const cont1 = document.getElementById("contenido-1");
// const cont2 = document.getElementById("contenido-2");
// const cont3 = document.getElementById("contenido-3");

// btnUno.addEventListener("click", function(){
//     if (!cont2.classList.contains("hidden")){
//         cont1.classList.remove("hidden")
//         cont2.classList.add("hidden")
//         cont3.classList.add("hidden")

        
//         btnUno.classList.add("btn-primary")
//         btnDos.classList.remove("btn-primary")
//         btnTres.classList.remove("btn-primary")

        
//         btnUno.classList.remove("btn-light")
//         btnDos.classList.add("btn-light")
//         btnTres.classList.add("btn-light")
        
//     }
// });
// btnDos.addEventListener("click", function(){
//     if (cont2.classList.contains("hidden")){
//         cont1.classList.add("hidden")
//         cont2.classList.remove("hidden")
//         cont3.classList.add("hidden")
        
//         btnUno.classList.remove("btn-primary")
//         btnUno.classList.add("btn-light")

//         btnDos.classList.remove("btn-light")
//         btnDos.classList.add("btn-primary")


//     }
// });

