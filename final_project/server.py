from machinetranslation import translator
from flask import Flask, render_template, request, jsonify

app = Flask("Web Translator", template_folder="machinetranslation/templates")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    if not textToTranslate:
        return jsonify({'error': 'Invalid input: Text to translate is missing.'}), 400

    translatedText = translator.english_to_french(textToTranslate)
    return jsonify({'translation': translatedText})

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    if not textToTranslate:
        return jsonify({'error': 'Invalid input: Text to translate is missing.'}), 400

    translatedText = translator.french_to_english(textToTranslate)
    return jsonify({'translation': translatedText})

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
