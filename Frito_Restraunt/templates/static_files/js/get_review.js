// // Function to get the number of gold stars by div ID
// function getGoldStarsById() {
//     var goldstarn_num=0
//    // Loop through each div and get the number of gold stars
// for (let i = 1; i <= 7; i++) {
//     var goldstarn= $('#div_' + i).hasClass('gold') ? parseInt($('#div_' + i).attr('class').split('gold-')[1]) : 0;
//     console.log(`Gold stars for div_${i}: ${goldstarn_num}`);
//     if(goldstarn == 0){

//     }else{
//         goldstarn_num+=1
//     }
// }

//     return goldstarn_num;
// }
function full_comment(star,review,date,username){
    var html = `
    <div class="single-comment justify-content-between d-flex mb-30">
        <div class="user justify-content-between d-flex">
            <div class="thumb text-center">
                <img src="/static/assets/imgs/blog/author-2.png" alt="" />
            </div>
            <div style="float:left;">
                <a href="#">${username}</a>
                <div class="d-flex align-items-center" style="margin-top: 5%; margin-left:2px;">
                    <span class="font-xs text-muted">${date}</span>
                </div>
                <div style="padding-left: 25px;">${review}</div>
            </div>
            <div style="float:left; margin-top:5px;">${star}</div>
        </div>
    </div>
`;

    return html;
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

function return_n_stars(number){
    if(number==0){
        return `
        <div  class="silver" style="float: left;">
        <label>
        <input  type="radio" name="rating" style="visibility:hidden"/>
    </label>
    </div>
    <div  class="silver" style="float: left;">
    <label>
    <input  type="radio" name="rating" style="visibility:hidden"/>
</label>
</div>
<div  class="silver" style="float: left;">
<label>
<input  type="radio" name="rating" style="visibility:hidden"/>
</label>
</div>
<div  class="silver" style="float: left;">
<label>
<input  type="radio" name="rating" style="visibility:hidden"/>
</label>
</div>
<div  class="silver" style="float: left;">
<label>
<input  type="radio" name="rating" style="visibility:hidden"/>
</label>
</div>
<div  class="silver" style="float: left;">
<label>
<input  type="radio" name="rating" style="visibility:hidden"/>
</label>
</div>
<div  class="silver" style="float: left;">
<label>
<input  type="radio" name="rating" style="visibility:hidden"/>
</label>
</div>
    
    `

    }else if(number==1){
        return `
        
        <div  class="gold" style="float: left;">
        <label>
        <input  type="radio" name="rating" style="visibility:hidden"/>
    </label>
</div>
<div  class="silver" style="float: left;">
<label>
<input  type="radio" name="rating" style="visibility:hidden"/>
</label>
</div>
<div  class="silver" style="float: left;">
<label>
<input  type="radio" name="rating" style="visibility:hidden"/>
</label>
</div>
<div  class="silver" style="float: left;">
<label>
<input  type="radio" name="rating" style="visibility:hidden"/>
</label>
</div>
<div  class="silver" style="float: left;">
<label>
<input  type="radio" name="rating" style="visibility:hidden"/>
</label>
</div>
<div  class="silver" style="float: left;">
<label>
<input  type="radio" name="rating" style="visibility:hidden"/>
</label>
</div>
<div  class="silver" style="float: left;">
<label>
<input  type="radio" name="rating" style="visibility:hidden"/>
</label>
</div>
        
        
        `
    }else if(number==2){
        return `
        
        <div  class="gold" style="float: left;">
        <label>
        <input  type="radio" name="rating" style="visibility:hidden"/>
    </label>
    </div>

    <div  class="gold" style="float: left;">
    <label>
    <input  type="radio" name="rating" style="visibility:hidden"/>
    </label>
    </div>
    <div  class="silver" style="float: left;">
<label>
<input  type="radio" name="rating" style="visibility:hidden"/>
</label>
</div>
<div  class="silver" style="float: left;">
<label>
<input  type="radio" name="rating" style="visibility:hidden"/>
</label>
</div>
<div  class="silver" style="float: left;">
<label>
<input  type="radio" name="rating" style="visibility:hidden"/>
</label>
</div>
<div  class="silver" style="float: left;">
<label>
<input  type="radio" name="rating" style="visibility:hidden"/>
</label>
</div>
<div  class="silver" style="float: left;">
<label>
<input  type="radio" name="rating" style="visibility:hidden"/>
</label>
</div>
        
        `
    }else if(number==3){
        return `
        
   <div  class="gold" style="float: left;">
        <label>
        <input  type="radio" name="rating" style="visibility:hidden"/>
    </label>
    </div>

    <div  class="gold" style="float: left;">
    <label>
    <input  type="radio" name="rating" style="visibility:hidden"/>
</label>
</div>
<div  class="gold" style="float: left;">
<label>
<input  type="radio" name="rating" style="visibility:hidden"/>
</label>
</div>
        
<div  class="silver" style="float: left;">
<label>
<input  type="radio" name="rating" style="visibility:hidden"/>
</label>
</div>
<div  class="silver" style="float: left;">
<label>
<input  type="radio" name="rating" style="visibility:hidden"/>
</label>
</div>
<div  class="silver" style="float: left;">
<label>
<input  type="radio" name="rating" style="visibility:hidden"/>
</label>
</div>
<div  class="silver" style="float: left;">
<label>
<input  type="radio" name="rating" style="visibility:hidden"/>
</label>
</div>

        `
    }else if(number==4){
        return `
   <div  class="gold" style="float: left;">
        <label>
        <input  type="radio" name="rating" style="visibility:hidden"/>
    </label>
    </div>
    <div  class="gold" style="float: left;">
    <label>
    <input  type="radio" name="rating" style="visibility:hidden"/>
</label>
</div>
<div  class="gold" style="float: left;">
<label>
<input  type="radio" name="rating" style="visibility:hidden"/>
</label>
</div>
<div  class="gold" style="float: left;">
<label>
<input  type="radio" name="rating" style="visibility:hidden"/>
</label>
</div>
<div  class="silver" style="float: left;">
<label>
<input  type="radio" name="rating" style="visibility:hidden"/>
</label>
</div>




<div  class="silver" style="float: left;">
<label>
<input  type="radio" name="rating" style="visibility:hidden"/>
</label>
</div>

<div  class="silver" style="float: left;">
<label>
<input  type="radio" name="rating" style="visibility:hidden"/>
</label>
</div>

<div  class="silver" style="float: left;">
<label>
<input  type="radio" name="rating" style="visibility:hidden"/>
</label>
</div>


        
        
        `
    }else if(number==5){
        return `
   <div  class="gold" style="float: left;">
        <label>
        <input  type="radio" name="rating" style="visibility:hidden"/>
    </label>
    </div>
    <div  class="gold" style="float: left;">
        <label>
        <input  type="radio" name="rating" style="visibility:hidden"/>
    </label>
    </div>
    <div  class="gold" style="float: left;">
        <label>
        <input  type="radio" name="rating" style="visibility:hidden"/>
    </label>
    </div>
    <div  class="gold" style="float: left;">
        <label>
        <input  type="radio" name="rating" style="visibility:hidden"/>
    </label>
    </div>
    <div  class="gold" style="float: left;">
        <label>
        <input  type="radio" name="rating" style="visibility:hidden"/>
    </label>
    </div>
    
    <div  class="silver" style="float: left;">
    <label>
    <input  type="radio" name="rating" style="visibility:hidden"  />
</label>
</div>

<div  class="silver" style="float: left;">
<label>
<input  type="radio" name="rating" style="visibility:hidden"  />
</label>
</div>

        
        
        `
    }else if(number==6){
        return `
        
    <div  class="gold" style="float: left;">
        <label>
        <input  type="radio" name="rating" style="visibility:hidden"  />
    </label>
    </div>


    <div  class="gold" style="float: left;">
    <label>
    <input  type="radio" name="rating" style="visibility:hidden"  />
</label>
</div>
<div  class="gold" style="float: left;">
<label>
<input  type="radio" name="rating" style="visibility:hidden"  />
</label>
</div>
<div  class="gold" style="float: left;">
<label>
<input  type="radio" name="rating" style="visibility:hidden"  />
</label>
</div>
<div  class="gold" style="float: left;">
<label>
<input  type="radio" name="rating" style="visibility:hidden"  />
</label>
</div>
<div  class="gold" style="float: left;">
<label>
<input  type="radio" name="rating" style="visibility:hidden"  />
</label>
</div>
<div  class="silver" style="float: left;">
<label>
<input  type="radio" name="rating" style="visibility:hidden"  />
</label>
</div>
        
        `
    }else if(number==7){
        return `
   <div  class="gold" style="float: left;">
        <label>
        <input  type="radio" name="rating" style="visibility:hidden"  />
    </label>
    </div>

    <div  class="gold" style="float: left;">
    <label>
    <input  type="radio" name="rating" style="visibility:hidden"  />
</label>
</div>
<div  class="gold" style="float: left;">
<label>
<input  type="radio" name="rating" style="visibility:hidden"  />
</label>
</div>
<div  class="gold" style="float: left;">
<label>
<input  type="radio" name="rating" style="visibility:hidden"  />
</label>
</div>
<div  class="gold" style="float: left;">
<label>
<input  type="radio" name="rating" style="visibility:hidden"  />
</label>
</div>
<div  class="gold" style="float: left;">
<label>
<input  type="radio" name="rating" style="visibility:hidden"  />
</label>
</div>
<div  class="gold" style="float: left;">
<label>
<input  type="radio" name="rating" style="visibility:hidden"  />
</label>
</div>
        
        
        `
    }
    return `
   <div  class="silver" style="float: left;">
        <label>
        <input  type="radio" name="rating" style="visibility:hidden"  />
    </label>
    </div>
     <div  class="silver" style="float: left;">
        <label>
        <input  type="radio" name="rating" style="visibility:hidden"  />
    </label>
    </div>
     <div  class="silver" style="float: left;">
        <label>
        <input  type="radio" name="rating" style="visibility:hidden"  />
    </label>
    </div>
     <div  class="silver" style="float: left;">
        <label>
        <input  type="radio" name="rating" style="visibility:hidden"  />
    </label>
    </div>
     <div  class="silver" style="float: left;">
        <label>
        <input  type="radio" name="rating" style="visibility:hidden"  />
    </label>
    </div>
     <div  class="silver" style="float: left;">
        <label>
        <input  type="radio" name="rating" style="visibility:hidden"  />
    </label>
    </div>
     <div  class="silver" style="float: left;">
        <label>
        <input  type="radio" name="rating" style="visibility:hidden"  />
    </label>
    </div>


    
    `

}

function myFunction(){
$(document).ready(function() {
    // $(document).on("click", "button[name='submit_client_review']", function(event) {
        // event.preventDefault();
        // var comment =$("#comment_id").val()
        // var numberStars= getGoldStarsById() 
        // var numberStars= getGoldStarsById() 
        // var csrftoken = getCookie('csrftoken');
        var pidValue = $('input[name="pid"]').attr('id');
        var full_comments;
        // setInterval(function() {
          $.ajax({
            url: "/commentProduct/",
            method: "GET",
            data: {
                pid:pidValue
            },
            dataType: 'json',
            // beforeSend: function(xhr) {
            //     xhr.setRequestHeader("X-CSRFToken", csrftoken);
            //     console.log("Adding Products to Card")
            // },
            success: function(response) {
                $("#FullComment").empty();
                console.log("Review data received:", response);
                var reviews = response.comments;
                var ratingPercentages = response.rating_percentages;
            
                $("#Reviews_total_number").html(`Reviews ${reviews.length}`);
            
                for (var i = 0; i < reviews.length; i++) {
                    var rating = reviews[i].rating;
                    var date = reviews[i].date;
                    var username = reviews[i].user__username;
                    var comment = reviews[i].review;
                    $("#FullComment").append(full_comment(return_n_stars(rating), comment, date, username));
                }
            
                console.log("Rating percentages:", ratingPercentages)
                var keys = Object.keys(ratingPercentages);

                var keys = Object.keys(ratingPercentages);

                for (var i = 1; i <= keys.length; i++) {
                    var key = keys[i - 1];
                    var percentage = ratingPercentages[key];
                    console.log(key + ": " + percentage);
                    $(`#rate${i}star`).css("width", percentage + "%");
                    $(`#rate${i}star`).html(percentage + "%");
                    $(`#rate${i}star`).attr("aria-valuenow", percentage);
                }
                var maxPercentage = 0;
                for (var key in ratingPercentages) {
                    if (ratingPercentages.hasOwnProperty(key)) {
                        var percentage = ratingPercentages[key];
                        if (percentage > maxPercentage) {
                            maxPercentage = percentage;
                        }
                    }
                }
                
                $("#glob_rating").html('<div class="product-rating__" style="width: ' + maxPercentage + '%"></div>');

                // Update the text indicating the rating out of 7
                $(".d-flex h6").text(maxPercentage.toString() + "% out of 100%");

                    // Here you can perform any operations with the key-value pair
                    // For example, update HTML elements based on these values
            
                // for (var index = 0; index < ratingPercentages.length; index++) {
                //     console.log(ratingPercentages[index])
                    
                // }
                // $("#Add_To_Prod_Status").empty();

                // // Set the HTML for the alert
                // $("#Add_To_Prod_Status").html('<div class="alert alert-success" style="margin-left: 100px; width: 800px;" role="alert">Product Has Been Added Or Modified Sucessfully!</div>');

                // Set a timeout to remove the alert after 2.5 seconds
                // setTimeout(function() {
                //     $("#Add_To_Prod_Status").empty();
                // }, 2500); // 2500 milliseconds = 2.5 seconds
            },
            error: function(xhr, textStatus, errorThrown) {
                var errorResponse = JSON.parse(xhr.responseText);
                console.log(errorResponse)

                // alert(errorResponse.error); // Log the specific error message
                // $("#Add_To_Prod_Status").empty();

                // $("#Add_To_Prod_Status").html('<div class="alert alert-danger" role="alert" style="margin-left: 800px; width: 500px;>Error Has Happened '+errorResponse+'!</div>');

                // Set a timeout to remove the alert after 2.5 seconds
                // setTimeout(function() {
                //     $("#Add_To_Prod_Status").empty();
                // }, 2500); 
            }
        // },1000)

        });
    
    
    
    
     
        
    })
}
// })

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