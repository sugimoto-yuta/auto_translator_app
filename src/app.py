from flask import Flask, request, render_template
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        sentence_ = request.form.get('sentence')
        if sentence_ == '':
            error_sentence = '文字を入力して下さい'
            return render_template('index.html', error=error_sentence)
        else:
            language_ = request.form.get('language')
            target = GoogleTranslator().get_supported_languages(as_dict=True).get(language_)
            translated_ = GoogleTranslator(source='auto', target=target).translate(sentence_)
            return render_template('index.html', sentence=sentence_, language=language_, translated=translated_)

    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)