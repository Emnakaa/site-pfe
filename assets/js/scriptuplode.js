const videoElement = document.getElementById('myVideo');
const loadingElement = document.getElementById('loading');
const fileInput = document.getElementById('fileInput');

fileInput.addEventListener('change', (event) => {
  const file = event.target.files[0];
  
  if (file) {
    const reader = new FileReader();
    reader.onload = (e) => {
      videoElement.src = e.target.result;
      videoElement.load(); // Start video loading
      loadingElement.style.display = 'block'; // Show loading indicator
    };
    reader.readAsDataURL(file); // Read video file
  }

  videoElement.addEventListener('loadedmetadata', () => {
    loadingElement.style.display = 'none'; // Hide loading indicator when video is loaded
  });
});
