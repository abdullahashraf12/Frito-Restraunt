try{
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
            let checkedValues_items_for_MealType = [];
            let checkedValues_items_for_Side_Dishes = [];
            let checkedValues_items_for_Products_Additions = [];

            
            $('input[type="checkbox"][data-custom^="checkbox_in_product_Meal_TYPE_"]').each(function() {
                if ($(this).is(':checked')) {
                    let quantityInput = $(this).closest('div').next('div').find('input[data-custom-productmealtype-quantity]');
                    let quantity = quantityInput.val();
                    // Add the data-custom attribute value to the array
                    checkedValues_items_for_MealType.push({
                        custom: $(this).attr('data-custom'),
                        product_meal_type: $(this).attr('data-custom-product_Meal_TYPE-name'),
                        price:$(this).attr('data-custom-addtition-price'),
                        quantity:quantity
                    });
                }
             });
            




             $('input[type="checkbox"][data-custom^="checkbox_in_product_SIDE_DISH_"]').each(function() {
                if ($(this).is(':checked')) {
                    let quantityInput = $(this).closest('div').next('div').find('input[data-custom-ProductSideDish-quantity]');
                    let quantity = quantityInput.val();
                    // Add the data-custom attribute value to the array
                    checkedValues_items_for_Side_Dishes.push({
                        custom: $(this).attr('data-custom'),
                        product_side_dish: $(this).attr('data-custom-product_SIDE_DISH-name'),
                        price:$(this).attr('data-custom-addtition-price'),
                        quantity:quantity
                    });
                }
             });







             $('input[type="checkbox"][data-custom^="checkbox_in_ProdutsAdditions_"]').each(function() {
                if ($(this).is(':checked')) {
                    let quantityInput = $(this).closest('div').next('div').find('input[data-custom-addtition-quantity]');
                    let quantity = quantityInput.val();
                    // Add the data-custom attribute value to the array
                    checkedValues_items_for_Products_Additions.push({
                        custom: $(this).attr('data-custom'),
                        additionName: $(this).attr('data-custom-addtition-name'),
                        price:$(this).attr('data-custom-addtition-price'),
                        quantity:quantity
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
                    prod_ven:"Special Order"
                },
                headers: {
                    'X-CSRFToken': csrftoken
                },
                success: function(response) {
                    console.log(checkedValues_items_for_MealType);
                    console.log(checkedValues_items_for_Side_Dishes);
                    console.log(checkedValues_items_for_Products_Additions);
       
                    // Print the JSON response to the browser console
                    console.log(response);
                },
                error: function(xhr, status, error) {
                    // Print the error to the browser console
                    console.log('Error adding product to cart:', xhr.responseText);
                }
            });
        








            //  console.log(checkedValues_items_for_MealType);
            //  console.log(checkedValues_items_for_Side_Dishes);
            //  console.log(checkedValues_items_for_Products_Additions);

            });
        });
        // Serialize the form data
            // var formData = $(this).serialize();

            // // Send an AJAX request
            // $.ajax({
            //     type: 'POST',
            //     url: $(this).attr('action'), // Get the form action URL dynamically
            //     data: formData,
            //     headers: {
            //         'X-CSRFToken': csrftoken
            //     },
            //     success: function(response) {
            //         // Print the JSON response to the browser console
            //         console.log(response);
            //     },
            //     error: function(xhr, status, error) {
            //         // Print the error to the browser console
            //         console.log('Error adding product to cart:', xhr.responseText);
            //     }
            // });















        }catch(err){
            console.log(err);
        }




