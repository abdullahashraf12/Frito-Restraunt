function myFunction() {
    $.ajax({
        url: "/wishlist_Add/",
        method: "GET",
        data: {},
        dataType: 'json',
        beforeSend: function(xhr) {
            // Code to run before the request is sent
        },
        success: function(response2) {
            try {
                var csrftoken = getCookie('csrftoken');
                console.log(response2);

                var userOrderCards = JSON.parse(response2.prod_card);
                console.log(userOrderCards);
                $("ul[name=Shopping_card_wish]").empty();
                $("span[name=number_of_products_in_card_wish]").html(userOrderCards.length);
                var price =0;
                for (var i = 0; i < userOrderCards.length; i++) {
                    console.log(userOrderCards[i].id)
                    var userOrderCard = userOrderCards[i];
                    // console.log(prod_card);
                    // console.log(userOrderCard.uoc_prod__image.url);
                    price += parseFloat(userOrderCard.product__price); // Use parseFloat to ensure proper addition
                    var liHtml = '<li>' +
                    '<div class="shopping-cart-img">' +
                    '<a href="/get_products/' + userOrderCard.product__pid + '"><img alt="Nest" src="/media/' + userOrderCard.product__image + '" /></a>' +
                    '</div>' +
                    '<div class="shopping-cart-title">' +
                    '<h4><a href="/get_products/' + userOrderCard.product__pid + '">' + userOrderCard.product__title + '</a></h4>' +
                    '</div>' +
                    '<div class="shopping-cart-delete">' +
                    '<form class="delete-form" data-pid="' + userOrderCard.product__pid + '">' +
                    '<input type="hidden" name="csrfmiddlewaretoken" value="' + csrftoken + '">' +
                
                    '<button type="button" class="delete-button_wish" style="background-color: red; ' +
                    'border: 1px solid red; ' +
                    'color: #fff; ' +
                    'font-size: 16px; ' +
                    'cursor: pointer; ' +
                    'border-radius: 4px;  ' +
                    'transition: background-color 0.3s ease;  border-radius: 100%; ">X</button>' +
                
                    '</form>' +
                    '</div>' +
                    '</li>';
                

                
                    $('ul[name=Shopping_card_wish]').append(liHtml);
                }
                $("span[name=total_product_price_card_wish]").empty()
                $("span[name=total_product_price_card_wish]").html("$"+price.toString())
            } catch (error) {
                console.log(error)
                // console.error("Error parsing response:", error);
            }
        },
        error: function(xhr, textStatus, errorThrown) {
            console.error("Error:", textStatus, errorThrown);
            if (xhr.responseText) {
                alert(xhr.responseText);
            }
        }
    });
}
// Function to retrieve CSRF token from the cookie
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

if (isMobile) {
    // The client is accessing the website from a mobile device
    try{

    myFunction()
    console.log("The client is using a mobile device.");
    }catch(error){

    }
} else {
    // The client is accessing the website from a non-mobile device
    try{

    setInterval(myFunction, 1000);
    console.log("The client is not using a mobile device.");
}catch(error){
        
}
    
}

