
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    const csrftoken = getCookie('csrftoken');

    $(document).ready(function() {
        $('#add-to-cart-form').on('submit', function(event) {
            event.preventDefault(); // Prevent the default form submission

            // Serialize the form data
            var formData = $(this).serialize();

            // Send an AJAX request
            $.ajax({
                type: 'POST',
                url: $(this).attr('action'), // Get the form action URL dynamically
                data: formData,
                headers: {
                    'X-CSRFToken': csrftoken
                },
                success: function(response) {
                    // Print the JSON response to the browser console
                    console.log(response);
                },
                error: function(xhr, status, error) {
                    // Print the error to the browser console
                    console.log('Error adding product to cart:', xhr.responseText);
                }
            });
        });
        $('#add-to-cart-form-Special-Order').on('submit', function(event) {
            event.preventDefault(); // Prevent the default form submission

            // Serialize the form data
            var formData = $(this).serialize();

            // Send an AJAX request
            $.ajax({
                type: 'POST',
                url: $(this).attr('action'), // Get the form action URL dynamically
                data: formData,
                headers: {
                    'X-CSRFToken': csrftoken
                },
                success: function(response) {
                    // Print the JSON response to the browser console
                    console.log(response);
                },
                error: function(xhr, status, error) {
                    // Print the error to the browser console
                    console.log('Error adding product to cart:', xhr.responseText);
                }
            });
        });























    });
