   $(document).ready(function() {
    $.ajax({
        url: 'https://apis.digital.gob.cl/dpa/regiones',
        method: 'GET',
        dataType: 'json',
        cors: true,
        success: function(data) {
            data.forEach(function (region) {
                let regiones = $('<option>').text(region.nombre);
                $("#inputRegion").append(regiones);
            });
        },
        error: function(xhr, status, error) {
            console.log(error);
        }
    });
});
