from flask import Flask, url_for, render_template, request, flash
from markupsafe import escape


app = Flask(__name__)
app.secret_key = "diipadaapa"

@app.route('/', methods=["GET", "POST"])
def index(name=None):
    return render_template("index.html", name=name)

@app.route('/submit', methods=["GET", "POST"])
def submit(name=None):
    luvut = []
    lampotila = 0

    if request.method == "POST":
        luku = request.form.get("annettu_luku")
        luvut.append(luku)

        mista = request.form.get("mista")
        mihin = request.form.get("mihin")
        
        print(luku)
        print(mista)
        print(mihin)

        lampotila = konvertteri(luku, mista, mihin)

        return flash(f"{lampotila} {mihin}")


def konvertteri(luku, mista, mihin):
        lampotila = 0
        if mista == "celcius":
            if mihin == "fahrenheit":
                lampotila = (float(luku) * 1.8) + 32
            elif mihin == "kelvin":
                lampotila = float(luku) + 273.15
            elif mihin == "celcius":
                return

        if mista == "fahrenheit":
            if mihin == "celcius":
                lampotila = (float(luku) - 32) * 1.8
            elif mihin == "kelvin":
                lampotila = (float(luku) + 459.67) * 0.5555555555555555555555
                lampotila = round(lampotila, 2)
            elif mihin == "fahrenheit":
                return

        if mista == "kelvin":
            if mihin == "celcius":
                lampotila = float(luku) - 273.15
            elif mihin == "fahrenheit":
                lampotila = float(luku) * 1.8 - 459.67
            elif mihin == "kelvin":
                return

        return lampotila
        


#@app.route("/data", methods=["POST"])
#def data():
#    luku = request.form.get("annettu_luku")
#    return f"annoit luvun {luku}"

with app.test_request_context():
    print(url_for('index'))
    print(url_for('submit'))