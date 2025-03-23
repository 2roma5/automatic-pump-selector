from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html", css_name="home.css")

if __name__ == "__main__":
    app.run(debug=True)
