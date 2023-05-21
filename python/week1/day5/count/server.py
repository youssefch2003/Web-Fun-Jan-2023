from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key='hellohi'

@app.route('/')
def dis():
    if 'count' in session:
        session['count']+=1
    else:
        session['count']=1
    return render_template("index.html")

@app.route('/destroy')
def dest():
    session.clear()
    return redirect('/')









if __name__=="__main__":
    app.run(debug=True)