/* 
1.- Crear el archivo util.js y crear las siguientes funciones
    2.obtenerUsuario()
    2.1- Crear un arreglo de apellidos y un arreglo de nombres, por ejemplo: 
        apellidos = ['Aguilar', 'Basurto', 'Fernández', 'Gómez', 'Juárez', 'Méndez', 'Malinalgo'];
        nombres = ['Ana', 'Armando', 'Carmen', 'Daniela', 'Ernesto', 'Francisco', 'Fernanda']; 
    2.2- Crear un diccionario con un nombre, apellido paterno, apellido materno y edad que sea aleatorio, 
         tomando en cuenta los datos del arreglo. 
         La instrucción Math.random regresa un número aleatorio entre 0 y 1
         La instrucción Math.round redondea a un entero
         El método  .length  regresa el tamaño de un arreglo 
    3.- regresar el diccionario
*/

function obtenerUsuario() {
    apellidos = ['Aguilar', 'Basurto', 'Fernández', 'Gómez', 'Juárez', 'Méndez', 'Malinalgo', 'Vázquez'];
    nombres = ['Ana', 'Armando', 'Carmen', 'Daniela', 'Ernesto', 'Francisco', 'Fernanda', 'Juliana', 'Julia', 'Julio', 'Miguel', 'Marcos']; 
    apPaterno = apellidos[Math.round(Math.random() * (apellidos.length - 1))];
    apMaterno = apellidos[Math.round(Math.random() * (apellidos.length - 1))];
    nombre = nombres[Math.round(Math.random() * (nombres.length - 1))];
    edad = Math.round(Math.random() * 50 + 15);
    usuario = {
        nombre:nombre,
        apPaterno:apPaterno,
        apMaterno:apMaterno,
        edad:edad
    };
    return usuario;
}