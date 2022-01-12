"use strict"

//BOTONES
const btnUno = document.getElementById("uno");
const btnDos = document.getElementById("dos");
const btnTres = document.getElementById("tres");
const btnCuatro = document.getElementById("cuatro");

//TEXTOS
const texto1 = document.getElementById("txt-uno");
const texto2 = document.getElementById("txt-dos");
const texto3 = document.getElementById("txt-tres");
const texto4 = document.getElementById("txt-cuatro");

//Etiquetas
const etiqueta1 = document.getElementById("bo1");
const etiqueta2 = document.getElementById("bo2");
const etiqueta3 = document.getElementById("bo3");
const etiqueta4 = document.getElementById("bo4");


let activo = 0
const arreg = ["1", "2", "3", "4"];
const arr2 = arreg.map(val => "texto" + val)
const arr3 = arreg.map(val => "etiqueta" + val)
const arreg1 = [1,2,3,4]

const funcionEV = function(arr){
    
    eval(arr2[arr[0] - 1]).classList.toggle("hidden");
    arr.slice(1).forEach( function(val){
        eval(arr2[val - 1]).classList.add("hidden");
    });

    eval(arr3[arr[0] - 1]).classList.add("foco");
    eval(arr3[arr[0] - 1]).classList.remove("card-header");
    arr.slice(1).forEach( val => eval(arr3[val - 1]).classList.remove("foco"));
    arr.slice(1).forEach( val => eval(arr3[val - 1]).classList.add("card-header"));
}


btnUno.addEventListener("click", () =>  funcionEV([1,2,3,4]));
btnDos.addEventListener("click", () =>  funcionEV([2,1,3,4]));
btnTres.addEventListener("click", () =>  funcionEV([3,1,2,4]));
btnCuatro.addEventListener("click", () =>  funcionEV([4,1,2,3]));
