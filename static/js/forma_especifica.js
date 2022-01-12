'use strict'
const submitForms = function(){
    document.getElementById("forma-datos").submit();
}

const imgs = document.getElementById("imgs");
const row =document.getElementById("img-row");

imgs.addEventListener("change", function(){
    row.innerHTML = `<span class = "center">Previsualización de Imágenes</span> <br>`
    const files = this.files
    
    console.log(files.length)
    if(files.length){
        // row.innerHTML += `<span class = "center">Seleccione imágen principal</span>`

        for(let i  = 0;i<files.length;i++){
            const reader = new FileReader();

            reader.addEventListener("load", function(){
                console.log(this)
                row.innerHTML += `<div class = 'col-3 mx-4 my-1 brd img-cont'>
                <img h id = 'disp-img' src = '${this.result}' alt = 'imagen' class = 'fit'>
            </div>`
            })

            reader.readAsDataURL(files[i])
            console.log(i)
        }
        const arabSpring = document.querySelectorAll(".img-cont");
        console.log(arabSpring)
    }


})

