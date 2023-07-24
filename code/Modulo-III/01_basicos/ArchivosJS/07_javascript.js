
//Tipo string 

cadena = "Pruebas";

console.log("Prueba del FOR ");
for (i=0; i<cadena.length; i++) {
    console.log(cadena[i]);
}

console.log("Prueba del FOR 22 ");
for (i=cadena.length-1; i>=0; i--) {
    console.log(cadena[i]);
}

cad2 = cadena + " otra cadena";
console.log(cad2);

//Diccionario 
let auto = {
    marca: "Ford",
    submarca: "Ranger",
    modelo: 2023
};

//Notación punto
console.log(auto.marca);
// notación corchete
console.log(auto["marca"]);

//Para modificar un valor del diccionario
auto.marca = "VW";
auto['modelo'] = 2015;
console.log(auto);

//Arreglos
arreglo = [2, 4, 1, 5, 3, 2, 4, 7, 9];
console.log(arreglo[0]);
arreglo.sort();
console.log(arreglo);
console.log("Tamaño del arreglo: ");
console.log(arreglo.length);

for (i=0; i<arreglo.length; i++) {
    console.log(i, "= ", arreglo[i]);
}

