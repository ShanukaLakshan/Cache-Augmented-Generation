from deep_translator import GoogleTranslator

def translate_response(response: str, target_language: str):
    translator = GoogleTranslator(source="en", target=target_language)
    return translator.translate(response)
