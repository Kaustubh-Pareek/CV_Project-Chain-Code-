import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from utils import allowed_file, get_file_extension
#from static.pipeline import labeller

UPLOAD_FOLDER = './images'


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)



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
            #chain_code = labeller(path, output_path)

            return render_template("output.html", filename=f'processed_image.{get_file_extension(file)}')
    return render_template("index.html")

@app.route('/output/<filename>')
def output(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    app.run(debug=True)
