from flask import Flask,render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/places')
def places():
    return render_template("places.html")

@app.route('/visit',methods=['GET','POST'])
def visit():
    # return render_template('registered.html',name=request.args['nametext'])
    if request.method=='POST': 
        return render_template('visit.html',name=request.form['user'], place=request.form['userplace'])
    else:
        #return render_template('home.html')
        return redirect('/places')
        #return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(port=3000,debug=True)