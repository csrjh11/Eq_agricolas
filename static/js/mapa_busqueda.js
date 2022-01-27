"use strict";
window.onload = function(){
    const url = window.location.href
    console.log(url)

    slideOne();
    slideTwo();
}



//Definición de clase Mapa
class Mapa{
    #mapa;
    #equipos;

    constructor(){
        this.getPosition();
        this.consigueEquipos();        
    }


    renderWorkoutMarker(wo, cluster){
        // const bounds = this.#mapa.getBounds()
        const equis = parseFloat(wo.coord_x)
        const ye = parseFloat(wo.coord_y)

        // const lasEquis = [bounds._northEast.lat, bounds._southWest.lat]
        // const lasYes = [bounds._northEast.lng, bounds._southWest.lng]
        if(wo.precio_renta_dia != 0){
            var html_precios = `<div class="col-6">
            <h6>Precio de renta/dia:</h6>
            <h5>$${wo.precio_renta_dia}</h5>
            </div>`
        }else{
            var html_precios =`<div class="col-6">
            <h6>Precio de renta/dia:</h6>
            <h6>No Disponible</h6>
            </div>`
        }
        if(wo.precio_venta){
            html_precios +=`<div class="col-6 derecha">
            <h6>Precio de Venta</h6>
            <h5>$${wo.precio_venta}</h5>
            </div>`
        }
        const popu = L.popup({
        maxWidth: 250,
        minWidth: 100,
        autoClose: true,
        closeOnClick: true,
        })
        let m = L.marker([equis,ye])
        .bindPopup(popu)
        .setPopupContent(` <h6><strong>${ wo.tipo_eq.toUpperCase()} ${wo.marca} ${wo.modelo}</strong></h6>
        <hr>
        <div class="row">
         ${html_precios}
        </div>
        <hr>
        <div class="row">
            <h6>Ubicación:</h6>
            <h5>${wo.municipio}, ${wo.estado}</h5>
        </div>
        <hr>
        <div class="row center">
            <a class = "btn btn-outline-success " href="/browse/${wo.num}">Más Información</a>
        </div>`)

        cluster.addLayer(m)
        this.#mapa.addLayer(cluster)
    };

    con_default(){
        alert("No se pudo obtener su posición actual")
        const coords_def =  [19.46499475547948, -98.9073248779107]
        this.loadMap(coords_def)
    }

    getPosition(){
        if(navigator.geolocation){
            navigator.geolocation.getCurrentPosition(this.loadMap.bind(this), //Caso Positivo
            this.con_default.bind(this) //Caso Negativo
            )}
    }

    consigueEquipos = async function(){
        const respo = await fetch("/equipos")
        const jsonR = await respo.json()
        this.#equipos = jsonR.response

        let markerClusters = L.markerClusterGroup();
        this.#equipos.forEach(eq => this.renderWorkoutMarker(eq, markerClusters))
    }

    loadMap(pos){
    let latitude;
    let longitude;
    if(!pos.length){
        latitude = pos.coords.latitude;
        longitude = pos.coords.longitude;
    }else{
        latitude = pos[0]
        longitude = pos[1]
    }





    this.#mapa = L.map('map').setView([latitude, longitude], 15);

    L.tileLayer('https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(this.#mapa);
    this.#mapa.invalidateSize();

    }    
}
const mapaT1= new Mapa
const llAPI = "AIzaSyA6BgqA2oKejfHVnFodwFPmIDJZDIH6YeE"


//Componentes Sliders
const sliderUno = document.getElementById("slider-1");
const sliderDos = document.getElementById("slider-2");
const valorUno = document.getElementById("rango1");
const valorDos = document.getElementById("rango2");
const inputUno = document.getElementById("f1");
const inputDos = document.getElementById("f2");
let valIntermedio = 0

//Funciones Sliders
const slideOne = function(){
    if(parseInt(sliderDos.value) - parseInt(sliderUno.value) <= valIntermedio){
        sliderUno.value = parseInt(sliderDos.value) - valIntermedio
    }
    valorUno.textContent = sliderUno.value
    inputUno.value = sliderUno.value


}

const slideTwo = function(){
    if(parseInt(sliderDos.value) - parseInt(sliderUno.value) <= valIntermedio){
        sliderDos.value = parseInt(sliderUno.value) + valIntermedio
    }
    valorDos.textContent = sliderDos.value
    inputDos.value = sliderDos.value
}



