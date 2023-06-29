/*FUNCIONES PARA CARGAR HTML*/

function cargarHTML(pagina){

    var elemento = document.getElementById("contenedor_inicio");
    elemento.innerHTML = "";

    var rutaHTML = `${pagina}`
    console.log(rutaHTML);
    console.log("Hola");

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if(this.readyState == 4 && this.status == 200 && rutaHTML == "") {
            var contenidoHTML = this.responseText;
            var inicio = document.createElement('div');
            inicio.innerHTML = contenidoHTML;
            var contenidoIndex = inicio.querySelector('#contenedor_inicio').innerHTML;

            var contenedor = document.getElementById('contenido');
            contenedor.innerHTML = contenidoIndex;
            }
        else if(this.readyState == 4 && this.status == 200){
            document.getElementById("contenido").innerHTML = this.responseText;
        }
        };
        xhttp.open("GET",rutaHTML, true);
        xhttp.send();
    }




