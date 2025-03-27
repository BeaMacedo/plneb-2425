function delete_conceito(designation){  //função delete conceito que recebe designacao como parametro
    $.ajax( "/conceitos/"+ designation, {            //$ que permite ir buscar o ajax, ferramenta de java script que permite fazer http request. 
        type:"DELETE",      //Recebe a rota e junta um conceito. Vamos fazer delete
        success: function(data){
            console.log(data) //se correr bem mostra o resultado
            if (data["success"]){
                window.location.href = data["redirect_url"]
            }
        },
        error: function(error) {
            console.log(error)      //para mostrar o erro
        }

    })

}

//a de cima é uma função, só executa quando se carrega num botão

$(document).ready( function () {
    $('#tabela_conceitos').DataTable({
        search: {
            regex: true
        },
    });     //o id (#) da tabela é tabela_conceitos
} );
