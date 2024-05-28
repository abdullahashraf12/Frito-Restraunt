$(document).ready(function() {
    // Attach event handler to a parent element and delegate it to .delete-button elements
    $(document).on("click", ".delete-button_wish", function(event) {
        event.preventDefault(); // Prevent default button behavior

        var form = $(this).closest(".delete-form"); // Find the parent form
        var csrftoken = form.find('input[name="csrfmiddlewaretoken"]').val(); // Get CSRF token from the form
        var pid = form.data("pid"); // Get product ID from data attribute

        // Manually construct the AJAX request
        $.ajax({
            url: "/remove_from_wish/", // Correct URL
            method: "POST",
            headers: {"X-CSRFToken": csrftoken}, // Include CSRF token in the request header
            data: {csrfmiddlewaretoken: csrftoken, pid: pid}, // Include CSRF token and product ID in data
            dataType: 'json',
            success: function(response2) {
                // Handle success response if needed
                console.log(response2);
                // Remove the corresponding HTML element from the DOM
                form.closest('li').remove(); // Remove the parent li element of the form
            },
            error: function(xhr, textStatus, errorThrown) {
                var errorResponse = JSON.parse(xhr.responseText);
                alert(errorResponse.error); // Log the specific error message
            }
        });
    });
});
