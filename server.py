from flask import Flask, render_template, redirect, request, session
app = Flask (__name__)
app.secret_key = 'hello'

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/create_ninja', methods=['POST'])
def create():
    print(request.form)
    session['first_name']=request.form ['name']
    session['location']=request.form ['location']
    session['language']=request.form ['language']
    session['comments']=request.form ['comments']
    return redirect("/show")

@app.route("/show")
def show():
    return render_template("submit.html")

@app.route('/create_ninja')
def home():
     return redirect('/')
if __name__ == '__main__':
    app.run(debug=True)
    
    