from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    greeting = 'Hello World'
    return render_template("index.html", greeting = greeting)

@app.route('/foo')
def foo():
    message = 'Hello from Foo'
    return render_template('foo.html', message = message)

if __name__ == '__main__':
    app.run()
