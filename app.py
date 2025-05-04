from flask  import Flask

app = Flask(__name__)

@app.route("/")
def homePage():
    return "Hello World"

@app.route("/employee")
def getEmployee():
    return {
        'name':"Akash",
        'age':36
    }

@app.route("/<int:a>/<int:b>")
def addNumber(a,b):
    return {
        'inputNumbers': f"{a} and {b}",
        'addition': a+b
    }

if(__name__ == "__main__"):
    app.run()