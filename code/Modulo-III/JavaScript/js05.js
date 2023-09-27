
google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {
    const datos =  google.visualization.arrayToDataTable([
        ['Estado', 'Población'],
        ['Ciudad de México', 12],
        ['Puebla', 3],
        ['Jalisco', 4.5],
        ['Oaxaca', 1.9 ]
    ]);

    const opciones = {title:'Ejemplo grafica de barras'}; 
    const grafica = new google.visualization.BarChart(document.getElementById('grafica1'));
    grafica.draw(datos, opciones);

    ///////////////////
    const opciones2 = {title:'Ejemplo grafica de PIE'}; 
    const grafica2 = new google.visualization.PieChart(document.getElementById('grafica2'));
    grafica2.draw(datos, opciones2);

}