from flask import Flask, render_template, url_for, redirect, request
import pandas as pd
app=Flask(__name__)
import pdb
import os

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
def get_path_images():
	static_images = url_for('static',filename="images")
	static_folder  = static_images.split('/')[1]
	images  = static_images.split('/')[2]
	file_path = os.path.join(static_folder, images)
	return file_path



@app.route('/fileupload',methods=['GET','POST'])
def fileupload():
	images_path = get_path_images()
	images_names = os.listdir(images_path)
	if request.method == "POST":
		img = request.files.get('image')
		
		file_path = os.path.join(images_path, img.filename)
		img.save(file_path)	
	file_paths = []
	for  image in images_names:
		file_paths.append(os.path.join(images_path,image))
	return render_template('form.html', file_paths = file_paths)


if __name__ == "__main__":
	app.run(debug=True)
