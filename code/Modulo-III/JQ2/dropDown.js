
/*
    ----------------------------------------------------------------------
    Condición                   | Mensaje       | Premio
    ---------------------------------------------------------------------
    Si la calificación >= 8     | Felicidades!  | Bicicleta / Patines
    Si la calificación >= 6     | Aprobado      | Patineta / Piñata
    Cualquier otro caso         | Reprobado     | No existan opciones

*/

$(function() {
    $('#selectCalificacion').change(obtieneMensaje); 
}); 


function obtieneMensaje() {
    $('#selectPremio').empty();
    $('#pDescripcion').text(""); 

    let calificacion =  Number($(this).val());
    if (calificacion == 8 || calificacion == 9 || calificacion == 10 ) {
        $('#pDescripcion').text("Felicidades!!!");  
        $('#selectPremio').append("<option value='Bicicleta'>Bicicleta</option>").
            append("<option value='Patines'>Patines</option>"); 
    } 
    if (calificacion < 8 && calificacion >= 6) {
        $('#pDescripcion').text("Aprobado");  
        $('#selectPremio').append("<option value='Patineta'>Patineta</option>").
            append("<option value='Piñata'>Piñata</option>")
    }
    
    if (calificacion < 6 && calificacion >= 0) {
        $('#pDescripcion').text("Reprobado");  
    }   
}



