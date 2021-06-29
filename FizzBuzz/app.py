from flask import Flask
from flask.templating import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/fizzbuzz/<int:line_count>')
def fizzbuzz(line_count):
    l = []
    for i in range(1, line_count + 1):
        if (i % 3 == 0) and (i % 5 == 0):
            l.append("FizzBuzz")
        elif i % 3 == 0:
            l.append("Fizz")
        elif i % 5 == 0:
            l.append("Buzz") 
        else:
            l.append(i)
    return render_template('fizzbuzz.html', line_count=line_count, l=l)