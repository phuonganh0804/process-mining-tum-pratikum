from flask import Flask, render_template, request, flash, redirect, send_from_directory, session, url_for
from werkzeug.utils import secure_filename
from alpha_miner.alpha_algorithm import AlphaAlgorithm
from heuristic_miner.heuristic_mining import HeuristicMiner 
import os
import shutil
from flask import request

UPLOAD_FOLDER = './backend/static/uploads'

# define allowed files:
ALLOWED_EXTENSIONS = {'xes', 'pdf'}

app = Flask(__name__)

# Configure upload file path flask
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Set the secret key to some random bytes.
app.secret_key = b'_5#y2251248rt8z\n\xec]/'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/api/upload', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],
                            filename))
            session['uploaded_data_file_path'] = os.path.join(app.config['UPLOAD_FOLDER'],
                     filename)
            # Uploaded File Path
            data_file_path = session.get('uploaded_data_file_path', None)
            # read .xes file
            algorithm = request.form.get("algorithm")
            d = {}
            if (algorithm == "Alpha Algorithm"):
                mining = AlphaAlgorithm(data_file_path)    
                result = mining.get_petri_net()  
                d['message'] = result
            elif (algorithm == "Heuristic Miner"):
                dependency = float(request.form.get("dependency"))
                and_threshold = float(request.form.get("and"))
                mining = HeuristicMiner(data_file_path, dependency, and_threshold)
                result = mining.heuristic_net()
                d['message'] = result 
            dest = './frontend/src/result.png' 
            shutil.copy(d['message'], dest)
            return redirect(url_for("pdf", data=d['message']))
    return render_template('index.html')

@app.route('/uploads/<name>')
def download_file(name):
    return render_template("upload.html", filename=name)

@app.route('/pdf/<data>')
def pdf(data):
    return send_from_directory("../", data)
    
if __name__ == '__main__':
   app.run(debug=True)
    


