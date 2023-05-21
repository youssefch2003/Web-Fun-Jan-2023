from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key='hellohi'

@app.route('/')
def form():
    return render_template('index.html')



@app.route('/process', methods=["post"])
def pross():
    session['name']= request.form['nom']
    session['location']= request.form['location']
    session['language']= request.form['language']
    session['txtarea']= request.form['area']
    
    return  redirect('/display')

@app.route('/display')
def disp():
    return render_template('display.html')




if __name__=='__main__':
    app.run(debug=True)