
function Mensaje1() {
    document.getElementById('p1').textContent = "Hola Parrafo 1";
}

function Mensaje2(texto) {
    document.getElementById('p1').textContent = texto;
}

// setTimeout(Mensaje1, 3000);
// setTimeout(function() {Mensaje2("Hola Mundo");}, 3000);

function escribeHora() {
    let fecha = new Date();
    let hora = fecha.getHours() + ":" + fecha.getMinutes() + ':' + fecha.getSeconds();
    Mensaje2(hora);
}

setInterval(escribeHora, 1000);


