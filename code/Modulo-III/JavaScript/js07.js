
// Una función de tipo CallBack es una función que pasa como un ARGUMENTO en otra función 
function mensaje(texto) {
    document.getElementById('p1').textContent = texto;
}
function suma(n1, n2, funCB) {
    let res = n1 + n2;
    funCB(res);
}
suma(3, 4, mensaje);

// Ejemplo 2 
const numeros = [3, 2, -2, -1, 5, -5, 6, 1, -1, 4];

function eliminaNumNegativos(arreglo, fCB) {
    const numPos = [];
    for (const x of arreglo) {
        if (fCB(x)) {
            numPos.push(x);
        }
    }
    return numPos;
}

const resultado = eliminaNumNegativos(numeros, z => z >= 0);
console.log(resultado);

const resultado2 = eliminaNumNegativos(numeros, z => z < 0);
console.log(resultado2);

const resultado3 = eliminaNumNegativos(numeros, z => z%2 == 0);
console.log(resultado3);
