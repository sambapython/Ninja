from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
 
app = Flask(__name__)
 
@app.route('/', methods=['GET','POST'])
def home():
    if request.method=="POST":
        session['logged_in']=request.form.get('nm')
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello {0}  <a href='/logout'>Logout</a>".format(session['logged_in'])
 
@app.route('/login', methods=['GET','POST'])
def do_admin_login():
    if request.method=="POST":
        if request.form['password'] == 'password' and request.form['username'] == 'admin':
            session['logged_in'] = True
        else:
            flash('wrong password!')
        return home()
    return render_template('login.html')

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

 
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, port=4000)
