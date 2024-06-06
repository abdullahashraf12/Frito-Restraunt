document.addEventListener("DOMContentLoaded", function() {
    const qtyContainers = document.querySelectorAll('.detail-qty');

    qtyContainers.forEach(function(container) {
        const qtyValue = container.querySelector('.qty-val');
        const qtyUpBtn = container.querySelector('.qty-up');
        const qtyDownBtn = container.querySelector('.qty-down');

        if (!qtyValue || !qtyUpBtn || !qtyDownBtn) {
            console.error('One or more elements not found in a container.');
            return;
        }

        // Initialize qtyValue with a default value if it's empty or not a number
        if (isNaN(parseInt(qtyValue.value))) {
            qtyValue.value = 1;
        }

        // Increment quantity when up button is clicked
        qtyUpBtn.addEventListener('click', function(event) {
            event.preventDefault();
            incrementQuantity(qtyValue);
        });

        // Decrement quantity when down button is clicked
        qtyDownBtn.addEventListener('click', function(event) {
            event.preventDefault();
            decrementQuantity(qtyValue);
        });

        // Handle keydown events for numeric input and arrow keys
        qtyValue.addEventListener('keydown', function(event) {
            handleKeydown(event, qtyValue);
        });

        function handleKeydown(event, input) {
            const key = event.key;
            const controlKeys = ['Backspace', 'Delete', 'ArrowLeft', 'ArrowRight', 'Tab'];

            if (controlKeys.includes(key)) {
                // Allow control keys
                return;
            }

            if (key === 'ArrowUp') {
                event.preventDefault();
                incrementQuantity(input);
            } else if (key === 'ArrowDown') {
                event.preventDefault();
                decrementQuantity(input);
            } else if (!/^[0-9]$/.test(key)) {
                event.preventDefault();
            }
        }

        function incrementQuantity(input) {
            let currentValue = parseInt(input.value);
            currentValue = isNaN(currentValue) ? 0 : currentValue; // Handle NaN case
            input.value = currentValue + 1;
        }

        function decrementQuantity(input) {
            let currentValue = parseInt(input.value);
            currentValue = isNaN(currentValue) ? 1 : currentValue; // Handle NaN case
            input.value = currentValue > 1 ? currentValue - 1 : 1;
        }
    });
});

// document.addEventListener("DOMContentLoaded", function() {
//     const qtyValue = document.querySelector('.qty-val');
//     const qtyUpBtn = document.querySelector('.qty-up');
//     const qtyDownBtn = document.querySelector('.qty-down');

//     // Increment quantity when up button is clicked
//     qtyUpBtn.addEventListener('click', function(event) {
//         event.preventDefault();
//         incrementQuantity();
//     });

//     // Decrement quantity when down button is clicked
//     qtyDownBtn.addEventListener('click', function(event) {
//         event.preventDefault();
//         decrementQuantity();
//     });

//     // Allow only numeric input
//     qtyValue.addEventListener('keydown', function(event) {
//         if (!isNumericInput(event)) {
//             event.preventDefault();
//         }
//     });

//     // Increment/decrement quantity using arrow keys
//     qtyValue.addEventListener('keydown', function(event) {
//         if (event.key === 'ArrowUp') {
//             event.preventDefault();
//             incrementQuantity();
//         } else if (event.key === 'ArrowDown') {
//             event.preventDefault();
//             decrementQuantity();
//         }
//     });

//     function isNumericInput(event) {
//         const key = event.key;
//         return /^[0-9]*$/.test(key);
//     }

//     function incrementQuantity() {
//         let currentValue = parseInt(qtyValue.value);
//         qtyValue.value = currentValue + 1;
//     }

//     function decrementQuantity() {
//         let currentValue = parseInt(qtyValue.value);
//         // Check if current value is greater than 1, if not set it to 1
//         currentValue = currentValue > 1 ? currentValue - 1 : 1;
//         qtyValue.value = currentValue;
//     }
// });
