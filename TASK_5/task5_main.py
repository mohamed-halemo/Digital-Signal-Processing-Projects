from flask import Flask,render_template,url_for,flash,redirect,request
app= Flask(__name__)
@app.route("/")
def home():
    return render_template("Main.html")


if __name__ == "__main__":
    app.run()

