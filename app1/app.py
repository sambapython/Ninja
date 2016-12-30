from flask import Flask, render_template, request, make_response, session, redirect, url_for
import pandas as pd
import pdb
import db_operations
app = Flask(__name__,template_folder='own_templates',)
'''
def check_signin():
	user = session.get('user')
	if user:
		return user
	return False
'''
# decorator to check the user loged in or not.
'''
@app.errorhandler(404)
def page_not_found(err):
	return render_template('404.html',error=err)
	'''

@app.errorhandler(501)
def error_501(err):
	return render_template('501.html',error=err)



def login_user(fun):
	def inner():
		user = session.get('user')
		if not user:
			url = url_for('signin')
			return redirect(url)
		return fun()
	return inner

@app.route('/reg', methods=['GET','POST'])
def reg():
	message=""
	if request.method == "POST":
		data = request.form
		ret_value = db_operations.insert(data)
		message = ret_value

	return render_template('reg.html',message=message)


@app.route('/contact',methods=['GET','POST'])
@login_user
def contact():
	'''
	#user = request.cookies.get('user')
	user = session.get('user')
	'''
	user = session.get('user')
	return render_template('contact.html',user = user)
	'''
	else:
		#return render_template('signin.html')
		#return redirect('/login')
		url = url_for('signin')
		print "url=",url
		return redirect(url)
	'''

@app.route('/logout')
def signout():
	session.pop('user')
	return render_template('signin.html',message="logout successfully")

@app.route('/login', methods=['GET','POST'])
def signin():
	message = ""
	if request.method=="POST":
		username = request.form.get('name')
		password = request.form.get('password')
		user = db_operations.check_user(username, password)

		if user:
			'''
			resp_obj = make_response(render_template('home.html', message="Signin succesfully"))
			resp_obj.set_cookie('user',username)
			return resp_obj
			'''
			session['user'] = user
			return render_template('home.html', message="Signin succesfully")
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
	app.secret_key = "some string"
	app.run(port=8889,debug=True)

