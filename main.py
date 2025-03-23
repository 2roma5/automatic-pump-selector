from flask import Flask, render_template
from core.units import Q_, convert_units

app = Flask(__name__)

@app.route('/')
def index():
    flow = Q_(1, 'meter ** 3 / second')
    flow = convert_units(flow, 'gallon / minute')
    return render_template("home.html", css_name="home.css", flow=flow)

if __name__ == "__main__":
    app.run(debug=True)
