from deep_translator import GoogleTranslator


def traduttore(testo, lingua_partenza, lingua_arrivo):
    try:
        traduzione= GoogleTranslator(source=lingua_partenza, target=lingua_arrivo).translate(testo)

        return traduzione
    except Exception as e:
        return e
    