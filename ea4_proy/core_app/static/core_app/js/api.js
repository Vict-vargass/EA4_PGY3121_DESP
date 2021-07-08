$(document).ready(function(){
    //INICIALIZA VARIABLE CONTENEDOR PARA USAR EMPTY
    var contenedor=$('#contenedor');
    contenedor.empty();
    //VARIABLES
    var nombreArtista="";
    var tokenAsignado="";
    //REVISA SI EL CAMPO ESTA COMPLETO, MANDA UNA ALERTA QUE MARCA EL CAMPO INCOMPLETO Y OTORGA EL VALOR A LA VARIABLE INICIALIZADA
    $('#nombreArtista').blur(function(){
        if ($('#nombreArtista').val()==""){
            $('#nombreArtista').addClass('alerta');
            $("#traerSpotify").prop('disabled', true);   
        }else{
            $('#nombreArtista').removeClass('alerta');
            $("#traerSpotify").prop('disabled', false);
            nombreArtista=$('#nombreArtista').val();
        }
    })
    //REVISA SI EL CAMPO ESTA COMPLETO, MANDA UNA ALERTA QUE MARCA EL CAMPO INCOMPLETO Y OTORGA EL VALOR A LA VARIABLE INICIALIZADA
    $('#token').blur(function(){
        if($('#token').val()==""){
            $('#token').addClass('alerta');
            $("#traerSpotify").prop('disabled', true);
        }else{
            $('#token').removeClass('alerta');
            $("#traerSpotify").prop('disabled', false);
            tokenAsignado=$('#token').val();
        }
    })
    //COMPRUEBA CAMPOS Y DESACTIVA BOTON SI ESTAN VACIOS
    $('#traerSpotify').hover(function(){
        if(tokenAsignado==""||nombreArtista==""){
            $("#traerSpotify").prop('disabled', true);
        }else{
            $("#traerSpotify").prop('disabled', false);
        }
    })
    //TRAE API DE SPOTIFY
    $('#traerSpotify').click(function(){
        artista=nombreArtista;
        token=tokenAsignado;
        $.get({
            url: 'https://api.spotify.com/v1/artists/' + artista +'/albums',
            headers: {
                Authorization: 'Bearer ' + token
            },
            success: function(respuestaOK){
                $.each(respuestaOK.items, function(indice, album){
                    contenedor.append("<div class='card'>" +
                    "<img src='" + album.images[1].url + "' class='card-img-top max-tam-img' alt='" + album.name + "'>" +
                    "<div class='card-body'>"+
                    "<h5 class='card-title'>" + album.name + "</h5>" +
                    "<p class='card-text'><b>Lanzamiento: </b>" + album.release_date + "<br>"+album.external_urls[1]+"</p>"+
                "</div></div>")
                })

            },
            error: function(respuestaError){
                console.error(respuestaError);
            }
        })
    })
    //LIMPIA EL CAMPO NOMBRE, CLASES Y CONSERVA EL TOKEN
    $('#btnLimpiar').click(function(){
        contenedor.empty();
         $('#nombreArtista').val("").removeClass('alerta');
         $('#token').removeClass('alerta');
         $("#traerSpotify").prop('disabled', false);
    })
})//fin document ready{
