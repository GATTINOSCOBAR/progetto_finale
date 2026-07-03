from flask import Flask, render_template, request
from trascrittore import trascrittore
from traduttore import traduttore
import random


app = Flask(__name__)

parole = ['cane', 'gatto', 'topo', 'casa', 'albero', 'sole', 'luna', 'stella', 'mare', 'montagna', 'fiume', 'lago', 'cielo', 'nuvola', 'pioggia', 'vento', 'neve', 'fiore', 'prato', 'bosco', 'strada', 'città', 'paese', 'scuola', 'libro', 'penna', 'quaderno', 'zaino', 'banco', 'sedia', 'tavolo', 'finestra', 'porta', 'muro', 'tetto', 'giardino', 'cane', 'gatto', 'cavallo', 'uccello', 'pesce', 'farfalla', 'ape', 'formica', 'bambino', 'ragazza', 'uomo', 'donna', 'amico', 'famiglia', 'madre', 'padre', 'fratello', 'sorella', 'nonno', 'nonna', 'sorriso', 'occhi', 'mani', 'piedi', 'cuore', 'mente', 'voce', 'musica', 'canzone', 'arte', 'quadro', 'colore', 'rosso', 'blu', 'verde', 'giallo', 'nero', 'bianco', 'arancione', 'viola', 'grigio', 'cibo', 'pane', 'pasta', 'pizza', 'riso', 'mela', 'pera', 'banana', 'arancia', 'fragola', 'acqua', 'latte', 'caffè', 'tè', 'zucchero', 'sale', 'lavoro', 'ufficio', 'computer', 'telefono', 'internet', 'schermo', 'tastiera', 'mouse', 'programma', 'gioco', 'sport', 'calcio', 'basket', 'tennis', 'corsa', 'bicicletta', 'viaggio', 'treno', 'autobus', 'automobile', 'aereo', 'nave', 'valigia', 'mappa', 'fotografia', 'film', 'teatro', 'museo', 'biblioteca', 'mercato', 'negozio', 'denaro', 'tempo', 'giorno', 'notte', 'mattina', 'pomeriggio', 'sera', 'settimana', 'mese', 'anno', 'estate', 'inverno', 'primavera', 'autunno', 'felicità', 'speranza', 'coraggio', 'pace', 'libertà', 'sogno', 'futuro', 'passato', 'presente', 'successo', 'idea', 'progetto', 'energia', 'natura', 'universo']


@app.route("/")
def homepage():
    return render_template('homepage.html')


@app.route("/inglese", methods=['GET', 'POST'])
def inglese():
    traduzione = None
    parola = random.choice(parole)
    esito_vocale = None
    esito_scritto = None
    soluzione = None
    trascrizione_vocale = None



    if request.method == "POST":
        parola = request.form.get('parola')
        soluzione = traduttore(parola, 'it', 'en')

        trascrizione_vocale = trascrittore('en-EN')
        traduzione_input = request.form.get('traduzione')

        if not trascrizione_vocale:
            esito_vocale = "Errore: nessun audio rilevato o trascrizione fallita."
        else:
            if trascrizione_vocale.strip().lower() == soluzione.strip().lower():
                esito_vocale = "Hai risposto correttamente!"
            else:
                esito_vocale = (
                    f"Hai risposto male! Hai detto: '{trascrizione_vocale}'. "
                    f"La traduzione corretta era: {soluzione}"
                )

        if traduzione_input:
            if traduzione_input.strip().lower() == soluzione.strip().lower():
                esito_scritto = "Hai risposto correttamente!"
            else:
                esito_scritto = (
                    f"Hai risposto male! La traduzione corretta era: {soluzione}"
                )

    return render_template(
        'inglese.html',
        traduzione=traduzione,
        parola=parola,
        esito_vocale=esito_vocale,
        esito_scritto=esito_scritto,
        soluzione=soluzione,
        trascrizione_vocale=trascrizione_vocale
    )


@app.route("/spagnolo", methods=['GET', 'POST'])
def spagnolo():
    traduzione = None
    parola = random.choice(parole)
    esito_vocale = None
    esito_scritto = None
    soluzione = None
    trascrizione_vocale = None



    if request.method == "POST":
        parola = request.form.get('parola')
        soluzione = traduttore(parola, 'it', 'es')

        trascrizione_vocale = trascrittore('es-ES')
        traduzione_input = request.form.get('traduzione')

        if not trascrizione_vocale:
            esito_vocale = "Errore: nessun audio rilevato o trascrizione fallita."
        else:
            if trascrizione_vocale.strip().lower() == soluzione.strip().lower():
                esito_vocale = "Hai risposto correttamente!"
            else:
                esito_vocale = (
                    f"Hai risposto male! Hai detto: '{trascrizione_vocale}'. "
                    f"La traduzione corretta era: {soluzione}"
                )

        if traduzione_input:
            if traduzione_input.strip().lower() == soluzione.strip().lower():
                esito_scritto = "Hai risposto correttamente!"
            else:
                esito_scritto = (
                    f"Hai risposto male! La traduzione corretta era: {soluzione}"
                )

    return render_template(
        'spagnolo.html',
        traduzione=traduzione,
        parola=parola,
        esito_vocale=esito_vocale,
        esito_scritto=esito_scritto,
        soluzione=soluzione,
        trascrizione_vocale=trascrizione_vocale
    )


@app.route("/francese", methods=['GET', 'POST'])
def francese():
    traduzione = None
    parola = random.choice(parole)
    esito_vocale = None
    esito_scritto = None
    soluzione = None
    trascrizione_vocale = None



    if request.method == "POST":
        parola = request.form.get('parola')
        soluzione = traduttore(parola, 'it', 'fr')

        trascrizione_vocale = trascrittore('fr-FR')
        traduzione_input = request.form.get('traduzione')

        if not trascrizione_vocale:
            esito_vocale = "Errore: nessun audio rilevato o trascrizione fallita."
        else:
            if trascrizione_vocale.strip().lower() == soluzione.strip().lower():
                esito_vocale = "Hai risposto correttamente!"
            else:
                esito_vocale = (
                    f"Hai risposto male! Hai detto: '{trascrizione_vocale}'. "
                    f"La traduzione corretta era: {soluzione}"
                )

        if traduzione_input:
            if traduzione_input.strip().lower() == soluzione.strip().lower():
                esito_scritto = "Hai risposto correttamente!"
            else:
                esito_scritto = (
                    f"Hai risposto male! La traduzione corretta era: {soluzione}"
                )

    return render_template(
        'francese.html',
        traduzione=traduzione,
        parola=parola,
        esito_vocale=esito_vocale,
        esito_scritto=esito_scritto,
        soluzione=soluzione,
        trascrizione_vocale=trascrizione_vocale
    )
@app.route("/tedesco", methods=['GET', 'POST'])
def tedesco():
    traduzione = None
    parola = random.choice(parole)
    esito_vocale = None
    esito_scritto = None
    soluzione = None
    trascrizione_vocale = None



    if request.method == "POST":
        parola = request.form.get('parola')
        soluzione = traduttore(parola, 'it', 'de')

        trascrizione_vocale = trascrittore('de-DE')
        traduzione_input = request.form.get('traduzione')

        if not trascrizione_vocale:
            esito_vocale = "Errore: nessun audio rilevato o trascrizione fallita."
        else:
            if trascrizione_vocale.strip().lower() == soluzione.strip().lower():
                esito_vocale = "Hai risposto correttamente!"
            else:
                esito_vocale = (
                    f"Hai risposto male! Hai detto: '{trascrizione_vocale}'. "
                    f"La traduzione corretta era: {soluzione}"
                )

        if traduzione_input:
            if traduzione_input.strip().lower() == soluzione.strip().lower():
                esito_scritto = "Hai risposto correttamente!"
            else:
                esito_scritto = (
                    f"Hai risposto male! La traduzione corretta era: {soluzione}"
                )

    return render_template(
        'tedesco.html',
        traduzione=traduzione,
        parola=parola,
        esito_vocale=esito_vocale,
        esito_scritto=esito_scritto,
        soluzione=soluzione,
        trascrizione_vocale=trascrizione_vocale
    )



app.run(debug=True)