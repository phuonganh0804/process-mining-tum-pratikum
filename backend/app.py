from flask import Flask, render_template, request, flash, redirect, session
from werkzeug.utils import secure_filename
from alpha_miner.alpha_algorithm import AlphaAlgorithm
from heuristic_miner.heuristic_mining import HeuristicMiner 
import os
from flask import jsonify, request

UPLOAD_FOLDER = './backend/static/uploads'

# define allowed files:
ALLOWED_EXTENSIONS = {'xes'}

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
                mining.get_petri_net()  
                d['message'] = "alpha success"
            elif (algorithm == "Heuristic Miner"):
                mining = HeuristicMiner(data_file_path, 0.5, 0.1)
                mining.heuristic_net()
                d['message'] = "heuristic success"
            return jsonify(d)
    return render_template('index.html')

if __name__ == '__main__':
   app.run(host="::1", port = 9025)
    


