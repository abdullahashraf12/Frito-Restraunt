$(document).ready(function () {
    $("#Login_Form").submit(function(event) {
        var form = $(this); // Capture the reference to the form

        var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
        var emailValue = $("#email").val();
        var passwordValue = $("#password").val();
        // event.preventDefault();
        $.ajax({
            url: "fetch_img",
            type: 'POST', // The type of request (GET, POST, etc.)
            dataType: 'json', // The type of data we expect back
            data: {email: emailValue,password:passwordValue},
            headers: {
                'X-CSRFToken': csrfToken // Send the CSRF token in the request header
            },
            success: function(data) {
                console.log(data.img);
                $('#result').html(JSON.stringify(data));
                if(data.img!=""){
                    $("#Login_img").attr("src", data.img);
                    setTimeout(function() {
                        // Restore form attributes
                        form.attr('action', "/userauths/login");
                        form.attr('method', 'POST');
                        // form.unbind('submit').submit(); // Submit the form with original attributes after 2 seconds
                        $("#login_submit_button").click();

                    }, 1000);
                }
            },
            error: function(xhr, status, error) {
                // What to do if the request fails
                console.error('Error:', error);
                $('#result').html('An error occurred: ' + error);
            }
        });
    });

});

// $(document).ready(function () {

//    $("#Login_Form").submit(function(event) {
//     var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
//     var emailValue = $("#email").val();
//     event.preventDefault();
    
//     $.ajax({
//         url: "fetch_img",
//         type: 'POST', // The type of request (GET, POST, etc.)
//         dataType: 'json', // The type of data we expect back
//         data: {email: emailValue},
//         headers: {
//             'X-CSRFToken': csrfToken // Send the CSRF token in the request header
//         },
//         success: function(data) {
//             console.log(data.img);
//             $('#result').html(JSON.stringify(data));
//             if(data.img==""){

//             }else{
//                 $("#Login_img").attr("src", data.img);
//                 $(this).unbind('submit').submit();

//                 // runScript("/static/assets/js/errors_registeration_or_login.js")


//             }
            
//         },
//         error: function(xhr, status, error) {
//             // What to do if the request fails
//             console.error('Error:', error);
//             $('#result').html('An error occurred: ' + error);
//         }
//     });



//    })
//    function runScript(url) {
//     var script = document.createElement('script');
//     script.src = url;
//     document.head.appendChild(script);
// }
// });