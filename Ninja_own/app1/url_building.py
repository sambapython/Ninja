from flask import Flask,redirect,url_for
app=Flask(__name__)

@app.route("/admin")
def admin():
	return "Hello Admin"
@app.route("/guest/<guest>")
def guest(guest):
	return "Hello %s as Guest" % guest
@app.route("/user/<user>")
def user(user):
	if user=="admin":
	   return redirect(url_for("admin"))
	else:
	   return redirect(url_for("guest",guest=name))
if __name__=='__main__':
	app.run(debug=True)
