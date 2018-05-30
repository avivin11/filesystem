from flask import Flask,render_template,request,flash, redirect
from werkzeug.utils import secure_filename
import Encrytion as a
import Decrption as b
import Decrypt as c
import os


app = Flask(__name__)
roll=0


@app.route('/')
def my_form():
    return render_template("index.html")



@app.route('/Student.html')
def my_form1():
    return render_template("Student.html")


@app.route('/Admin.html')
def my_form3():
    return render_template("Admin.html")


@app.route('/About.html')
def my_form4():
    return render_template("About.html")


@app.route('/Admin.html')
def my_form5():
    return render_template("Admin.html")


@app.route('/1',methods=['POST'])
def my_form2():
	global roll
	roll=request.form['name']
	if not os.path.exists("/home/avi/down/"+str(roll)) :
		os.makedirs("/home/avi/down/"+str(roll))
		os.makedirs("/home/avi/ds/"+str(roll))
	return render_template("Portal.html")


@app.route('/a', methods=['GET','POST'])
def my_form_post():
	global roll
	if request.method == 'POST':
		f = request.files['file']
		filen = secure_filename(f.filename)
		f.save(os.path.join("/home/avi/testing/", filen))
		if os.path.exists("/home/avi/down/"+str(roll)+"/"+filen) :
			flash("Overwriting already existing File")
		a.Encryption(filen,roll)
		return render_template("Portal.html")

@app.route('/b', methods=['POST'])
def my_form_post1():
	global roll
	text = request.form['name']
	b.Decryption(text,roll)
	return render_template("Portal.html")


@app.route('/z',methods=['POST'])
def my_form7():
	usr = request.form['usr']
	pass1 = request.form['pass']
	us="admin123"
	ps="pass123"
	if usr==us and pass1==ps :
		return render_template("AdminPortal.html")
	else :
		flash("Enter Valid Username and Password")
		return render_template("Admin.html")


@app.route('/c', methods=['POST'])
def my_form_post5():
	global roll
	roll= request.form['name1']
	text = request.form['name']
	c.Decrypt(text,roll)
	return render_template("AdminPortal.html")


if __name__ == '__main__':
    app.run(debug=True,port=5010)