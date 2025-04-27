import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from utils import allowed_file, get_file_extension
from static.chaincode import chain_code
import cv2 as cv

UPLOAD_FOLDER = os.path.join('static', 'images')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('file') 
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(path)

            output_filename = f'processed_image.{get_file_extension(file)}'
            output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
            chaincode, processed_img = chain_code(path) 
            cv.imwrite(output_path, processed_img)

            return render_template("output.html", filename=output_filename, chaincode=chaincode)
    return render_template('index.html')

@app.route('/output/<filename>')
def output(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    app.run(debug=True)
