from flask import Flask, render_template, url_for, redirect
import pandas as pd
app=Flask(__name__)
import pdb

@app.route('/')
def home():
	return render_template('base.html')
@app.route('/persons/<name>')
def persons(name):
	data= pd.read_csv('data.csv')
	if name == 'all':
		return render_template('persons.html',
			 names = data['name'].values)
	else:
		person_data = data[data['name']==name]
		if person_data.empty:
			return redirect(url_for('persons',name='all'))
		else:
			perdetails = person_data.to_dict()
			person = dict()
			for atr in perdetails:
				person.update({atr:perdetails[atr].values()[0]})

			return render_template('persons_info.html',
				person_info = person)



if __name__ == "__main__":
	app.run(debug=True)
