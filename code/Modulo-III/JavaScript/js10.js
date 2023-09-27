
function DespliegaMensaje(texto) {
    document.getElementById('p1').innerHTML = texto;
}

function DespliegaMensaje2(texto) {
    document.getElementById('p2').innerHTML = texto;
}


let promesa = new Promise(function(myResolve, myReject) {
    let req = new XMLHttpRequest();
    req.open('GET', './js01.html');
    req.onload = function() {
        if (req.status == 200) {
            myResolve(req.response);
        }else {
            myReject("Error al intentar abrir el archivo, estado " + req.status);
        }
    };
    req.send();
});

promesa.then(
    function (value) {DespliegaMensaje(value);},
    function (error) {DespliegaMensaje(error);}
);

// Otro ejemplo
// Uso del catch 
const promesa2 = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve('Fin de manera exitosa');
    }, 3000);
    throw new Error('Excepción de pruebas...');
});

promesa2.then( (value) => {
    DespliegaMensaje2(value);
}).catch((error) => {
    DespliegaMensaje2(error);
});