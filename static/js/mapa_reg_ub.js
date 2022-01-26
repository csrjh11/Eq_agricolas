"use strict";


class Mapa{
    #mapa;
    #marcador;

    constructor(){
        this.getPosition();
        
    }
    con_default(){
        alert("Couldn't get current position!")
        const coords_def =  [19.46499475547948, -98.9073248779107]
        this.loadMap(coords_def)
    }

    getPosition(){
        if(navigator.geolocation){
            navigator.geolocation.getCurrentPosition(this.loadMap.bind(this), //Caso Positivo
            this.con_default.bind(this) //Caso Negativo
            )}

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
    console.log(latitude)


    this.#mapa = L.map('map').setView([latitude, longitude], 15);

    L.tileLayer('https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(this.#mapa);
    this.#mapa.invalidateSize();



    this.#mapa.on("click", this.renderUbicacion.bind(this))
    }

    renderUbicacion(event){
        if (this.#marcador){
            this.#mapa.removeLayer(this.#marcador)
        }        
        const equis = event.latlng.lat
        const ye = event.latlng.lng
        console.log(typeof(ye))
        this.#marcador = L.marker([equis, ye], {"draggable": true})
        this.#mapa.addLayer(this.#marcador)

        inputX.value = equis
        inputY.value = ye
    }
}

const inputX = document.getElementById("cdx");
const inputY = document.getElementById("cdy");
const botGo = document.getElementById("dale");
const formaLdehido = document.getElementById("forma-princ");
const muni = document.getElementById("municipio");
const estadoC = document.getElementById("estado");


const mapaT1= new Mapa
const llAPI = "AIzaSyA6BgqA2oKejfHVnFodwFPmIDJZDIH6YeE"

botGo.addEventListener("click", function(){
    const equis = inputX.value
    const ye = inputY.value

    if(!equis) alert("Por favor seleccione una ubicación")
    else{
        const coords = `${equis},${ye}`
        const datos = datos_dir(coords, llAPI)
    }
})


const datos_dir= async function(coords, llave){
    const respo = await fetch(`https://maps.googleapis.com/maps/api/geocode/json?latlng=${coords}&key=${llave}`)
    const jsonR = await respo.json()
    console.log(jsonR)
    let elIndex = jsonR.results.map( res => res.types).findIndex(areg => areg.includes("administrative_area_level_2"))
    console.log(elIndex)
    if (elIndex == -1){
        elIndex = jsonR.results.map( res => res.types).findIndex(areg => areg.includes("administrative_area_level_3"))
    }
    const municipio = jsonR.results[elIndex].address_components[0].long_name
    const estado = jsonR.results[elIndex].address_components[1].long_name    
    muni.value = municipio
    estadoC.value = estado
    console.log(municipio, estado)
    formaLdehido.submit()
}
