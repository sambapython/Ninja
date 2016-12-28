from flask import Flask, render_template, request, make_response
import pandas as pd
import pdb
import db_operations
app = Flask(__name__,template_folder='own_templates',)

@app.route('/reg', methods=['GET','POST'])
def reg():
	message=""
	if request.method == "POST":
		data = request.form
		ret_value = db_operations.insert(data)
		message = ret_value

	return render_template('reg.html',message=message)
@app.route('/contact')
def contact():
	user = request.cookies.get('user')
	return render_template('contact.html',user = user)

@app.route('/login', methods=['GET','POST'])
def signin():
	message = ""
	if request.method=="POST":
		username = request.form.get('name')
		password = request.form.get('password')
		user = db_operations.check_user(username, password)
		if user:
			resp_obj = make_response(render_template('home.html', message="Signin succesfully"))
			resp_obj.set_cookie('user',username)
			return resp_obj
		else:
			message="sigin failed"

	return make_response(render_template('signin.html',message=message))


@app.route('/')
def index():
	#return "<h1> Hello flask</h1>"
	'''
	f=open('a.html')
	data = f.read()
	return data
	'''
	'''
	return render_template('a.html',)
	'''
	data = pd.read_csv('data.csv')
	names = data.name
	names = names.values.tolist()
	avg_sal = data.sal.mean()
	return render_template('a.html',person_names=names, sal_avg = avg_sal)
	


if __name__ == "__main__":
	app.run(port=8889,debug=True)

