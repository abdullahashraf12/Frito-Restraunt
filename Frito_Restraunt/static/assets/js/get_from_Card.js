try {
    $.ajax({
        type: 'GET',
        url: "/core/add-to-cart/",  // Update the URL here
        success: function(response) {
            console.log("Success:", response);
            // Handle the response data here
        },
        error: function(xhr, status, error) {
            console.log('Error adding product to cart:', error);
            // Log the error details
        }
    });
} catch(error) {
    console.log('Caught an error:', error);
    // Log any unexpected errors
}
