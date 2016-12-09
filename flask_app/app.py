'''
from flask import Flask 
print Flask.__file__
'''
'''
import flask
print flask.__file__

'''
from flask import Flask 
app = Flask(__name__)
@app.route('/')
def home():
	data = open('home.html').read()
	return data
	#return "<h1>Hello Flask</h1>"

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0',port=8889)





