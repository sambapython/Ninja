from flask import Flask,redirect,url_for,request
app=Flask(__name__)

@app.route('/sucess/<name>')
def sucess(name):
	return 'welcome %s' %name
@app.route('/login',methods=["POST","GET"])
def login():
	if request.method=="POST":
	   user=request.form["nm"]
	   return redirect(url_for("sucess",name=user))
	else:
	   user=request.arg.get("nm")
	   return redirect(url_for("sucess",name=user))
if __name__=='__main__':
	app.run(debug=True)
