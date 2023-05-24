from flask import Flask,render_template,request,session,redirect
from user import User
app=Flask(__name__)

@app.route('/')
def index():
    user = User.get_all()
    return render_template("index.html", user = user)
@app.route('/users/new')
def new_user():
    return render_template('new_user.html')
@app.route('/users/create',methods=['POST'])
def create():
    User.create(request.form)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug =True)