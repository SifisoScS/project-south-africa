try:
    from googletrans import Translator
except Exception:
    Translator = None

def translate_text(text, dest='en'):
    if Translator is None:
        return text
    t = Translator()
    return t.translate(text, dest=dest).text
