## Flask app routing process


from flask import Flask


## create a simple application
app = Flask(__name__)

@app.route("/",methods=["Get"])
def welcome():
    return "<h1>Welcome to the MO Channel</h1>"

@app.route("/index",methods=["Get"])
def index():
    return "<h2>Welcome to the Index page</h2>"



if __name__ == '__main__':
    app.run(debug=True)