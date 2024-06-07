try {
    $.ajax({
        type: 'GET',
        url: "/core/add-to-cart/",  // Update the URL here
        success: function(response) {
            console.log("Success:", response);
            if(response.error=="User Empty"){
                alert("user not logged in ")
            } else if (response.success && Array.isArray(response.success) && response.success.length === 0) {
                alert("Error: Success array is empty");
            } else if (response.success && Array.isArray(response.success) && response.success.length > 0) {
                alert("Success: Success array is not empty");
                // Handle the response data here
                console.log("Response success:", response.success);
                // Further processing of response data
            } else {
                // Handle other possible cases or errors
                console.log("Unexpected response structure:", response);
            }
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
