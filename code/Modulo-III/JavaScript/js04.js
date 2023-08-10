
const xArray = ["Mexico", "Puebla", "Jalisco", "BCN", "Tlaxcala"]; 
const yArray = [12, 4, 5.5, 1.2, 0.5];

const data = [
    {
        x:xArray, 
        y:yArray,
        type:'bar',
        orientation:"v",
        marker: {color:'rgba(0,0,255,0.6)'}
    }
];

const titulo = {title:'Estado / Millones de personas'};
Plotly.newPlot("grafica1", data, titulo);
// ---------------
const data2 = [
    {
        x:yArray, 
        y:xArray,
        type:'bar',
        orientation:"h",
        marker: {color:'rgba(255,0,0,0.6)'}
    }
];

const titulo2 = {title:'Grafica 2'};
Plotly.newPlot("grafica2", data2, titulo2);
// ---------------
const data3 = [
    {
        labels:xArray, 
        values:yArray,
        type:'pie'
    }
];

const titulo3 = {title:'Grafica de PIE'};
Plotly.newPlot("grafica3", data3, titulo3);
// ---------------
const xDatos = [];
const yDatos = [];
for (let x=0; x<20; x += 0.1){
    xDatos.push(x);
    yDatos.push(Math.cos(x));
}

const data4 = [
    {
        x:xDatos, 
        y:yDatos,
        mode:"lines"
    }
];

const titulo4 = {title:'COSENO'};
Plotly.newPlot("grafica4", data4, titulo4);