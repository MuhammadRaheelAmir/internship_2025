
from flask import Flask, render_template

## WSGI 
## __name__ : Entry point

app=Flask(__name__)

@app.route('/')
def greet():
    return "Welcome to this best flask application"

@app.route('/about')
def about():
    return "<html><h1>This is just a test project</h1><html>"

@app.route('/index')
def index():
    return render_template('index.html')



if __name__=='__main__':
    app.run(debug=True)