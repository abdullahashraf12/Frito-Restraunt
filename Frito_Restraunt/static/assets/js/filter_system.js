$(document).ready(function(){
    // Selecting all product cards, category checkboxes, and vendor checkboxes
    var card_element_by_categ = $('[name="product_card"]');
    var checkbox_by_categ = $('input[name="checkbox_categ"]');
    var min_price_input = $('#min_price');
    var max_price_input = $('#max_price');

    var numberOfShownItems = 0;

    // Function to update the count of shown items
    function updateShownItems() {
        numberOfShownItems = card_element_by_categ.filter(':visible').length;
        console.log("Number of shown items: " + numberOfShownItems);
        $("#number_of_all_showed_products").html(numberOfShownItems);
    }

    function applyFilters() {
        // Retrieve IDs of checked categories
        var checkedIds_categs = checkbox_by_categ.filter(':checked').map(function() {
            return this.id;
        }).get();


        var min_price = parseFloat(min_price_input.val());
        var max_price = parseFloat(max_price_input.val());

        function categoryVendorFilter() {
            var category_ids = $(this).data('categ_id').toString().split(',');

            var categoryMatch = checkedIds_categs.length === 0 || checkedIds_categs.some(id => category_ids.includes(id));

            return categoryMatch;
        }

        // Filter function for price range
        function priceFilter() {
            var product_price = parseFloat($(this).data('product-price'));
            var priceMatch = (isNaN(min_price) || product_price >= min_price) && (isNaN(max_price) || product_price <= max_price);
            return priceMatch;
        }

        if (checkedIds_categs.length === 0) {
            card_element_by_categ.hide().filter(priceFilter).show();
        } else {
            card_element_by_categ.hide().filter(categoryVendorFilter).filter(priceFilter).show();
        }

        // Update the count of shown items
        updateShownItems();
    }

    // Event handler for changes in category checkboxes
    checkbox_by_categ.change(function(){
        // Call the function to apply filters
        applyFilters();
    });

    // Event handler for changes in price inputs
    min_price_input.add(max_price_input).on('input change', function() {
        // Call the function to apply filters
        applyFilters();
    });

    // Initialize slider
    $("#slider-range").slider({
        range: true,
        orientation: "horizontal",
        min: 0,
        max: 10000,
        values: [0, 10000],
        step: 100,
        slide: function(event, ui) {
            $("#min_price").val(ui.values[0]);
            $("#max_price").val(ui.values[1]);
        },
        change: function(event, ui) {
            applyFilters(); // Apply filters when slider values change
        }
    });

    // Trigger initial filtering
    applyFilters();
});
