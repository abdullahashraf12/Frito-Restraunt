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


function myFunction() {
    $.ajax({
        url: "/add_to_card/",
        method: "GET",
        data: {},
        dataType: 'json',
        beforeSend: function(xhr) {
            // Code to run before the request is sent
        },
        success: function(response2) {
            try {
                var csrftoken = getCookie('csrftoken');

                var userOrderCards = JSON.parse(response2.prod_card);
                $("ul[name=Shopping_card]").empty();
                $("span[name=number_of_products_in_card]").html(userOrderCards.length);
                var price =0;
                const csrftoken = getCookie('csrftoken');

                for (var i = 0; i < userOrderCards.length; i++) {
                    var userOrderCard = userOrderCards[i];
                    console.log(userOrderCard);
                    console.log(userOrderCard.uoc_prod__image.url);
                    price += parseFloat(userOrderCard.uoc_prod__price); // Use parseFloat to ensure proper addition
                    var liHtml = '<li>' +
                    '<div class="shopping-cart-img">' +
                    '<a href="/get_products/' + userOrderCard.uoc_prod__pid + '"><img alt="Nest" src="/media/' + userOrderCard.uoc_prod__image + '" /></a>' +
                    '</div>' +
                    '<div class="shopping-cart-title">' +
                    '<h4><a href="/get_products/' + userOrderCard.uoc_prod__pid + '">' + userOrderCard.uoc_prod__title + '</a></h4>' +
                    '<h4><span>' + userOrderCard.qty + ' × </span>' + userOrderCard.weight + '</h4>' +
                    '</div>' +
                    '<div class="shopping-cart-delete">' +
                    '<form class="delete-form" data-pid="' + userOrderCard.uoc_prod__pid + '">' +
                    '<input type="hidden" name="csrfmiddlewaretoken" value="' + csrftoken + '">' +
                
                    '<button type="button" class="delete-button" style="background-color: red; ' +
                    'border: 1px solid red; ' +
                    'color: #fff; ' +
                    'font-size: 16px; ' +
                    'cursor: pointer; ' +
                    'border-radius: 4px;  ' +
                    'transition: background-color 0.3s ease;  border-radius: 100%; ">X</button>' +
                
                    '</form>' +
                    '</div>' +
                    '</li>';
                

                
                    $('ul[name=Shopping_card]').append(liHtml);
                }
                $("span[name=total_product_price_card]").empty()
                $("span[name=total_product_price_card]").html("$"+price.toString())
            } catch (error) {
                console.error("Error parsing response:", error);
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



// Check if the user agent string contains any mobile-related keywords

if (isMobile) {
    try{
    myFunction()
    console.log("The client is using a mobile device.");

    }catch(error){

    }
    // The client is accessing the website from a mobile device
} else {
    try{

    // The client is accessing the website from a non-mobile device
    setInterval(myFunction, 1000);
    console.log("The client is not using a mobile device.");
}catch(error){

}
}
