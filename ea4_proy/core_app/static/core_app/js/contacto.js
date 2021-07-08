$(document).ready(function(){
    //FUNCION QUE ESTABLECE EL RUT SELECCIONADO, ASEGURA PONER EL INPUT CORRESPONDIENTE
    $('#rut').html(function(){
        var agregaInput1= $('#rutPas')
        var seleccionado=$('#rut')
        agregaInput1.html('<input type="text" name="" id="rutPersona" class="form-control" placeholder="Ingrese su rut">');
        seleccionado.click();
    })
    // FUNCION PARA VOLVER AL INPUT ORIGINAL
    $('#rut').click(function(){
        var agregaInput2= $('#rutPas')
        agregaInput2.html('<input type="text" name="" id="rutPersona" class="form-control" placeholder="Ingrese su rut" maxlength="20">');
    })
    //FUNCION PARA CAMBIAR A INPUT PASAPORTE
    $('#pas').click(function(){
        var agregaInput3 = $('#rutPas')
        agregaInput3.html('<input type="text" name="" id="pasaporte" class="form-control" placeholder="Ingrese su pasaporte"  maxlength="20">')
    })
    //CONJUNTO QUE REVISA SI HAY VALORES EN LOS CAMPOS Y AGRUEGA CLASE ALERT, SI TIENE VALOR ELIMINA ALERT
    $('#nombreCompleto').blur(function(){
        if($('#nombreCompleto').val()==""){
            $('#nombreCompleto').addClass("alert")
        }else{
            $('#nombreCompleto').removeClass("alert")
        }
    })
    $('#email').blur(function(){
        if($('#email').val()==""){
            $('#email').addClass("alert")
        }
        else{
            $('#email').removeClass("alert")
        }
    })
    $('#rutPersona').blur(function(){
        if($('#rutPersona').val()==""){
            $('#rutPersona').addClass("alert")
        }else{
            $('#rutPersona').removeClass("alert")
        }
    })
    $('#pasaporte').blur(function(){
        if($('#pasaporte').val()==""){
            $('#pasaporte').addClass("alert")
        }else{
            $('#pasaporte').removeClass("alert")
        }
    })
    $('#ciudades').blur(function(){
        if($('#ciudades').val()==""){
            $('#ciudades').addClass("alert")
        }
        else{
            $('#ciudades').removeClass("alert")
        }
    })
    $('#textArea').blur(function(){
        if($('#textArea').val()==""){
            $('#textArea').addClass("alert")
        }
        else{
            $('#textArea').removeClass("alert")
        }
    })//FIN CONJUNTO
    
    //ENVIAR Y VALIDAR EL FORMULARIO
    $('#formularioContacto').submit(function(){ 
        var nombreCompleto=$('#nombreCompleto')
        var email= $('#email');
        var rut = $('#rutPersona');
        var pasaporte = $('#pasaporte');
        var ciudad = $('#ciudades');
        var mensaje = $('#textArea'); 
        if(nombreCompleto.val()==""){
            nombreCompleto.addClass('alert')
            event.preventDefault();
        }
        if(email.val()==""){
            email.addClass('alert');
            event.preventDefault();
        }
        if(rut.val()==""){
            rut.addClass('alert');
            event.preventDefault();
        }
        if(pasaporte.val()==""){
            pasaporte.addClass('alert');
            event.preventDefault();
        }
        if(ciudad.val()=="0"){
            ciudad.addClass('alert');
            event.preventDefault();
        }
        if(mensaje.val()==""){
            mensaje.addClass('alert');
            event.preventDefault();
        }
        //COMPRUEBA TODOS LOS CAMPOS Y PREVIENE EL ENVIO
        if(nombreCompleto.val()=="" || email.val()=="" || rut.val()=="" || pasaporte.val()=="" || ciudad.val()=="" || mensaje.val()==""){
            event.preventDefault();
            existe==false
        }else{
            alert("Formulario enviado correctamente")
        }
    })
    //LIMPIAR EL FORMULARIO
    $('#btnLimpiar').click(function(){
        var nombreCompleto=$('#nombreCompleto');
        var email= $('#email');
        var rut = $('#rutPersona');
        var pasaporte = $('#pasaporte');
        var celular = $('#nroCelular');
        var ciudad = $('#ciudades');
        var mensaje = $('#textArea');
        nombreCompleto.val("").removeClass("alert");
        email.val("").removeClass("alert");
        rut.val("").removeClass("alert");
        pasaporte.val("").removeClass("alert");
        celular.val("")
        ciudad.val(0).removeClass("alert");
        mensaje.val("").removeClass("alert");
    })

})