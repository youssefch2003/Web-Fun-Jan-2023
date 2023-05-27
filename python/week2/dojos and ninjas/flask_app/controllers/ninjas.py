from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja







@app.route('/ninjas')
def newninja():
    dojos=Dojo.get_all()

    return render_template("new_ninja.html", dojos=dojos)

@app.route('/ninjas/create', methods=['POST'])
def createninja():
    Ninja.create_ninja(request.form)
    return redirect('/dojos/show/'+str(request.form['dojo_id']))