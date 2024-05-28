document.addEventListener('DOMContentLoaded', function() {
  const overlay = document.querySelector('.overlay');
  const popup = document.querySelector('.popup');
  const iframe = document.getElementById('popup-iframe');
  const triggers = document.querySelectorAll('.open_iframe');
  const closeButton = document.querySelector('button[name="close-btn"]'); // Selecting by name

  triggers.forEach(function(trigger) {
    trigger.addEventListener('click', function(e) {
      e.preventDefault();
      const src = this.getAttribute('data-src');
      iframe.src = src;
      overlay.style.display = 'block';
      popup.style.display = 'block';
    });
  });

  function closePopup() {
    overlay.style.display = 'none';
    popup.style.display = 'none';
    iframe.src = ''; // Reset iframe src
  }

  // Add event listeners
  closeButton.addEventListener('click', closePopup);

  overlay.addEventListener('click', closePopup);
});