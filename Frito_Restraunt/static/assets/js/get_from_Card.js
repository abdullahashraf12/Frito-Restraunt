try {
    $.ajax({
        type: 'GET',
        url: "/core/add-to-cart/",  // Update the URL here
        success: function(response) {
            console.log("Success:", response);
            if(response.error=="User Empty"){
                $("#Add_Products_from_card_here").html("<h4 style='color:darkblue; font-weight:bolder; font-size=medium; text-align: center; '>Nothing To Show <h4>")

            } else if (response.success && Array.isArray(response.success) && response.success.length === 0) {
                $("#Add_Products_from_card_here").html("<h4 style='color:darkblue; font-weight:bolder; font-size=medium; text-align: center; '>Nothing To Show <h4>")

            } else if (response.success && Array.isArray(response.success) && response.success.length > 0) {
                let number_of_ordered_items = response.success.length
                $("#number_of_ordered_items").html(number_of_ordered_items)
                $("#Add_Products_from_card_here").html("")
                for (const key in response.success) {
                    if (response.success.hasOwnProperty.call(response.success, key)) {
                        const element = response.success[key];
                        console.log("---------------------------")
                        console.log(element)
                        console.log("---------------------------")
    //                     $("#Add_Products_from_card_here").html(
    //                         `
    //                         <div class="card__Shopping_Card">
    //     <img src="img_avatar.png" alt="Product Image" class="card__Shopping_Card-image">
    //     <div class="card__Shopping_Card-content">
    //         <h2>Product Title</h2>
    //         <p>Product description goes here. This is where you can provide details about the product.</p>
    //     </div>
    //     <div class="card__Shopping_Card-price">
    //         <h5>Price <b style="color:red">150 L.E</b></h5>
    //     </div>
    // </div>                 
    //        `
    //                     );


                        
                    }
                }
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
// function run_every_Second(){
//     try {
//         $.ajax({
//             type: 'GET',
//             url: "/core/add-to-cart/",  // Update the URL here
//             success: function(response) {
//                 console.log("Success:", response);
//                 if(response.error=="User Empty"){
//                     $("#Add_Products_from_card_here").html("<h4 style='color:darkblue; font-weight:bolder; font-size=medium; text-align: center; '>Nothing To Show <h4>")
    
//                 } else if (response.success && Array.isArray(response.success) && response.success.length === 0) {
//                     $("#Add_Products_from_card_here").html("<h4 style='color:darkblue; font-weight:bolder; font-size=medium; text-align: center; '>Nothing To Show <h4>")
    
//                 } else if (response.success && Array.isArray(response.success) && response.success.length > 0) {
//                     let number_of_ordered_items = response.success.length
//                     $("#number_of_ordered_items").html(number_of_ordered_items)
//                     $("#Add_Products_from_card_here").html("")
//                     // Handle the response data here
//                     console.log("Response success:", response.success);
//                     // Further processing of response data
//                 } else {
//                     // Handle other possible cases or errors
//                     console.log("Unexpected response structure:", response);
//                 }
//                 // Handle the response data here
//             },
//             error: function(xhr, status, error) {
//                 console.log('Error adding product to cart:', error);
//                 // Log the error details
//             }
//         });
//     } catch(error) {
//         console.log('Caught an error:', error);
//         // Log any unexpected errors
//     }
// }

// setInterval(run_every_Second, 1000);
