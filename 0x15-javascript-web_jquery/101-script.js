$('#add_item').click(function() {
    const newitem = $("<li>Item</li>");
    $('UL.my_list').append(newitem);
});
$('#remove_item').click(function() {
    $("UL.my_list li:last-child").remove();
});

$('#clear_list').click(function() {
    $("UL.my_list").empty();
});
