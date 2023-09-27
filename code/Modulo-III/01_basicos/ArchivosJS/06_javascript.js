
function varTest() {
    var x = 45;
    if (true) {
        var x = 90;
        console.log(x);
    }
    console.log(x);
}

function letTest() {
    let x = 45;
    if (true) {
        let x = 90;
        console.log(x);
    }
    console.log(x);
}

const cteNumero = 50;
function testConstant() {
    cteNumero = 45; // Error porque es una constante 
    console.log(cteNumero);
}

console.log("varTest..");
varTest();
console.log("---------------------------------------");
console.log("letTest..");
letTest();

testConstant();