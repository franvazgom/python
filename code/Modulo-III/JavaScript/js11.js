function DespliegaMensaje(texto) {
    document.getElementById('p1').innerHTML = texto;
}

// La palabra async antes de una función hace que dicha función regresa una PROMESA
function mensaje() {
    return Promise.resolve("Saludos");
}

async function mensaje2() {
    return "Saludos";
}

mensaje2().then (
    function (value) {DespliegaMensaje(value);},
    function (error) {DespliegaMensaje(error);}
)

// Ejemplo 2
async function DespliegaMensaje2() {
    let promesa = new Promise(function (resolve) {
        setTimeout(function() {resolve("Despues de los 3 segundos..");}, 3000);
    });
    DespliegaMensaje("Mensaje 1 de la función DespliegaMensaje2");
    document.getElementById('p2').innerHTML = await promesa;
    console.log('Termina la función DespliegaMensaje2');
}

DespliegaMensaje2();