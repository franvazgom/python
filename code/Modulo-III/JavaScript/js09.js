
function DespliegueMensaje(texto) {
    document.getElementById('p1').innerHTML = texto;
}

// Sintaxis de una función tipo Promesa
let miPromesa = new Promise(function (myResolve, myReject){
    // Código de la función.. 
    if (0 > 1) {
        myResolve("Bien!!"); 
    }else {
        myReject("Error");
    }
}); 

miPromesa.then(
    function(value) {
        DespliegueMensaje(value);
    },
    function (error) { 
        DespliegueMensaje(error);
    }
);




