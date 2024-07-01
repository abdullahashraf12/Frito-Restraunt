$(document).ready(function() {

try{
    $("input.save-button").click(function() {
        var successAlert = `
    <div class="alert alert-success" role="alert" style=text-weight:bold;"">
        Record Has Been Saved
    </div>
`;

// Prepend the success alert to the specified div
$(".change-list-actions.row.pb-3").prepend(successAlert);

// Remove the alert after 2 seconds
setTimeout(function() {
    $(".alert-success").remove();
}, 2000);
    });
}catch(Err){

}
});
// $(document).ready(function() {

//   // Add save button functionality
//   $('.save-button').on('click', function(e) {
//     e.preventDefault();
    
//     var row = $(this).closest('tr');
//     var id = row.find('th.field-id a').text().trim();
//     var clientStatus = row.find('select[name="client_status"]').val();
//     var salesRep = row.find('select[name="SalesRep"]').val();
    
//     var data = {
//         'pk': id,
//         'client_status': clientStatus,
//         'SalesRep': salesRep
//     };

//     // Perform AJAX request to save data
//     $.ajax({
//         url: '/core/save_cashier_table/' + data.pk ,
//         method: 'POST',
//         data: {
//             'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
//             'client_status': data.client_status,
//             'SalesRep': data.SalesRep,
//             'id': parseInt(data.pk)  // Include the ID in the POST data
//         },
//         success: function(response) {
//             // Optional: Handle success response if needed
//             console.log('Data saved successfully!');
//             // Example: Update UI or show a success message
//             console.log(response.client_status)
//             console.log(response.SalesRep)
//             // Assuming response contains updated data, you can update the row
//             // For example, if your response includes updated client_status and SalesRep values
         
//             // Alternatively, you can reload the entire row from the server if needed
//             // Example: row.load('/admin/product/cashiertable/' + data.pk + '/'); // Reloads the row
            
//         },
//         error: function(xhr, status, error) {
//             // Optional: Handle error response if needed
//             console.error('Error saving data:', error);
//             // Example: Show an error message to the user
//         }
//     });
// });

//     var $currentIframe = null;

//     // Open or close popup when a link with class 'openPopup' is clicked
//     $('.openPopup').click(function(e) {
//         e.preventDefault();

//         var $popup = $(this).siblings('.popup');
//         var $iframe = $popup.find('.videoIframe');

//         // Close all other popups
//         // $('.popup').not($popup).fadeOut();

//         // Toggle the clicked popup
//         $popup.fadeToggle(function() {
//             // Check if the popup is now visible
            
//             var isVisible = $popup.is(':visible');
//             console.log(isVisible)
//             if (isVisible) {
//                 // Popup is now visible, load iframe content if not already loaded
//                 var iframeSrc = $iframe.attr('data-src');
//                 if (iframeSrc && !$iframe.attr('src')) {
//                     $iframe.attr('src', iframeSrc).on('load', function() {
//                         $iframe.fadeIn();
//                         $currentIframe = $iframe;
//                     });
//                 }
//             } else {
//                 var iframeSrc = $iframe.attr('data-src');
//                 if (iframeSrc && !$iframe.attr('src')) {
//                     $iframe.attr('src', iframeSrc).on('load', function() {
//                         $iframe.fadeIn();
//                         $currentIframe = $iframe;
//                         $popup.fadeIn();
//                     });
//                 }
//                 // Popup is now hidden, remove iframe if it exists
//                 if ($currentIframe && $currentIframe.parent().is($popup)) {
//                     $currentIframe.fadeOut('fast', function() {
//                         $(this).remove(); // Remove the iframe from DOM
//                     });
//                     $currentIframe = null;
//                 }
//             }
//         });
//     });

//     // Close popup when close button or outside popup content is clicked
//     $('.popup .close, .popup-overlay').click(function() {
//         var $popup = $(this).closest('.popup');
//         var $iframe = $popup.find('.videoIframe');

//         $popup.fadeOut();

//         // Check if $currentIframe is in this popup and remove it
//         if ($currentIframe && $currentIframe.parent().is($popup)) {
//             $currentIframe.fadeOut('fast', function() {
//                 $(this).remove(); // Remove the iframe from DOM
//             });
//             $currentIframe = null;
//         }
//     });

//     // Optional: Close popup when Escape key is pressed
//     $(document).keyup(function(e) {
//         if (e.key === "Escape") {
//             $('.popup').fadeOut();
//             if ($currentIframe) {
//                 $currentIframe.fadeOut('fast', function() {
//                     $(this).remove(); // Remove the iframe from DOM
//                 });
//                 $currentIframe = null;
//             }
//         }
//     });
    
// });

// $(document).ready(function() {
//     var $currentIframe = null;

//     // Open or close popup when a link with class 'openPopup' is clicked
//     $('.openPopup').click(function(e) {
//         e.preventDefault();

//         var $popup = $(this).siblings('.popup');

//         // Close all other popups and reset currently displayed iframe
//         $('.popup').not($popup).fadeOut();
//         if ($currentIframe) {
//             $currentIframe.fadeOut('fast', function() {
//                 $currentIframe.remove();
//             });
//             $currentIframe = null;
//         }

//         // Toggle the clicked popup
//         $popup.fadeToggle();

//         // Load iframe content if not already loaded
//         var $iframe = $popup.find('.videoIframe');
//         var iframeSrc = $iframe.attr('data-src');
//         if (iframeSrc && !$iframe.attr('src')) {
//             $iframe.attr('src', iframeSrc).on('load', function() {
//                 $iframe.fadeIn();
//                 $currentIframe = $iframe;
//             });
//         }
//     });

//     // Close popup when close button or outside popup content is clicked
//     $('.popup .close, .popup-overlay').click(function() {
//         var $popup = $(this).closest('.popup');
//         $popup.fadeOut();
//         if ($currentIframe) {
//             $currentIframe.fadeOut('fast', function() {
//                 $currentIframe.remove();
//             });
//             $currentIframe = null;
//         }
//     });

//     // Optional: Close popup when Escape key is pressed
//     $(document).keyup(function(e) {
//         if (e.key === "Escape") {
//             $('.popup').fadeOut();
//             if ($currentIframe) {
//                 $currentIframe.fadeOut('fast', function() {
//                     $currentIframe.remove();
//                 });
//                 $currentIframe = null;
//             }
//         }
//     });
// });
