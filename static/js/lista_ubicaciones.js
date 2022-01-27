'use strict'

const btnB = document.querySelectorAll("#btn-el");
btnB.forEach(bt => bt.addEventListener("click", function(){
    nombre = this.parentNode.parentNode.firstElementChild.nextElementSibling.innerHTML
    aidi = this.firstElementChild.value
    if(confirm("Eliminar la ubicación {{ub.alias}}?")){
        window.location.replace(`/mi_cuenta/ubicaciones/${aidi}/eliminar`)
    }
}))

const 