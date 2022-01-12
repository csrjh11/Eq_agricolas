"use strict"

const bAlias = document.getElementById("btn-alias");
const bRef = document.getElementById("btn-ref");
const btnGo = document.getElementById("btn-go");
const dGo = document.getElementById("div-go");
const btnNel = document.getElementById("btn-nel");
const fAlias = document.getElementById("form-aref");
const btnUb = document.getElementById("btn-ub");
const elModal = document.querySelector(".overlay");
const btnGoMapa = document.getElementById("btn-go-mapa");
const btnNelMapa = document.getElementById("btn-nel-mapa");
const laImagen = document.querySelector(".img-ajustada");
const muni = document.getElementById("id-municipio");
const estadoC = document.getElementById("id-estado");
const eliminar = document.getElementById("drZ");


const latitud = document.getElementById("coord_x")
const longitud = document.getElementById("coord_y")
let elMarcador;
let mapa;
let cambioCrd = false;
const valInit = [];

const campoAlias = document.getElementById("id_alias");
const campoRef = document.getElementById("id_referencias");

valInit.push(campoAlias.value);
valInit.push(campoRef.value);
valInit.push(latitud.value);
valInit.push(longitud.value);

const salirMapa = function(){
    elModal.classList.add("hidden");
    latitud.value = valInit[2];
    longitud.value = valInit[3];
    cambioCrd = false;
}

bAlias.addEventListener("click", function(){
    campoAlias.disabled = false;
    dGo.classList.remove("hidden");
});

bRef.addEventListener("click", function(){
    campoRef.disabled = false;
    dGo.classList.remove("hidden");
});

btnNel.addEventListener("click",function(){
    campoAlias.value = valInit[0];
    campoRef.value = valInit[1];
    dGo.classList.add("hidden");
    campoAlias.disabled = true;
    campoRef.disabled = true;
});


btnGo.addEventListener("click", function(){
    if (confirm('Are you sure you want to save this thing into the database?')) {
        fAlias.submit()
        console.log('Thing was saved to the database.');
      } else {
        // Do nothing!
        console.log('Thing was not saved to the database.');
      }
});

btnUb.addEventListener("click", function(){
    elModal.classList.remove("hidden");
    cargaMapa()
})

const cargaMapa = function(){
    if(mapa){
        mapa.remove()
    }

    mapa = L.map("map-mod").setView([latitud.value, longitud.value], 13);

    L.tileLayer("https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png", {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(mapa)
    mapa.invalidateSize();

    elMarcador = L.marker([latitud.value, longitud.value], {"draggable":true})
    mapa.addLayer(elMarcador);

    mapa.on("click", renderMrk);

    elMarcador.on("dragend", function(event){
        const equis = event.target._latlng.lat
        const ye = event.target._latlng.lng
        latitud.value =equis;
        longitud.value = ye;
        cambioCrd = true
    });
}

const renderMrk = function(event){
    if(elMarcador){
        mapa.removeLayer(elMarcador);
    }
    const equis = event.latlng.lat
    const ye = event.latlng.lng
    elMarcador = L.marker([equis, ye], {"draggable": true})
    mapa.addLayer(elMarcador)
    cambioCrd = true
    latitud.value =equis;
    longitud.value = ye;


    elMarcador.on("dragend", function(e){
        const equis = e.target._latlng.lat
        const ye = e.target._latlng.lng
        latitud.value =equis;
        longitud.value = ye;
        cambioCrd = true

    });
}

window.onkeydown = function(e){
    if(!elModal.classList.contains("hidden")){
        if (e.keyCode == 27){
            salirMapa()
        }
    }
}

btnNelMapa.addEventListener("click",salirMapa);

btnGoMapa.addEventListener("click", function(){
    console.log(cambioCrd)
    if(confirm("Seguro que desea modificar esta ubicación?")){
        elModal.classList.add("hidden")
        
        if(cambioCrd){
            const crdd = `${latitud.value},${longitud.value }`
            datos_dir(crdd);
        }

    }else{
        alert("Cambios descartados.")
        salirMapa()
    }
})


const datos_dir = async function(coords){
    const respo = await fetch(`https://maps.googleapis.com/maps/api/geocode/json?latlng=${coords}&key=AIzaSyA6BgqA2oKejfHVnFodwFPmIDJZDIH6YeE`)
    const jsonR = await respo.json()
    let elIndex = jsonR.results.map( res => res.types).findIndex(areg => areg.includes("administrative_area_level_2"))
    if (elIndex == -1){
        elIndex = jsonR.results.map( res => res.types).findIndex(areg => areg.includes("administrative_area_level_3"))
    }
    const municipio = jsonR.results[elIndex].address_components[0].long_name
    const estado = jsonR.results[elIndex].address_components[1].long_name
    muni.value = municipio
    estadoC.value = estado
    console.log(municipio, estado)
    console.log(muni, estadoC)
    fAlias.submit()
}

eliminar.addEventListener("click", function(){
    if(confirm("¿Desea eliminar esta ubicación?")){
        const ubic = window.location.href.split("/");
        const laUbic = ubic[ubic.length - 1];
        window.location.replace(`${laUbic}/eliminar`);
    };
});