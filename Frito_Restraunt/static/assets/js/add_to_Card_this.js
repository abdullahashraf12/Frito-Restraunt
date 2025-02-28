$(document).ready(function() {


try{
    function display_message_success(){
        $("#message").html(`
            <div class="alert alert-success" role="alert">
            Product Has Been Added or (Modified) Sucessfully
            </div>
            `)
            setTimeout(function() {
                $("#message").empty();
            }, 2000);
    }
    function display_message_error(){
        $("#message").html(`
     <div class="alert alert-danger" role="alert">
  Error Happened
</div>
            `)
            setTimeout(function() {
                $("#message").empty();
            }, 2000);
    }
    function display_message_error_user_login(){
        $("#message").html(`
     <div class="alert alert-danger" role="alert">
  User Must Login First
</div>
            `)
            setTimeout(function() {
                $("#message").empty();
            }, 2000);
    }
    function get_from_Card(){
        const csrftoken = getCookie('csrftoken');
    
        $.ajax({
            type: 'GET',
            url: "/core/add-to-cart/",  // Update the URL here
            success: function(response) {
                console.log("Success:", response);
                if(response.error=="User Empty"){
                    $("#Add_Products_from_card_here").html("<h4 style='color:darkblue; font-weight:bolder; font-size=medium; text-align: center; '>Nothing To Show <h4>")
                    $("#Add_Products_from_card_here").append(`
                        <button style='width:100%; height:50px; color: white; background-color:blue; font-weight:bold;'>My Orders</button>
                        `)
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

         var offer_oid=null

        // Get the default checked radio button
        var defaultCheckedValue = $('input[name="radio_button"]:checked').val();
        var defaultCheckedOffer = $('input[name="radio_button"]:checked').data('custom-offer');
        // console.log("Default checked radio button value: " + defaultCheckedValue);
        // console.log("Default checked radio button data-custom-offer: " + defaultCheckedOffer);
        
        // Attach change event listener to radio buttons with name "radio_button"
        $('input[name="radio_button"]').change(function() {
            // Get the value of the checked radio button
            var checkedOffer = $('input[name="radio_button"]:checked').data('custom-offer');
            // Do something with the checked value
            // console.log("Checked radio button value: " + checkedValue);
            // console.log("Checked radio button data-custom-offer: " + checkedOffer);
            offer_oid = checkedOffer
        });
    
        // Check the default value if no change occurs
        $('input[name="radio_button"]').blur(function() {
            var checkedValue = $('input[name="radio_button"]:checked').val();
            var checkedOffer = $('input[name="radio_button"]:checked').data('custom-offer');
            if (checkedValue === undefined) {
                // console.log("Default checked radio button value: " + defaultCheckedValue);
                // console.log("Default checked radio button data-custom-offer: " + defaultCheckedOffer);
            }else{
                offer_oid = checkedOffer

            }
       

        });










        
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
                    if(response.error=="User Must Login To Add To Card"){
                        display_message_error_user_login();
                    }else{
                        get_from_Card();
                        display_message_success();
    
                    }


                },
                error: function(xhr, status, error) {
                    // Print the error to the browser console
                    console.log('Error adding product to cart:', xhr.responseText);
                    display_message_error();
                }
            });
        });
        $('#add-to-cart-form-Special-Order').on('submit', function(event) {
            event.preventDefault(); // Prevent the default form submission
            let checkedValues_items_for_MealType = [];
            let checkedValues_items_for_Side_Dishes = [];
            let checkedValues_items_for_Products_Additions = [];
            var defaultCheckedOffer = $('input[name="radio_button"]:checked').data('custom-offer');

            $('input[type="checkbox"][data-custom^="checkbox_in_product_Meal_TYPE_"]').each(function() {
                if ($(this).is(':checked')) {
                    let meal_imga = $(this).closest('li').find('img[name="ProductMealType_image"]');
                    let src_value = meal_imga.attr('src');
                    let quantityInput = $(this).closest('div').next('div').find('input[data-custom-productmealtype-quantity]');
                    let quantity = quantityInput.val();
                    // alert(quantity)
                    // Add the data-custom attribute value to the array
                    checkedValues_items_for_MealType.push({
                        
                        // custom: $(this).attr('data-custom'),
                        product_meal_type: $(this).attr('data-custom-product_Meal_TYPE-name'),
                        price:$(this).attr('data-custom-addtition-price'),
                        quantity:quantity,
                        mealtype:src_value
                    });
                }
             });
            


             $('input[type="checkbox"][data-custom^="checkbox_in_product_SIDE_DISH_"]').each(function() {


                if ($(this).is(':checked')) {
                    let sid_imga = $(this).closest('li').find('img[name="ProductSideDish_image"]');
                    let src_value = sid_imga.attr('src');

                    let quantityInput = $(this).closest('div').next('div').find('input[data-custom-ProductSideDish-quantity]');
                    let quantity = quantityInput.val();

                    // Add the data-custom attribute value to the array
                    checkedValues_items_for_Side_Dishes.push({
                        // custom: $(this).attr('data-custom'),
                        product_side_dish: $(this).attr('data-custom-product_SIDE_DISH-name'),
                        price:$(this).attr('data-custom-addtition-price'),
                        quantity:quantity,
                        side_image:src_value
                    });
                }
             });



             $('input[type="checkbox"][data-custom^="checkbox_in_ProdutsAdditions_"]').each(function() {
                if ($(this).is(':checked')) {
                    let addition_imga = $(this).closest('li').find('img[name="ProdutsAdditions_image"]');
                    let src_value = addition_imga.attr('src');


                    let quantityInput = $(this).closest('div').next('div').find('input[data-custom-addtition-quantity]');
                    let quantity = quantityInput.val();
                    
                    // Add the data-custom attribute value to the array
                    checkedValues_items_for_Products_Additions.push({
                        // custom: $(this).attr('data-custom'),
                        additionName: $(this).attr('data-custom-addtition-name'),
                        price:$(this).attr('data-custom-addtition-price'),
                        quantity:quantity,
                        addition_image:src_value
                    });
                }
             });

             $.ajax({
                type: 'POST',
                url: $(this).attr('action'), // Get the form action URL dynamically
                data: {
                    pid: $('[name="product_pid_to_card"]').val(),
                    mealType: JSON.stringify(checkedValues_items_for_MealType),
                    sideDishtype: JSON.stringify(checkedValues_items_for_Side_Dishes),
                    prductAdditionstype: JSON.stringify(checkedValues_items_for_Products_Additions), 
                    offer_oid:defaultCheckedOffer,
                    prod_ven:"Special Order",
                },
                headers: {
                    'X-CSRFToken': csrftoken
                },
                success: function(response) {
                    if(response.error=="User Must Login To Add To Card"){
                        display_message_error_user_login();
                    }else{
                        get_from_Card();
                        display_message_success();
    
                    }

                },
                error: function(xhr, status, error) {
                    // Print the error to the browser console
                    console.log('Error adding product to cart:', xhr.responseText);
                    display_message_error();
                }
            });
        


                // Get the default checked radio button
       
                // Attach change event listener to radio buttons with name "radio_button"

            



            //  console.log(checkedValues_items_for_MealType);
            //  console.log(checkedValues_items_for_Side_Dishes);
            //  console.log(checkedValues_items_for_Products_Additions);
        });
    }catch(err){

    }
    });
  