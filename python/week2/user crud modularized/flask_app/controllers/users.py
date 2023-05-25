from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.user import User

@app.route('/')
def index():
    users = User.get_all()
    return render_template('index.html', users=users)

@app.route('/users/new')
def new_user():

    return render_template('new_user.html')

@app.route('/users/create',methods=['POST'])
def create():
    User.create(request.form)
    return redirect('/')

@app.route('/users/show/<int:user_id>')
def showone(user_id):
    data ={
        'id':user_id
    }
    user = User.get_one(data)
    print(user)
    return render_template('one_user.html',user=user)


@app.route('/users/show/<int:user_id>/edit')
def edit(user_id):
    user = User.get_one({'id':user_id})
    return render_template('edit.html',user = user)


@app.route('/users/update/<int:user_id>/', methods=['post'])
def updateuser(user_id):
    User.update(request.form)
    return redirect('/')

@app.route('/users/delete/<int:user_id>/')
def remove(user_id):
    data ={
        'id':user_id
    }
    User.delete(data)
    return redirect('/')

    
