from flask import Flask

# __name__ = "__main__"
app = Flask(__name__)

@app.route("/")
def hello_word():
    return "Hello, World!"

@app.route("/about")
def about():
    return "This is the about page."    

if __name__ == "__main__":
    app.run(debug=True)