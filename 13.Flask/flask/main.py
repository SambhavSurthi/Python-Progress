from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def index():
    return '<h1> This is a index page at route / </h1>'

@app.route('/home')
def home():
    return '<h1> This is a Home page at route /home </h1>'


@app.route('/show/<number>')
def showing(number):
    return number

@app.route('/form',methods=['GET','POST'])
def submitForm():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        age=request.form['age']
        return f"Hiii <b>{name}</b>, Your Email is <b>{email}</b> and your age is <b>{age}</b>"
    return render_template('form.html')


@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        age=request.form['age']
        return render_template('result.html',ls=[name,email,age])
    return render_template('form.html')



if __name__=='__main__':
    app.run(debug=True)