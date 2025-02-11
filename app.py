from flask import Flask, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'mp3', 'wav'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if the post request has the file part
    if 'audioFile' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['audioFile']

    # If the user does not select a file, the browser also
    # submits an empty part without filename
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file and allowed_file(file.filename):
        # Save the uploaded file
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
        file.save(file_path)

        # Get file details
        file_details = {
            'fileName': file.filename,
            'fileSize': os.path.getsize(file_path)
        }

        return jsonify(file_details)

    return jsonify({'error': 'Invalid file format'})

if __name__ == '__main__':
    app.run(debug=True)


