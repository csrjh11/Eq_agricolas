'use strict'
const tipoEquipo = document.getElementById("id_tipo_equipo");
const parametros = document.getElementById("parametros");
const ventaRenta = document.getElementById("tipo_operacion");
const te = ["Tractor", "Arado", "Rastra", "Sembradora", "Pulverizadora", "Cosechadora",]

te.forEach( marca =>{
    let opEstado = document.createElement("option");
    opEstado.text = marca
    opEstado.value = marca.toLowerCase()
    tipoEquipo.add(opEstado);
  })

const arado = `<p>
<label for="parametro_1">Tipo de Cuerpos:</label>
<select name="parametro_1" class="form-control" id="parametro_1">
    <option value="vertedera">Vertedera</option>

    <option value="disco">Disco</option>

    <option value="cincel">Cincel</option>

    <option value="subsuelo">Subsuelo</option>
</select>
</p>
<p><label for="parametro_2">¿Reversible?:</label> 
<select name="parametro_2" id="parametro_2" class = "form-control">
    <option value = si>Si</option>
    <option value = no>No</option>
</select>
</p>
<p><label for="parametro_3">Número de cuerpos:</label> <input type="number" name="parametro_3" class="form-control" min="1" required="" id="parametro_3"></p>
<p><label for="parametro_4">¿Neumático o Mecánico?</label> <select name="parametro_4" class="form-control" id="parametro_4">
<option value="neumatica">Neumático</option>

<option value="mecanica">Mecánico</option>

</select></p>
`
const tractor = `<p><label for="parametro_1">Potencia del Motor (HP):</label> <input type="number" name="parametro_1" class="form-control" min="1" required="" id="parametro_1"></p>
<p><label for="parametro_2">Estrias de la Toma de Fuerza:</label> <select name="parametro_2" class="form-control" id="parametro_2">
<option value="6">6</option>

<option value="21">21</option>

</select></p>
<p><label for="parametro_3">¿Con enganche de tres puntos?</label> 
    <select name="parametro_3" id="parametro_3" class = "form-control" >
    <option value = si>Si</option>
    <option value = no>No</option>
</select>

</p>
<p><label for="parametro_4">Tipo de Tracción:</label> <select name="parametro_4" class="form-control" id="parametro_4">
<option value="delantera">Delantera</option>

<option value="trasera">Trasera</option>

<option value="4wd">4WD</option>

</select></p>
<p><label for="parametro_5">¿Con Cabina?</label>     <select name="parametro_5" id="parametro_5" class = "form-control">
    <option value = si>Si</option>
    <option value = no>No</option>
</select></p>`

const rastra = `<p><label for="parametro_1">Tipo de Acople:</label> <select name="parametro_1" class="form-control" id="parametro_1">
<option value="Integral">Integral</option>

<option value="De Tiro">De Tiro</option>

</select></p>
<p><label for="parametro_2">Tipo de cuerpos:</label> <select name="parametro_2" class="form-control" id="parametro_2">
<option value="Disco Liso">Disco Liso</option>

<option value="Disco Dentado">Disco Dentado</option>

<option value="Discos Combinados">Discos Combinados</option>

</select></p>
<p><label for="parametro_3">No  de cuerpos:</label> <input type="number" name="parametro_3" class="form-control" min="1" required="" id="parametro_3"></p>
<p><label for="parametro_4">Disposicion de los cuerpos:</label> <select name="parametro_4" class="form-control" id="parametro_4">
<option value="Simple">Simple</option>

<option value="Tandem">Tandem</option>

<option value="Offset">Offset</option>

</select></p>`

const sembradora = `<p><label for="parametro_1">Tipo de Sembradora:</label> <select name="parametro_1" class="form-control" id="parametro_1">
<option value="Voleo">De Voleo</option>

<option value="Chorrillo">A chorrillo</option>

<option value="Precision">De Precisión</option>

<option value="Monograno">Monograno</option>

</select></p>
<p><label for="parametro_2">¿Con Fertilizadora?:</label> <select name="parametro_2" id="parametro_2" class = "form-control">
    <option value = si>Si</option>
    <option value = no>No</option>
</select></p>
<p><label for="parametro_3">No de tolvas:</label> <input type="number" name="parametro_3" class="form-control" min="1" required="" id="parametro_3"></p>
<p><label for="parametro_4">¿Neumatica o Mecánica?</label> <select name="parametro_4" class="form-control" id="parametro_4">
<option value="neumatica">Neumática</option>

<option value="mecanica">Mecánica</option>

</select></p>`


const pulverizadora = `<p><label for="parametro_1">¿Autopropulsada?</label> <select name="parametro_1" id="parametro_1" class = "form-control">
<option value = si>Si</option>
<option value = no>No</option>
</select></p>
<p><label for="parametro_2">Capacidad del Tanque (Litros):</label> <input type="number" name="parametro_2" class="form-control" min="1" required="" id="parametro_2"></p>
<p><label for="parametro_3">Número de Boquillas:</label> <input type="number" name="parametro_3" class="form-control" min="1" required="" id="parametro_3"></p>
<p><label for="parametro_4">Capacidad de la Bomba:</label> <input type="number" name="parametro_4" class="form-control" min="1" required="" id="parametro_4"></p>
`

const cosechadora = `<p><label for="parametro_1">Tipo de cultivo a Cosechar:</label> <input type="text" name="parametro_1" class="form-control" required="" id="parametro_1"></p>
<p><label for="parametro_2">Potencia del motor(HP):</label> <input type="number" name="parametro_2" class="form-control" min="1" required="" id="parametro_2"></p>
<p><label for="parametro_3">Capacidad de almacenaje de granos:</label> <input type="number" name="parametro_3" class="form-control" min="1" required="" id="parametro_3"></p>
<p><label for="parametro_4">Tasa de descarga (L/s):</label> <input type="number" name="parametro_4" class="form-control" min="1" required="" id="parametro_4"></p>`

const obEq = {
    "arado":arado,
    "tractor":tractor,
    "sembradora":sembradora,
    "cosechadora": cosechadora,
    "pulverizadora":pulverizadora,
    "rastra":rastra,
}

tipoEquipo.addEventListener("change", function(){
    let queEs = tipoEquipo.value
    if(queEs === ""){
        console.log("ajam")
        parametros.innerHTML = ""
    }else{
        parametros.innerHTML = ""
        parametros.innerHTML += obEq[queEs]
    }

})


const divFEchas = document.getElementById("fechas")
const htmlFechas = `            <p>
<label for="fecha_inicio">Seleccione Fecha Inicial</label>
<input type="date" class = "form-control" id = "fecha_inicio" name = "fecha_inicio" required>
</p>
<p >
<label for="fecha_final">Seleccione Fecha Final</label>
<input type="date" class = "form-control" id = "fecha_final" name = "fecha_final" required>
</p>`



ventaRenta.addEventListener("change", function(){
    let vr = ventaRenta.value
    if(vr === "renta"){

        divFEchas.innerHTML =""
        divFEchas.innerHTML += htmlFechas

    }else{
        divFEchas.innerHTML =""
    }
})