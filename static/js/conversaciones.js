"use strict"

const lConv = document.getElementById("con-m").children
const arrBtn = []
const idUs = document.getElementById("elaidi").value
const contM = document.getElementById("msjs")
const areaNM = document.querySelector(".nuevo-m")
const btnNM = document.querySelector(".btn-send")
const areaENM = document.getElementById("btn-txt")
const formaNM = document.querySelector(".fnm")
const csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value
let idConversacion
let convAct
let mensaje




for(var i = 0; i < lConv.length; i++){
    arrBtn.push(lConv[i])
}

arrBtn.forEach(btn => btn.addEventListener("click", () => {
    areaNM.classList.remove("hidden")
    if(btn.id === convAct){
        return
    }else{
        mensajes(btn.id)
    }
    
}))

btnNM.addEventListener("click", function(e){
    e.preventDefault()
    mensaje = areaENM.value
    if(mensaje == "" || mensaje.trim() == ""){
        formaNM.reset();
    }else{
        formaNM.reset();
        contM.innerHTML += `<p class = "from-me">${mensaje}</p>`
        postear(`/conv/${convAct}`, {"msg" : mensaje, "id_conv" : idConversacion})
    }
})


const armaMensajes = function(arM){
    arM.forEach(ms => {
        if(ms.remitente == idUs){
            contM.innerHTML += `<p class = "from-me">${ms.cont}</p>`
        }
        else if(ms.remitente != idUs){
            contM.innerHTML += `<p class = "from-them">${ms.cont}</p>`
        }
    })
    return
}


const mensajes = async function(aidi){
    const respo = await fetch(`/mensajes/${aidi}`)
    const jsonR = await respo.json()
    // if (jsonR.response.length >0){

    // }
    
    idConversacion = jsonR.response[0].id_conversacion
    const msjOrdenados = jsonR.response.sort(function(a, b){
        if (a.id > b.id) {
            return 1;
        }
        if (a.id < b.id) {
            return -1;
        }
        return 0
    })
    armaMensajes(msjOrdenados);
    convAct = aidi
}


const postear = async function(url, datos){
    const response = await fetch(url, { method      : "POST",
                                        credentials : "same-origin",
                                        body        : JSON.stringify(datos),
                                        headers     : {"X-Requested-With"  : "XMLHttpRequest",
                                                        "X-CSRFToken"       : csrf}
                                                    })
}

