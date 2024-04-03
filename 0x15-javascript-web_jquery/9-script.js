$.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    method: 'GET',
    datatype: 'text',
    success: function(data) {
        $('#hello').text(data);
    },
});
