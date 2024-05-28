$(document).ready(function() {
    $(document).on("click", "a[name='add_to_wishcard']", function(event) {
        event.preventDefault(); // Prevent the default behavior of the button click event
        
        var form = $(this).closest('form');
        var email = $("#email_exist").val(); // Function to get the CSRF token from the cookie

        if (!email || !email.trim() || !email.match(/^[^\s@]+@[^\s@]+\.[^\s@]+$/)) {
            alert("You Cannot Add To Card Please LogIn First");
        } else {
            var csrftoken = getCookie('csrftoken');
            var sizeList ="";
            var activeOption =""
            var activatedOption ="";
            var form = event.target.closest('form');
            var inputValue = form.querySelector('input[name="product_pid_to_card"]').value;
            
                $.ajax({
                    url: "/wishlist_Add/",
                    method: "POST",
                    data: {
                        pid: inputValue,
   
                    },
                    dataType: 'json',
                    beforeSend: function(xhr) {
                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
                        console.log("Adding Products to Card")
                    },
                    success: function(response2) {

                        console.log("product added or modified");
                        $("#Add_To_Prod_wish_list_Status").empty();
    
                        // Set the HTML for the alert
                        $("#Add_To_Prod_wish_list_Status").html('<div class="alert alert-success" style="margin-left: 100px; width: 800px;" role="alert">Product Has Been Added To WishList!</div>');
    
                        // Set a timeout to remove the alert after 2.5 seconds
                        setTimeout(function() {
                            $("#Add_To_Prod_wish_list_Status").empty();
                        }, 2500); // 2500 milliseconds = 2.5 seconds
                    },
                    error: function(xhr, textStatus, errorThrown) {
                        // var errorResponse = JSON.parse(xhr.responseText);
                        // alert(errorResponse.error); // Log the specific error message
                        alert(xhr.responseText)
                        $("#Add_To_Prod_wish_list_Status").empty();
    
                        $("#Add_To_Prod_wish_list_Status").html('<div class="alert alert-danger" role="alert" style="margin-left: 800px; width: 500px;>Error Has Happened '+errorResponse+'!</div>');
    
                        // Set a timeout to remove the alert after 2.5 seconds
                        setTimeout(function() {
                            $("#Add_To_Prod_wish_list_Status").empty();
                        }, 2500); 
                    }
                });
  
        }
    });
});

// Function to retrieve CSRF token from the cookie
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
