from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja
@app.route('/dojos')
def index():
    dojos = Dojo.get_all()
    return render_template("index.html", dojos=dojos)

@app.route('/dojos/create', methods=['POST'])
def create():
    Dojo.create_dojo(request.form)
    return redirect('/dojos')


@app.route('/dojos/show/<int:dojo_id>')
def one_dojo(dojo_id):
    data = {
        'id':dojo_id,
        'dojo_id':dojo_id
        }
    ninjas = Ninja.get_dojo_ninjas(data)
    return render_template("show.html",ninjas=ninjas)