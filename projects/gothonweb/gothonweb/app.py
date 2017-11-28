from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/hello', methods=['POST', 'GET'])
def index():
    greeting = "Hello world"
    if request.method == "POST":
        name = request.form['name']
        greet = request.form['greet']
        greeting = f"{greet}, {name}"
        return render_template('index.html', greeting=greeting)
    else:
        return render_template("Hello_form.html")

@app.route('/foo')
def got():
    return render_template("foo.html")

if __name__ == "__main__":
    app.run()