from flask import Flask
app=Flask(__name__)

@app.route('/')
def fun():
	return "Hello Anudeep Tarimela"
@app.route('/profile/<username>')
def fun1(username):
	return "<h1>Hello %s<h1>"%username
@app.route('/profile/<int:profile_id>')
def fun2(profile_id):
	return "<h2>Hello Anudeep your id is %s</h2>"%profile_id
if __name__=='__main__':
	app.run(debug=True)
