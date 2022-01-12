'use strict'

const venta = document.getElementById("id_precio_venta");
const renta = document.getElementById("id_precio_renta_dia");
const seleccion = document.getElementById("id_para_que");
const seleccionMarca = document.getElementById("id_marca");
const seleccionModelo = document.getElementById("id_modelo");
const seleccionTipo  = document.getElementById("id_tipo_equipo");
const contenedorMarca = document.getElementById("contenedor-marca");
const contenedorModelo = document.getElementById("contenedor-modelo");

const padreVenta = venta.parentElement;
const padreRenta = renta.parentElement;
const te = ["Tractor", "Arado", "Rastra", "Sembradora", "Pulverizadora", "Cosechadora", "Otro"]
const listaMarcas = ['Case', 'Claas', 'Deutz-Fahr', 'Fendt', 'Ford', 'John Deere', 'Kubota', 'Massey Ferguson', 'New Holland', 'Valtra', "Otra"]

const modelos = {
  "Case": {
    "tractor" : ["Steiger", "Magnum AFS", "Puma", "Maxxum", "Farmall", "Otro"],
    "arado" : ['1-F194', '1-F296', '10', '125', '140', '145', '155', '165', '189', '193', '194', '1AV-193', '203S', '204S', '210',  '213S',  '214S', '215', '295', '296', '30 SERIES','58C SERIES', '60',
    '600 SERIES', '6000', '60L', '620', '641', '642', '6500', '6650', '70', '700-SERIES', '70L', '710', "Otro"],
    "rastra" : ['122', '310', '350', '370', '3800', '3850', '3900', '3950', '475', '485', '496', '501', '596', '696', '760', '770', '780', "Otro"],
    "sembradora": ['30', '40', '500', '510', '5100', '5200', '5300', '620', '6200', '6300', '7100', '7200', '8500', '8600', 'CONCORD', 'SDX30', 'SDX40', "Otro"],
    "pulverizadora": ["CIH", "Patriot", "SP", "SPX", "Trident", "TS"],
    "cosechadora" : ["Axial-Flow", "A8000", "A8800", "Otro"]
  },
  "Claas": {
    "tractor" : ["Xerion", "Axion", "Arion", "Elios", "Nexos", "Otro"],
    "cosechadora" : ["Lexion", "Trion"]
  },
  'Deutz-Fahr' : {
    "tractor" : ['5DF TTV ActiveSteer', '6145W HD', '6W Profi', '7250 TTV Agrotron', '8280 TTV', '9340 TTV Agrotron', 'Agroclimber', 'Agroclimber F/V', 'Agrofarm C', 'Agrofarm G', 'Agrofarm G - ROPS',
    'grolux', 'Agrolux', 'Agromaxx', 'Agroplus F Ecoline', 'Agroplus F Keyline', 'Agroplus F-V-S', 'Serie 2W', 'Serie 4E', 'Serie 4W', 'Serie 5G LRC', 'Serie 6', 'Serie 6', 'Serie 6G', 'Serie 6W', 'Serie 6W ', 'Series 4E', "Otro"],
    "cosechdora": ["C7206 TS", "Serie C6000", "Otro"]
  },
  "Fendt" : {
    "tractor" : ['Fendt 1100 Vario MT', 'Fendt 1000 Vario', 'Fendt 900 Vario', 'Fendt 800 Vario', 'Fendt 700 Vario', 'Fendt 500 Vario', 'Fendt 300 Vario', 'Fendt 200 Vario', "Otro"],
    "pulverizador" : ["Rogator 300", "Rogator 600", "Otro"],
    "cosechadora" : ["Ideal", "Serie C", "Serie SL", "Serie L", "Serie E"]
  },
  "Ford" : {
    "tractor" : ["7610", "7840", "5000", "2000", "6610", "6600", "3000", "4000", "7810", "TW25", "TW35"]
  },
  "John Deere" : {
    "tractor": ["1023E", "1025R", "2025R", "2032R", "2038R", "3025D", "3025E", "3032E", "3033R", "3035D", "3038E",  "3039R", "3043D", "3046R", "4044M", "4044R", "4052M", "4052M Heavy Duty", "4052R", "4066M", "4066M Heavy Duty", "4066R",
    "5075GL", "5075GL", "5075GN", "5075GV", "5090EL", "5090GN", "5090GV", "5100GN", "5100MH", "5100ML", "5115ML", "5115RH", "5125ML", "6120EH", "6155MH", "6155RH", "6R 175", "6R 195", "6R 215", "6R 230", "6R 250", "7R 210",
    "7R 230", "7R 250", "7R 270", "7R 290", "7R 310", "7R 330", "7R 350", "8R 230", "8R 250", "8R 280", "8R 310", "8R 340", "8R 370", "8R 410", "8RT 310", "8RT 340", "8RT 370", "8RT 410", "8RX 310", "8RX 340", "8RX 370",
    "8RX 410", "9R 390", "9R 440", "9R 490", "9R 540", "9R 590", "9R 640", "9RT 470", "9RT 520", "9RT 570", "9RX 490", "9RX 540", "9RX 590", "9RX 640", "Otro"],
    "arado" : ["624", "635", "645", "945", "975", "995", "3745", "3755", "Otro"],
    "rastra" : ["660", "670", "2633VT", "2660VT","MX225", "MX425", "Otro"],
    "sembadora" : ['1590', '1715', '1725', '1735', '1745', '1755', '1765', '1775', '1775NT', '1795', 'BD11', 'C650', 'DB44', 'DB60', 'DB66', 'DB80', 'DB90', 'DR12', 'DR16', 'DR24', "Otro"],
    "pulverizadora" : ['4630', '4730', 'Serie 400', 'Serie 600', 'Serie 800R', 'Serie Hagie', 'Serie PV', "Otro"],
    "cosechadora" : ["Serie CH", "Serie S", "Serie T", "Serie X", "Otro"]
  },
  "Kubota" : {
    "tractor" : ["Serie B", "Serie L", "Serie M", "Otro"]
  },
  "Massey Ferguson" : {
    "tractor" : ['MF 1500', 'MF1600 E', 'MF SERIE CLASSIC', 'MF 2600 LR', 'MF 4700', 'MF 2600 MR', 'MF 2600 E', 'MF 5700', 'MF 2600 HR', 'MF 6700', 'MF 7600', 'MF 7700 S', 'MF 8700', 'MF 8700 S', "Otro"],
    "arado" :["MF-AH03", "MF-AH04", "MF-AV200", "MF-S1", "MF-S3-5", "MF-S5-9", "MF-BR06", "Otro" ],
    "rastra" : ["MF-RT1824", "MF-RT2024", "MF-RT3224", "MF-RL1822	", "MF-RL1824", "MF-RL2024", "Otro" ],
    "pulverizadora" : ["MF9030", "MFA600", "Otro"],
    "cosechadora" : ["MF 6690", "Otro"],
  },
  "New Holland" :{
    "tractor" : ["Serie 10s", "Boomer-25", "Workmaster 40", "TT3", "Serie TT", "T3F", "LDF LP", "TS600", "6810", "Genesis T8", "Otro"],
    "pulverizadora" : ["Serie SA", "Otro"],
    "cosechadora" : ["Serie TC", "Serie FR", "Serie FP", "Otro"]
  },
  "Valtra" : {
    "tractor" : ["Serie A", "Serie F", "Serie G", "Serie N", "Serie S", "Serie T", "Otro"]
  },
  "Otra" :[]
}

// const lds = ["Serie PV", "4630", "4730", "Serie 400", "Serie 600", "Serie Hagie", "Serie 800R"]
// const lord = lds.sort()
// console.log(lord)


const ePrincipal = function(){
  padreVenta.classList.add("hidden");
  padreRenta.classList.add("hidden");
}

ePrincipal()


// Agrega Tipo de equipos a Select
te.forEach( marca =>{
  let opEstado = document.createElement("option");
  opEstado.text = marca
  opEstado.value = marca.toLowerCase()
  seleccionTipo.add(opEstado);
})

// Crea Etiqueta y Campo para Otra MArca
const pCont = document.createElement("p");
pCont.classList.add("hidden");
const pEtiqueta = document.createElement("label");
pEtiqueta.innerHTML = "Escriba el nombre de la Marca"
pEtiqueta.setAttribute("for", "otra-marca");
const p = document.createElement("input");
p.setAttribute('type', 'text');
p.setAttribute("id", "otra-marca");
p.classList.add("form-control");
pCont.appendChild(pEtiqueta)
pCont.appendChild(p);
seleccionMarca.parentElement.after(pCont);


//control de venta y renta
seleccion.addEventListener("change", function(){
  if (seleccion.value === "venta"){
    ePrincipal()
    padreVenta.classList.remove("hidden");
    renta.value = 0
  }else if(seleccion.value === "renta"){
    ePrincipal()
    padreRenta.classList.remove("hidden");
    venta.value = 0
  }else if(seleccion.value === "ambos"){
    padreVenta.classList.remove("hidden");
    padreRenta.classList.remove("hidden");
  }
})


//Control de seleción de Tipo
seleccionTipo.addEventListener("change", function(){
  // if(seleccionTipo.value !== "Otro"){ ------------------------------------------------------------------ Aqui te Quedaste(Con Otros)

  // }
  contenedorMarca.classList.remove("hidden");
  while(seleccionMarca.firstChild){
    seleccionMarca.removeChild(seleccionMarca.firstChild)
  }
  // Agrega marcas a Select
  listaMarcas.forEach( marca =>{
    if(modelos[marca][seleccionTipo.value]){
      let opEstado = document.createElement("option");
      opEstado.text = marca
      opEstado.value = marca
      seleccionMarca.add(opEstado);
    }
})})




//Control de cambio de Marca
seleccionMarca.addEventListener("change", function(){
  if (seleccionMarca.value === "Otra"){
    pCont.classList.remove("hidden");
    p.required = true;
  }
  else{
    contenedorModelo.classList.remove("hidden");
    pCont.classList.add("hidden")
    p.required = false;
    const sel = seleccionMarca.value
    const datosModelo = modelos[sel]
    const datosFinal = datosModelo[seleccionTipo.value]
    if (datosFinal){
      while(seleccionModelo.firstChild){
        seleccionModelo.removeChild(seleccionModelo.firstChild)
      }
      datosFinal.forEach( dato =>{
        let elModelo = document.createElement("option");
        elModelo.text = dato
        elModelo.value = dato
        seleccionModelo.add(elModelo)
      })
    
    }


  }
})