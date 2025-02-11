function uploadFile() {
    // Get the file input element
    const fileInput = document.querySelector('input[name="audioFile"]');

    // Check if a file is selected
    if (fileInput.files.length > 0) {
        // Create a FormData object to send the file
        const formData = new FormData();
        formData.append('audioFile', fileInput.files[0]);

        // Send the file to the server using fetch
        fetch('/upload', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            // Display file details on the page
            displayFileDetails(data);
        })
        .catch(error => {
            console.error('Error uploading file:', error);
        });
    } else {
        alert('Please select an audio file.');
    }
}

function displayFileDetails(data) {
    // Get the file details container
    const fileDetailsContainer = document.getElementById('fileDetails');

    // Display file details on the page
    fileDetailsContainer.innerHTML = `
        <p><strong>Uploaded File:</strong> ${data.fileName}</p>
        <p><strong>File Size:</strong> ${data.fileSize} bytes</p>
    `;
}