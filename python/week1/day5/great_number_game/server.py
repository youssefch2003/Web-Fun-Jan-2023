from flask import Flask,render_template,redirect,session, request
import random
app=Flask(__name__)
app.secret_key = "lalalalalalal"

@app.route('/')
def hello():
    if  'num' not in session :
        session['num']= random.randint(1, 100) 
    if 'choice ' not in session :
        session['choice']=1

    return render_template('index.html')
   
@app.route('/check',methods=['post'])
def check():
    session['choice'] = int( request.form['ran'])
        
    return redirect('/')

@app.route('/res')
def res():
    session.clear()
    
    return redirect('/')










if __name__ == '__main__':
    app.run(debug=True)
