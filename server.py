from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello_world!'

@app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "Hello, " + name

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def say_hi(name):
    print(name)
    return "Hi " + name

@app.route('/repeat/<num>/<text>')
def repeater(num, text):
    return f"{text}<br>" * int(num)

@app.errorhandler(404)
def no_response(wrong):
    return "Sorry! No response. Try again."

if __name__=="__main__":
    app.run(debug=True)

