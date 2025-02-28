// Function to get the number of gold stars by div ID
function getGoldStarsById() {
    var goldstarn_num=0
   // Loop through each div and get the number of gold stars
for (let i = 1; i <= 7; i++) {
    var goldstarn= $('#div_' + i).hasClass('gold') ? parseInt($('#div_' + i).attr('class').split('gold-')[1]) : 0;
    console.log(`Gold stars for div_${i}: ${goldstarn_num}`);
    if(goldstarn == 0){

    }else{
        goldstarn_num+=1
    }
}

    return goldstarn_num;
}
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Example usage:



$(document).ready(function() {
    $(document).on("click", "button[name='submit_client_review']", function(event) {
        event.preventDefault();
        var numberStars= getGoldStarsById() 
        var numberStars= getGoldStarsById() 
        var csrftoken = getCookie('csrftoken');
        var pidValue = $('input[name="pid"]').attr('id');
        var comment = $("#comment_id").val();
        var textareaValue = comment.trim();
        var minLength= 25;
        if ((textareaValue.length > minLength) && (comment !== '') && (numberStars != 0)) { 
        
            $.ajax({
                url: "/commentProduct/",
                method: "POST",
                data: {
                    stars: numberStars,
                    comment: comment,
                    pid:pidValue
                },
                dataType: 'json',
                beforeSend: function(xhr) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                    console.log("Adding Products to Card")
                },
                success: function(response2) {
                    console.log("Review added or modified");
                    // $("#Add_To_Prod_Status").empty();
    
                    // // Set the HTML for the alert
                    // $("#Add_To_Prod_Status").html('<div class="alert alert-success" style="margin-left: 100px; width: 800px;" role="alert">Product Has Been Added Or Modified Sucessfully!</div>');
    
                    // Set a timeout to remove the alert after 2.5 seconds
                    setTimeout(function() {
                        $("#Add_To_Prod_Status").empty();
                    }, 2500); // 2500 milliseconds = 2.5 seconds
                },
                error: function(xhr, textStatus, errorThrown) {
                    var errorResponse = JSON.parse(xhr.responseText);
                    // alert(errorResponse.error); // Log the specific error message
                    console.log(errorResponse)
                    // $("#Add_To_Prod_Status").empty();
    
                    // $("#Add_To_Prod_Status").html('<div class="alert alert-danger" role="alert" style="margin-left: 800px; width: 500px;>Error Has Happened '+errorResponse+'!</div>');
    
                    // Set a timeout to remove the alert after 2.5 seconds
                    setTimeout(function() {
                        $("#Add_To_Prod_Status").empty();
                    }, 2500); 
                }
            });
        
        
        
        
        }
        else{
            alert("empty or your words not enough Put at least 25 letters and stars must be checked");


        }
    
    
    })})