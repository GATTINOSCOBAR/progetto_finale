from flask import Flask, render_template
import jinja2

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('homepage.html')

@app.route("/inglese")
def inglese():
    return render_template('inglese.html')

@app.route("/lEn")
def lezione_inglese():
    return render_template('lezione_inglese.html')


app.run(debug=True)