import os
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/calculator')
def calculator():
    #return a + b result from the url query string
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    if a == 0 or b == 0:
        return 'Please provide a and b query parameters'
    return str(a - b)

if __name__ == '__main__':
   app.run(host=os.getenv("PYTHON_HOST", "127.0.0.1"), port=os.getenv("PYTHON_PORT", "5000"))