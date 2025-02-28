// try {
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
//     const csrftoken = getCookie('csrftoken');

//     total_for_all_products =0.00
//     $.ajax({
//         type: 'GET',
//         url: "/core/add-to-cart/",  // Update the URL here
//         success: function(response) {
//             console.log("Success:", response);
//             if(response.error=="User Empty"){
//                 $("#Add_Products_from_card_here").html("<h4 style='color:darkblue; font-weight:bolder; font-size=medium; text-align: center; '>Nothing To Show <h4>")

//             } else if (response.success && Array.isArray(response.success) && response.success.length === 0) {
//                 $("#Add_Products_from_card_here").html("<h4 style='color:darkblue; font-weight:bolder; font-size=medium; text-align: center; '>Nothing To Show <h4>")
//                 let number_of_ordered_items = 0
//                 $("#number_of_ordered_items").html(number_of_ordered_items)


//             } else if (response.success && Array.isArray(response.success) && response.success.length > 0) {
//                 let number_of_ordered_items = response.success.length
//                 $("#number_of_ordered_items").html(number_of_ordered_items)
//                 $("#Add_Products_from_card_here").html("")
//                 for (const key in response.success) {
//                     if (response.success.hasOwnProperty.call(response.success, key)) {
//                         const element = response.success[key];
                    
//                         console.log("---------------------------")
//                         console.log(element)
//                         console.log("---------------------------")
//                     if(element.user_meal_type == "Default"){
//                         total_for_all_products+=parseFloat(element.total_price_for_all)
//                         $("#Add_Products_from_card_here").append(
//                             `
//                             <div class="card__Shopping_Card" style="position: relative;">
//                                 <form style="position: absolute; top: 2px; right: 2px;" method="POST" class="remove-from-card-form">
//                                     <input type="hidden" name="csrfmiddlewaretoken" value="${csrftoken}">
//                                     <input type="hidden" name="product_type_def_special" value="${element.user_meal_type}">

//                                     <input type="hidden" name="product_id_remove_from_button" value="${element.uoc_prod_id}">
//                                     <button type="submit" class="remove-from-card-button" style="padding: 10px; background-color: red; color: white; border: 1px solid transparent; font-weight: bold; font-size: 15px;">X</button>
//                                 </form>

//                                 <img src="${element.default_image}" alt="Product Image" class="card__Shopping_Card-image">
//                                 <div class="card__Shopping_Card-content">
//                                     <h2>${element.product_name}</h2>
//                                     <p>Quantity ${element.quantity}</p>
//                                     <p>Product Type & SideDishes & Beverages Included <b style="color:green;">(Default)</b></p>
//                                 </div>
//                                 <div class="card__Shopping_Card-price">
//                                     <h5>Price <b style="color:red">${element.total_price_for_all} L.E</b></h5>
//                                 </div>
//                             </div>    
//                             `
//                         );
                        
                        
//                     }else{
//                         total_for_all_products+=parseFloat(element.total_price_for_all)
//                         $("#Add_Products_from_card_here").append(
//                             `
//                             <div class="card__Shopping_Card" style="position: relative;">
//                                 <form style="position: absolute; top: 2px; right: 2px;" method="POST" class="remove-from-card-form">
//                                     <input type="hidden" name="csrfmiddlewaretoken" value="${csrftoken}">
//                                     <input type="hidden" name="product_type_def_special" value="${element.user_meal_type}">

//                                     <input type="hidden" name="product_id_remove_from_button" value="${element.uoc_prod_id}">
//                                     <button type="submit" class="remove-from-card-button" style="padding: 10px; background-color: red; color: white; border: 1px solid transparent; font-weight: bold; font-size: 15px;">X</button>
//                                 </form>

//                                 <img src="${element.default_image}" alt="Product Image" class="card__Shopping_Card-image">
//                                 <div class="card__Shopping_Card-content">
//                                     <h2>${element.product_name}</h2>
//                                     <p>Product Type & SideDishes & Beverages & Quantity Included <b style="color:green;">(Special Order)</b></p>
//                                 </div>
//                                 <div class="card__Shopping_Card-price">
//                                     <h5>Price <b style="color:red">${element.total_price_for_all} L.E</b></h5>
//                                 </div>
//                             </div>
//                             `
//                         );
                        
//                     }



                        
//                     }
//                 }
//                 $("#Add_Products_from_card_here").append(`<div style="display: flex; justify-content: space-between; padding-left: 10px; padding-right: 10px;">
//     <h4>Total Price:</h4>
//     <h5><b style="color:red; padding-right: 10px;">Price ${total_for_all_products} L.E</b></h5>
// </div>
//  `)
//  $("#Add_Products_from_card_here").append("<button style='width:100%; height:50px; color: white; background-color:red; font-weight:bold;'>Checkout</button>");
 

//                 // Handle the response data here
//                 console.log("Response success:", response.success);
//                 // Further processing of response data
//             } else {
//                 // Handle other possible cases or errors
//                 console.log("Unexpected response structure:", response);
//             }
//             // Handle the response data here
//         },
//         error: function(xhr, status, error) {
//             console.log('Error adding product to cart:', error);
//             // Log the error details
//         }
//     });
// } catch(error) {
//     console.log('Caught an error:', error);
//     // Log any unexpected errors
// }
function get_from_Card(){
    const csrftoken = getCookie('csrftoken');

    $.ajax({
        type: 'GET',
        url: "/core/add-to-cart/",  // Update the URL here
        success: function(response) {
            console.log("Success:", response);
            if(response.error=="User Empty"){
                $("#Add_Products_from_card_here").html("<h4 style='color:darkblue; font-weight:bolder; font-size=medium; text-align: center; '>Nothing To Show <h4>")
               
            } else if (response.success && Array.isArray(response.success) && response.success.length === 0) {
                $("#Add_Products_from_card_here").html("<h4 style='color:darkblue; font-weight:bolder; font-size=medium; text-align: center; '>Nothing To Show <h4>")
                $("#Add_Products_from_card_here").append(`
                    <form method="GET" action="/core/my_orders">
                    <button type="submit" style='width:100%; height:50px; color: white; background-color:blue; font-weight:bold;'>My Orders</button>
                    </form>
                    `)
                let number_of_ordered_items = 0
                $("#number_of_ordered_items").html(number_of_ordered_items)
                total_for_all_products=0.00


            } else if (response.success && Array.isArray(response.success) && response.success.length > 0) {
                let number_of_ordered_items = response.success.length
                $("#number_of_ordered_items").html(number_of_ordered_items)
                $("#Add_Products_from_card_here").html("")
                total_for_all_products=0.00
                for (const key in response.success) {
                    if (response.success.hasOwnProperty.call(response.success, key)) {
                        const element = response.success[key];
                    
                        console.log("---------------------------")
                        console.log(element.product_offers_id)
                        console.log(element.product_offers_id)
                        console.log(element.product_offers_id)
                        console.log(element.product_offers_id)
                        console.log(element.product_offers_id)
                        console.log(element.product_offers_id)
                        console.log("---------------------------")
                    if(element.user_meal_type == "Default"){
                        total_for_all_products+=parseFloat(element.total_price_for_all)
                        $("#Add_Products_from_card_here").append(
                            `
                            <div class="card__Shopping_Card" style="position: relative;">
                                <form style="position: absolute; top: 2px; right: 2px;" method="POST" class="remove-from-card-form">
                                    <input type="hidden" name="csrfmiddlewaretoken" value="${csrftoken}">
                                    <input type="hidden" name="product_type_def_special" value="${element.user_meal_type}">
                                        <input type="hidden" name="offer_type" value="${element.product_offers_id}">

                                    <input type="hidden" name="product_id_remove_from_button" value="${element.uoc_prod_id}">
                                    <button type="submit" class="remove-from-card-button" style="padding: 10px; background-color: red; color: white; border: 1px solid transparent; font-weight: bold; font-size: 15px;">X</button>
                                </form>

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
                            <div class="card__Shopping_Card" style="position: relative;">
                                <form style="position: absolute; top: 2px; right: 2px;" method="POST" class="remove-from-card-form">
                                    <input type="hidden" name="csrfmiddlewaretoken" value="${csrftoken}">
                                    <input type="hidden" name="product_type_def_special" value="${element.user_meal_type}">
                                        <input type="hidden" name="offer_type" value="${element.product_offers_id}">

                                    <input type="hidden" name="product_id_remove_from_button" value="${element.uoc_prod_id}">
                                    <button type="submit" class="remove-from-card-button" style="padding: 10px; background-color: red; color: white; border: 1px solid transparent; font-weight: bold; font-size: 15px;">X</button>
                                </form>

                                <img src="${element.default_image}" alt="Product Image" class="card__Shopping_Card-image">
                                <div class="card__Shopping_Card-content">
                                    <h2>${element.product_name}</h2>
                                    <p>Product Type & SideDishes & Beverages & Quantity Included <b style="color:green;">(Special Order)</b></p>
                                </div>
                                <div class="card__Shopping_Card-price">
                                    <h5>Price <b style="color:red">${element.total_price_for_all} L.E</b></h5>
                                </div>
                            </div>
                            `
                        );
                        
                    }



                        
                    }
                }
                $("#Add_Products_from_card_here").append(`<div style="display: flex; justify-content: space-between; padding-left: 10px; padding-right: 10px;">
    <h4>Total Price:</h4>
    <h5><b style="color:red; padding-right: 10px;">Price ${total_for_all_products} L.E</b></h5>
</div>
 `)
 $("#Add_Products_from_card_here").append("<form method='GET' action='/core/checkout' ><button style='width:100%; height:50px; color: white; background-color:red; font-weight:bold;'>Checkout</button></form>");

 $("#Add_Products_from_card_here").append(`
    <form method="GET" action="/core/my_orders">
    <button type="submit" style='width:100%; height:50px; color: white; background-color:blue; font-weight:bold;'>My Orders</button>
    </form>
    `)
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
}
get_from_Card();
// setInterval(get_from_Card, 1000);
