
                var iframe = window.parent.document.getElementById('popup-iframe');
                const overlay = window.parent.document.querySelector('.overlay');
                const popup = window.parent.document.querySelector('.popup');


          function closePopup() {
    overlay.style.display = 'none';
    popup.style.display = 'none';
    iframe.src = ''; // Reset iframe src
  }

        var button = $("#button_close_iframe");
   
    if (window.parent !== window) {

            button.removeAttr("hidden");
        
            button.on("click", function() {
                closePopup();
           
                });
        } else {
            add_button_in_iframe=window.document.getElementById("prod_ven")
           
        }