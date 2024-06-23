

$(document).ready(function() {
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
});

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
