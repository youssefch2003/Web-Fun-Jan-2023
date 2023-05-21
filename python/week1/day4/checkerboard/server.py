from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html",c=int(6),l=int(6),color1="red",color2="blue")
@app.route('/<int:c>')
def two(c):
    return render_template("index.html",c=int(c),l=int(6),color1="yellow",color2="black")	




if __name__=="__main__":
    app.run(debug=True)