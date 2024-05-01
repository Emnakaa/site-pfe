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


const submitButton = document.getElementById('détection');
const errorMessage = document.getElementById('error-message');

// Allowed video formats (modify as needed)
const allowedFormats = ['video/mp4', 'video/mov', 'video/webm'];

fileInput.addEventListener('change', (event) => {
  const selectedFile = event.target.files[0];

  // Check if a file is selected
  if (!selectedFile) {
    errorMessage.textContent = 'Veuillez sélectionner un fichier.';
    submitButton.disabled = true;
    return;
  }

  // Check file type using MIME type
  const fileType = selectedFile.type;
  if (!allowedFormats.includes(fileType)) {
    errorMessage.textContent = `Format de fichier non pris en charge. Veuillez sélectionner un fichier MP4, MOV ou WEBM.`;
    submitButton.disabled = true;
    return;
  }
 

  // File format is valid, enable submit button and clear error message
  errorMessage.textContent = '';
  submitButton.disabled = false;
  
});



// Handle form submission (assuming further processing in another script)
uploadForm.addEventListener('submit', (event) => {
  // Prevent default form submission behavior
  event.preventDefault();

  // Handle video processing or upload logic here
});
