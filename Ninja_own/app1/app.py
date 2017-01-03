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
	return render_template('b.html',)
	'''
	data = pd.read_csv('data.csv')
	names = data.name
	names = names.values.tolist()
	avg_sal = data.sal.mean()
	return render_template('b.html',person_names=names, sal_avg = avg_sal)
	


if __name__ == "__main__":
	app.run(port=8889,debug=True)

