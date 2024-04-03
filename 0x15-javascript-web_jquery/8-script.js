$.ajax( {
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    datatype: 'json',
    success: function(data) {
        $.each(data.results, function(index, movie) {
            $("#list_movies").append("<li>" + movie.title + "</li>");
        });
    }
});
