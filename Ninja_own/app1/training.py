from flask import Flask,render_template,redirect,url_for,request
app=Flask(__name__)

@app.route('/')
def home():
	return "Welcome to home page"

@app.route('/login', methods==['GET','POST'])
def login():
	error=None
	if request.methods=='POST':
		if request.form['name']!='Anudeep' or request.form['password']!='123':
			error="Please check your crenditials and try again !"
		return redirect(url_for('home'))
	return render_template('login.html',error=error)

if __name__=='__main__':
	app.run(debug=True)
