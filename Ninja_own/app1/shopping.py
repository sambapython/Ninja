from flask import Flask,render_template
app=Flask(__name__)

@app.route("/shopping")
def shopping():
    food=["chicken","mutton","fish","prons"]
    return render_template("shopping.html",food=food)

if __name__=="__main__":
	app.run(debug=True,port=8899)
