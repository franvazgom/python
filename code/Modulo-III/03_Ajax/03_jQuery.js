$(function(){
    obtieneInformacion("1");
    $('#btnConsulta').click(function(){
        let textoBtn = $(this).text();
        if (textoBtn == "Página 2") {
            obtieneInformacion("2");
            $(this).text("Página 1");
        }else {
            obtieneInformacion("1");
            $(this).text("Página 2");
        }
    });
});

function obtieneInformacion(noPagina) {
    let url = "https://reqres.in/api/users?page=" + noPagina
    $.ajax({
        url:url,
        type:'GET',
        dataType:'json',
        success: function(data) {
            procesaInformacion(data.data);
        },
        error: function(xhr, status, error) {
            console.log(error);
        }
    });
}

function procesaInformacion(usuarios){
    $('#tarjetas').empty();
    let plantilla = '<div class="card">' +
        '<h3 class="card-title">titulo</h3>' + 
        '<img class="card-image" src=imagen>' + 
        '<div class="bodyCard">' +
        '<p class="card-description">parrafo</p>' + 
        '</div></div>'    

    $.each(usuarios, function(index, elemento){
        let tarjeta = plantilla.replace("titulo",
            elemento.first_name + ' ' + elemento.last_name);
        tarjeta = tarjeta.replace("imagen", elemento.avatar);
        tarjeta = tarjeta.replace("parrafo", elemento.email);
        $('#tarjetas').append(tarjeta);
    });
}