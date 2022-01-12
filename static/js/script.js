'use strict'

const botones = document.querySelectorAll(".btn-link")
const sig1 = document.getElementById("next1")



console.log(botones)
console.log(sig1)
botones.forEach(btn => console.log(btn.dataset))
botones.forEach(btn => btn.addEventListener("click", function(){
    const texto = document.querySelector(btn.dataset.target)
    texto.classList.toggle("show")
}))

// sig1.addEventListener("click", function(){
//     const abre = document.querySelector("#collapseTwo")
//     const cierra = document.querySelector("#collapseOne")

//     abre.classList.toggle("show")
//     cierra.classList.toggle("show")
// })

let elMapa;

const getPosition = function(){
    if(navigator.geolocation){
        navigator.geolocation.getCurrentPosition(loadMap, function(){
            alert("Couldn't get current position!")
        })}
}

const loadMap = function(pos){
    console.log(this)
    const{latitude} = pos.coords;
    const{longitude} = pos.coords;

    elMapa = L.map('map').setView([latitude, longitude], 15);
    console.log(elMapa)

    L.tileLayer('https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(elMapa)}

getPosition()