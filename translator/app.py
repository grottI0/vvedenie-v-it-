from flask import Flask, render_template, jsonify, request
import translate

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def start():
    return render_template('index.html')


@app.route('/translate-text', methods=['POST'])
def translate_text():
    data = request.get_json()
    text_input = data['text']
    translation_output = data['to']
    response = translate.get_translation(text_input, translation_output)
    return jsonify(response)


if __name__ == '__main__':
    app.run()
