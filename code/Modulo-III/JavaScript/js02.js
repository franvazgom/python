

// Seleccionar un elemento por ID 
p1 = $('#p1');
console.log(p1.text());
console.log('-----------------------------------');
p_1 = document.getElementById('p1');
console.log(p_1.textContent);

// Selecionar un elemento por el tag (tipo) 
todosParrafos = $('p');
todos_Parrafos = document.getElementsByTagName('p');
todos_Parrafos[0].style.fontSize = '35px';

//Seleccionar un elemento por clase
cRojo = $(".rojo");
c_Rojo = document.getElementsByClassName('rojo');
c_Rojo[0].style.fontSize = '20px';

//Seleccionar elemento por css
parrafoRojo = $('p.rojo');
parrafo_Rojo = document.querySelectorAll("p.rojo"); 

// Modificar el texto
// $('#p1').text('Hola');
// document.getElementById('p1').textContent = 'Hola 2';
// console.log($('#p1').text());
// console.log(document.getElementById('p1').textContent);

// Modificar el HTML
// $('#p1').html('<h3>Header 3 </h3>');
// document.getElementById('p1').innerHTML = '<h3>Header 33 </h3>';
// console.log('/////////////////////////////////');
// console.log($('#p1').html());
// console.log('/////////////////////////////////');
// console.log(document.getElementById('p1').innerHTML);

// Animaciones
// $('#p1').hide();
// document.getElementById('p1').style.display = 'none';

//Estilos css
// $('#p1').css('font-size', '25px');
document.getElementById('p1').style.fontSize = '25px';








