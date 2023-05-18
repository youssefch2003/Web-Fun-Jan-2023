from flask import Flask
app = Flask(__name__)

@app.route('/')

def hello():
    return "hello world"

@app.route('/dojo')
def dojo():
    return "dojo!"

@app.route('/hi/<string:a_name>')
def hi(a_name):
        return f"<h2> hi {a_name}</h2>"
   

@app.route('/hi/<a_name>/<int:time>')
def hi2(a_name,time ):
    return f"<h2> hi {a_name}</h2>" * time












if __name__ == "__main__":
    app.run(debug=True)