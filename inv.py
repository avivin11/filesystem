from flask import Flask
from flask import request
from flask import render_template
import Decrypt as b
app = Flask(__name__)
roll=''
@app.route('/')
def my_form():
    return render_template("staff.html")


@app.route('/b', methods=['POST'])
def my_form_post1():
	global roll
	roll= request.form['name1']
	text = request.form['name']
	b.Decrypt(text,roll)
	return render_template("staff.html")

if __name__ == '__main__':
    app.run(debug=True,port=5003)