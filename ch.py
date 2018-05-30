import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import render_template

UPLOAD_FOLDER = '/home/avi/testing'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/')
def my_form():
    return render_template("co.html")

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      filen = secure_filename(f.filename)
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], filen))
      return filen
    
if __name__ == '__main__':
    app.run(debug=True,port=5002)