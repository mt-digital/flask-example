/**
 * Here you'll write code to make a GET request to your API
 */
function displayData(data) {
            // render data somewhere in website
            Object.keys(data).some(function(key, idx) {

              $('div#put-stuff-here').append('<p>' + key + '</p>');
            });
          }

$.getJSON("http://localhost:5000/my-route",
          displayData);
