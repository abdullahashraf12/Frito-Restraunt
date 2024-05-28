document.addEventListener("DOMContentLoaded", function() {
    const qtyValue = document.querySelector('.qty-val');
    const qtyUpBtn = document.querySelector('.qty-up');
    const qtyDownBtn = document.querySelector('.qty-down');

    // Increment quantity when up button is clicked
    qtyUpBtn.addEventListener('click', function(event) {
        event.preventDefault();
        incrementQuantity();
    });

    // Decrement quantity when down button is clicked
    qtyDownBtn.addEventListener('click', function(event) {
        event.preventDefault();
        decrementQuantity();
    });

    // Allow only numeric input
    qtyValue.addEventListener('keydown', function(event) {
        if (!isNumericInput(event)) {
            event.preventDefault();
        }
    });

    // Increment/decrement quantity using arrow keys
    qtyValue.addEventListener('keydown', function(event) {
        if (event.key === 'ArrowUp') {
            event.preventDefault();
            incrementQuantity();
        } else if (event.key === 'ArrowDown') {
            event.preventDefault();
            decrementQuantity();
        }
    });

    function isNumericInput(event) {
        const key = event.key;
        return /^[0-9]*$/.test(key);
    }

    function incrementQuantity() {
        let currentValue = parseInt(qtyValue.value);
        qtyValue.value = currentValue + 1;
    }

    function decrementQuantity() {
        let currentValue = parseInt(qtyValue.value);
        // Check if current value is greater than 1, if not set it to 1
        currentValue = currentValue > 1 ? currentValue - 1 : 1;
        qtyValue.value = currentValue;
    }
});
