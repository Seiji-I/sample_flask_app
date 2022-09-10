from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
  return "<h1>index page</h1>"

@app.route("/hello")
def hello():
  return "<h1>Hello</h1>"

@app.route("/goodbye")
def goodbye():
  return "<h1>Good Bye!</h1>"

@app.route("/hi")
def hi():
  return "<h1>Hi!</h1>"



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5555)