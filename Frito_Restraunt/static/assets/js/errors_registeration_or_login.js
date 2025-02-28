document.addEventListener('DOMContentLoaded', function() {
    var errorsDiv = document.getElementById("errors");

    // Get the JSON data from the data-errors attribute
    var errorsData = errorsDiv.getAttribute("data-errors");

    // Parse the JSON string into a JavaScript object
    var errorsObject = JSON.parse(errorsData);

    var alertContainer = document.getElementById('alert-container');
    var currentURL = window.location.href.toString();
    console.log(currentURL);
    
    var card = document.querySelector(".flip-card-inner");
    var accountError = errorsObject["error_account"];
    var passwordError = errorsObject["error_password"];
    console.log(accountError.toString())
    console.log(passwordError.toString())

    if ((currentURL.toString().includes("userauths/register") && accountError.toString()=="User Not Registered") || passwordError.toString()== "The two password fields didn’t match." ||accountError.toString() =="Enter a valid email address." ) {
        card.classList.toggle("flipped");
    }else{


    }

    try {
        $("#Register_Form").submit(function(event) {
            // Your validation code here
            var fileInput = $("#profile_picture")[0];
            var img = $("#upload_register_photo")[0];
            if (!fileInput.files || !fileInput.files.length) {
                img.focus(); // Ensure file input is focused
                img.click(); // Open file browser

                fileInput.addEventListener('change', function(event) {
                    const file = this.files[0];
                    if (file) {
                        const reader = new FileReader();
                        reader.onload = function(e) {
                            img.src = e.target.result;
                        };
                        reader.readAsDataURL(file);
                    }
                });

                // Prevent the default form submission
                event.preventDefault();
            } else {
                // If files are selected, submit the form
                $(this).unbind('submit').submit();
            }

        });


        for (var key in errorsObject) {
            if (errorsObject.hasOwnProperty(key)) {
                if (errorsObject[key]) {
                    console.log(key + " has a value:", errorsObject[key]);
                    var errorDiv = document.createElement('div');
                    errorDiv.setAttribute('class', 'alert alert-danger alert-dismissible fade show');
                    errorDiv.setAttribute('role', 'alert');
                    // errorDiv.setAttribute('style', 'width:250px; height:20px; background-color: rgba(248,215,218,255);   font-size: 18px;       ');

                    errorDiv.innerHTML = `
                        <a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>
                        <strong>Error:&nbsp;</strong>${errorsObject[key]}
                    `;
                    // Append error div to alert container
                    alertContainer.appendChild(errorDiv);
                } else {

                }
            }
        }

    } catch (err) {
        console.error(err);
        if (err.message.includes("An invalid form control with name='profile_picture' is not focusable")) {
            console.log("True");
        }
    }
});
