## Flask app routing process


from flask import Flask,render_template,request


## create a simple application
app = Flask(__name__)

@app.route("/",methods=["Get"])
def welcome():
    return "<h1>Welcome to the MO Channel</h1>"

@app.route("/index",methods=["Get"])
def index():
    return "<h2>Welcome to the Index page</h2>"

#Variable rule to add values, with type casting defining data types

@app.route("/success/<int:score>")
def success(score):
    return f"<h3>The Person has passed and the score is: {score}</h3>"


#Varible rule for failure

@app.route("/fail/<int:score>")
def fail(score):
    return f"<h4>The Person has failed and the score is: {score}</h4>"


@app.route("/forms",methods=["GET","POST"])
def form():
    if request.method=="GET":
        return render_template("form.html")
    

if __name__ == '__main__':
    app.run(debug=True)