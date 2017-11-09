/**
 * Here you'll write code to make a GET request to your API
 */
function displayData(data) {
  // render data somewhere in website
  Object.keys(data).some(function(key, idx) {

    $('div#put-stuff-here').append('<p>' + key + '</p>');
  });
}

$.getJSON("/my-route", displayData);


/**
 * This code will send the POST request to the server with a variable number
 * of fields, depending on whether the user selects 2, 3, or 4 key/value 
 * pairs. 
 */
function handleSubmission(data) {

    // Create an object we'll send to the server's /post-route.
    var postObj = {};
    console.log('in here');

    // Append each adlib to the input object.
    for (var i=1; i <= 3; i++) {
        var key = "ad" + i;
        postObj[key] = $("#" + key).val();
    }

    // Make POST request to the server; log server response to console;
    $.post('/post-route', postObj, data => console.log(data));
}

$("#post-data-button").click(handleSubmission);

