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
    
    x=User.create(request.form)
    
    return redirect('/users/'+str(x))




@app.route('/users/<int:user_id>')
def oneuser(user_id):
    data = {
        'id':user_id
    }
    user = User.get_one(data)
    print(user)
    return render_template('one_user.html', user = user)

if __name__ == '__main__':
    app.run(debug =True)