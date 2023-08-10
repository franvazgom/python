
// Función clásica
var x = function(a) {
    return a ** 2;
}
console.log(x(3));

// Funciones Flecha 1
var x1 = (a) => {
    return a ** 2;
}
console.log(x1(5));

// Funciones Flecha 2 
var x2 = (a) => a ** 2;  // Las llaves se pueden omitir, el return esta implícito
console.log(x2(7));

// Funciones Flecha 3
var x3 = a => a ** 2;  // Se pueden omitir los paréntesis porque solo es un argumento
console.log(x3(2));

// Función flecha sin argumentos 
var x4 = () => "Saludos"; 
console.log(x4());