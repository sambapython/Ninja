from flask import Flask, render_template, request
#import pandas as pd
import pdb
import db_operations
app = Flask(__name__,template_folder='own_templates',)

@app.route('/signup', methods=['GET','POST'])
def reg():
	message=""
	if request.method == "POST":
		data = request.form
		ret_value = db_operations.insert(data)
		message = ret_value

	return render_template('reg.html',message=message)


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
	app.run(port=8889,debug=True)

