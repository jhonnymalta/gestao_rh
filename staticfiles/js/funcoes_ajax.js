function registrar_ponto(){

    token = document.querySelector('[name=csrfmiddlewaretoken]').value;

    $.ajax({
    type: 'POST',
    url: 'registro-ponto/registrar/',
    data:{
     csrfmiddlewaretoken: token
    },
    success: function(result){
        console.log("sucesso");
        $('#msg_retorno').text('Registrado com sucesso teste')
    }
    })
}