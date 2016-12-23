from flask import Flask, render_template
import pandas as pd
import pdb
app = Flask(__name__,template_folder='own_templates',)

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
	names = data.names
	pdb.set_trace()


if __name__ == "__main__":
	app.run(port=8899,debug=True)

