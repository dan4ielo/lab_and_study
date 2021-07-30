from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/hello', methods=['POST', 'GET'])
def index():
    
    greeting = 'Hello, World'
    
    if request.method == 'POST':
        name = request.form['name']
        greet = request.form['greet']
        greeting = '{}, {}'.format(greet, name)
        return render_template('index.html', greeting = greeting)
    else:
        return render_template('hello_form.html')

#    name = request.args.get('name', 'Nobody')
#    greet = request.args.get('greet', 'Hello')

#    if name:
#        greeting = '{}, {}'.format(greet, name)
#    else:
#        greeting = 'Hello, world'

#    return render_template("index.html", greeting = greeting)

if __name__ == '__main__':
    app.run()
