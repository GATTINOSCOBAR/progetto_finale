from flask import Flask, render_template, request
import jinja2
from trascrittore import trascrittore
from traduttore import traduttore


app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('homepage.html')

@app.route("/inglese")
def inglese():
    return render_template('inglese.html')

@app.route("/lEn")
def lezione_inglese():
    traduzione = None
    if request.method == "POST":
        trascrizione = trascrittore()
        if trascrizione:
            traduzione = traduttore(trascrizione, 'it', 'en')
        else:
            traduzione = "Errore: nessun audio rilevato o trascrizione fallita."
    return render_template('lezione_inglese.html', traduzione=traduzione)


app.run(debug=True)