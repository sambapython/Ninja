from flask import Flask,request
app=Flask(__name__)

@app.route("/")
def method():
	return "this method is: %s"%request.method

@app.route("/anudeep",methods=['GET','POST'])
def anudeep():
	if request.method=='POST':
		return "this is POST method"
	else:
		return "this is GET method"
if __name__=='__main__':
	app.run(debug=True) 
