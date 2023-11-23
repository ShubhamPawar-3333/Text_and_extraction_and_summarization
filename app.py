# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for
from ocr_engine import ocr_image
from utils.helper import allowed_file, save_uploaded_file
import os

app = Flask(__name__)

# Set up configuration for file uploads
app.config['UPLOAD_FOLDER'] = 'uploads'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Home route
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files[file]
        if file and allowed_file(file.filename):
            filename = save_uploaded_file(file)
            if filename:
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                extracted_text = ocr_image(file_path)
                return render_template('index.html', extracted_text = extracted_text)
        return redirect(url_for('index'))
    return render_template('index.html', extracted_text = None)



if __name__ == '__main__':
    app.run(debug=True)
