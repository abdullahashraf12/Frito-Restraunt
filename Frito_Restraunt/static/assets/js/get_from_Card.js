try {
    total_for_all_products =0.00
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
                    if(element.user_meal_type == "Default"){
                        total_for_all_products+=parseFloat(element.total_price_for_all)
                        $("#Add_Products_from_card_here").append(
                            `
                            <div class="card__Shopping_Card">
        <img src="${element.default_image}" alt="Product Image" class="card__Shopping_Card-image">
        <div class="card__Shopping_Card-content">
            <h2>${element.product_name}</h2>
            <p>Quantity ${element.quantity}</p>
            <p>Product Type & SideDishes & Beverages Included <b style="color:green;">(Default)</b></p>
        </div>
        <div class="card__Shopping_Card-price">
            <h5>Price <b style="color:red">${element.total_price_for_all} L.E</b></h5>
        </div>
    </div>    
                
           `
           
                        );
                    }else{
                        total_for_all_products+=parseFloat(element.total_price_for_all)
                        $("#Add_Products_from_card_here").append(
                            `
                            <div class="card__Shopping_Card">
        <img src="${element.default_image}" alt="Product Image" class="card__Shopping_Card-image">
        <div class="card__Shopping_Card-content">
            <h2>${element.product_name}</h2>
            <p style="">Product Type & SideDishes & Beverages & Quantity Included <b style="color:green;">(Special Order)</b></p>
        </div>
        <div class="card__Shopping_Card-price">
            <h5>Price <b style="color:red">${element.total_price_for_all} L.E</b></h5>
        </div>
    </div>
              
           `);
                    }



                        
                    }
                }
                $("#Add_Products_from_card_here").append(`<div style="display: flex; justify-content: space-between; padding-left: 10px; padding-right: 10px;">
    <h4>Total Price:</h4>
    <h5><b style="color:red; padding-right: 10px;">Price ${total_for_all_products} L.E</b></h5>
</div>
 `)
 $("#Add_Products_from_card_here").append("<button style='width:100%; height:50px; color: white; background-color:red; font-weight:bold;'>Checkout</button>");
 

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
