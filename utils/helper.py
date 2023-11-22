import os

# Set of allowed extensions
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# Function to check whether the file has allowed file extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Function to save file with allowed file extension into a specific directory
def save_uploaded_file(file, upload_folder='uploads'):
    if file and allowed_file(file.filename):
        filename = file.filename
        save_path = os.path.join(upload_folder, filename)
        file.save(save_path)
        return filename
    else:
        return None