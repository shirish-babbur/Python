from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    greeting = 'YO! How\'s you doing'
    return render_template("index.html", greeting = greeting)

@app.route('/foo')
def got():
    return render_template("foo.html")

if __name__ == "__main__":
    app.run()
