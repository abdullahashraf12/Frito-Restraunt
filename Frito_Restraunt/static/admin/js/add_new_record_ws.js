
document.addEventListener('DOMContentLoaded', function() {
    function runMe(){
        $('.save-button').on('click', function(e) {
          e.preventDefault();
          
          var row = $(this).closest('tr');
          var id = row.find('th.field-id a').text().trim();
          var clientStatus = row.find('select[name="client_status"]').val();
          var salesRep = row.find('select[name="SalesRep"]').val();
          
          var data = {
              'pk': id,
              'client_status': clientStatus,
              'SalesRep': salesRep
          };
      
          // Perform AJAX request to save data
          $.ajax({
              url: '/core/save_cashier_table/' + data.pk ,
              method: 'POST',
              data: {
                  'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                  'client_status': data.client_status,
                  'SalesRep': data.SalesRep,
                  'id': parseInt(data.pk)  // Include the ID in the POST data
              },
              success: function(response) {
                  // Optional: Handle success response if needed
                  console.log('Data saved successfully!');
                  // Example: Update UI or show a success message
                  console.log(response.client_status)
                  console.log(response.SalesRep)
                  // Assuming response contains updated data, you can update the row
                  // For example, if your response includes updated client_status and SalesRep values
               
                  // Alternatively, you can reload the entire row from the server if needed
                  // Example: row.load('/admin/product/cashiertable/' + data.pk + '/'); // Reloads the row
                  
              },
              error: function(xhr, status, error) {
                  // Optional: Handle error response if needed
                  console.error('Error saving data:', error);
                  // Example: Show an error message to the user
              }
          });
      });
      
          var $currentIframe = null;
      
          // Open or close popup when a link with class 'openPopup' is clicked
          $('.openPopup').click(function(e) {
              e.preventDefault();
      
              var $popup = $(this).siblings('.popup');
              var $iframe = $popup.find('.videoIframe');
      
              // Close all other popups
              // $('.popup').not($popup).fadeOut();
      
              // Toggle the clicked popup
              $popup.fadeToggle(function() {
                  // Check if the popup is now visible
                  
                  var isVisible = $popup.is(':visible');
                  console.log(isVisible)
                  if (isVisible) {
                      // Popup is now visible, load iframe content if not already loaded
                      var iframeSrc = $iframe.attr('data-src');
                      if (iframeSrc && !$iframe.attr('src')) {
                          $iframe.attr('src', iframeSrc).on('load', function() {
                              $iframe.fadeIn();
                              $currentIframe = $iframe;
                          });
                      }
                  } else {
                      var iframeSrc = $iframe.attr('data-src');
                      if (iframeSrc && !$iframe.attr('src')) {
                          $iframe.attr('src', iframeSrc).on('load', function() {
                              $iframe.fadeIn();
                              $currentIframe = $iframe;
                              $popup.fadeIn();
                          });
                      }
                      // Popup is now hidden, remove iframe if it exists
                      if ($currentIframe && $currentIframe.parent().is($popup)) {
                          $currentIframe.fadeOut('fast', function() {
                              $(this).remove(); // Remove the iframe from DOM
                          });
                          $currentIframe = null;
                      }
                  }
              });
          });
      
          // Close popup when close button or outside popup content is clicked
          $('.popup .close, .popup-overlay').click(function() {
              var $popup = $(this).closest('.popup');
              var $iframe = $popup.find('.videoIframe');
      
              $popup.fadeOut();
      
              // Check if $currentIframe is in this popup and remove it
              if ($currentIframe && $currentIframe.parent().is($popup)) {
                  $currentIframe.fadeOut('fast', function() {
                      $(this).remove(); // Remove the iframe from DOM
                  });
                  $currentIframe = null;
              }
          });
      
          // Optional: Close popup when Escape key is pressed
          $(document).keyup(function(e) {
              if (e.key === "Escape") {
                  $('.popup').fadeOut();
                  if ($currentIframe) {
                      $currentIframe.fadeOut('fast', function() {
                          $(this).remove(); // Remove the iframe from DOM
                      });
                      $currentIframe = null;
                  }
              }
          });
          
    
      
    }
    function undoRunMe() {
        // Remove event handlers from save buttons
        $('.save-button').off('click');
    
        // Remove event handlers from openPopup links
        $('.openPopup').off('click');
    
        // Remove event handlers from close buttons and overlay
        $('.popup .close, .popup-overlay').off('click');
    
        // Unbind keyup event for Escape key
        $(document).off('keyup');
    
        // Additional cleanup if necessary:
        // - Remove any added elements
        // - Reset global variables or states
    
        // Optional: Reset any specific variables or states introduced by runMe()
        // $currentIframe = null; // Example reset if needed
    
        console.log('Effects of runMe() have been undone.');
    }
    
    // Call undoRunMe() whenever you need to remove the effects of runMe()
    // For example, you might trigger this on a certain event or condition in your application
    undoRunMe();
    
    runMe();

    const socket = new WebSocket('ws://' + window.location.host + '/core/ws/cart/admin/');

    socket.onmessage = function(event) {
        


    // Add save button functionality
    try{
      
  
        const data = JSON.parse(event.data);
        console.log('New record:', data);
        alert(data.popup_url.toString())

        const tableBody = document.querySelector('#result_list tbody');

        const newRow = document.createElement('tr');
        newRow.innerHTML = `
            <td class="action-checkbox">
                <input type="checkbox" name="_selected_action" value="${data.id}" class="action-select" aria-label="Select this object for an action - CashierTable object (${data.id})">
            </td>
            <th class="field-id">
                <a href="/admin/product/cashiertable/${data.id}/change/">${data.id}</a>
            </th>
            <td class="field-order_number">${data.order_number}</td>
            <td class="field-order_date nowrap">${new Date(data.order_date).toLocaleString()}</td>
            <td class="field-client nowrap">${data.client}</td>
            <td class="field-address">${data.address}</td>
            <td class="field-client_number">${data.client_number}</td>
            <td class="field-total_price">${data.total_price.toFixed(2)}</td>
            <td class="field-client_status_widget">
                <select name="client_status" style="width: 200px; color: red;">
                    <option value="New" ${data.status === 'New' ? 'selected' : ''}>New</option>
                    <option value="In Progress" ${data.status === 'In Progress' ? 'selected' : ''}>In Progress</option>
                    <option value="On Delivery" ${data.status === 'On Delivery' ? 'selected' : ''}>On Delivery</option>
                    <option value="Finished" ${data.status === 'Finished' ? 'selected' : ''}>Finished</option>
                </select>
            </td>
            <td class="field-sales_rep">
                <select name="SalesRep" style="width: 200px; color: blue;" data-url="/admin/your_app/user/">
                    <option value="" ${data.sales_rep ? '' : 'selected'}>---------</option>
                    <option value="3" ${data.sales_rep === 'ahmed' ? 'selected' : ''}>ahmed</option>
                    <option value="4" ${data.sales_rep === 'mahmed' ? 'selected' : ''}>mahmed</option>
                </select>
            </td>
            <td class="field-open_popup_button">
                <div class="popup-container" style="margin-left:50px;">
                    <a href="#" class="openPopup ui-btn ui-corner-all ui-shadow ui-btn-inline">Open Client Data</a>
                    <div class="popup" style="display: none;">
                        <div class="popup-content">
                        <iframe name="my_iframe" data-src="${data.popup_url}" class="videoIframe" style="margin-left: -920%; margin-top: 15%;" width="1000%" height="550px" seamless="" src="${data.popup_url}"></iframe>
                        </div>
                    </div>
                </div>
            </td>
            <td class="field-save_button">
  <input type="submit" class="save-button" style=" padding: 10px 20px; background-color: blue;  color: white;   border: none;  border-radius: 5px;   text-align: center;  text-decoration: none;  display: inline-block;   font-size: 16px;     margin: 4px 2px;   transition-duration: 0.4s;     cursor: pointer;" value="Save">
            </td>          
            <td class="field-latitude">${data.latitude}</td>
            <td class="field-longitude">${data.longitude}</td>
            `;
            if (data.latitude.toString()=="undefined"){
                newRow.innerHTML+=`<td class="field-open_map"><a  href="https://www.google.com/maps?q=${data.address}&amp;hl=ar" target="_blank" style="                    display: inline-block;                     width: 100px;                     padding: 10px;                     text-align: center;                     background-color: #007bff;                     color: white;                     text-decoration: none;                     border-radius: 5px;                     transition: background-color 0.3s;">Open Map</a></td>`;

        }else{
            newRow.innerHTML+=`<td class="field-open_map"><a href="https://www.google.com/maps?q=${data.latitude},${data.longitude}&amp;hl=ar" target="_blank" style="                    display: inline-block;                     width: 100px;                     padding: 10px;                     text-align: center;                     background-color: #007bff;                     color: white;                     text-decoration: none;                     border-radius: 5px;                     transition: background-color 0.3s;">Open Map</a></td>`;

        }
            
   

        tableBody.prepend(newRow);
        undoRunMe();
        runMe();

        alert(`New Order Added: ${data.order_number} - Client: ${data.client}`);
    }catch(Exception){
        


        location.reload()

    }

    };

    socket.onopen = function() {
        console.log('WebSocket connection opened.');
    };

    socket.onclose = function() {
        console.log('WebSocket connection closed.');
    };

    socket.onerror = function(error) {
        console.error('WebSocket error:', error);
    };

});
