
from flask import Flask

## WSGI 
## __name__ : Entry point

app=Flask(__name__)

@app.route('/')
def greet():
    return "Welcome to this best flask application"



if __name__=='__main__':
    app.run(debug=True)