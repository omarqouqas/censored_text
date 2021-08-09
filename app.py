from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    html_form = """
        <html><body>
            <h1> Enter some text and then enter some text parts/words that you'd like to be censored! </h1>
            <br>
            <br>
            <form action="" method="get">
            Original text that of your choice: <input type="text" name="text">
            <br>
            <br>
            censored part of text (letter/word/number): <input type="text" name="censored_word">
            <input type="submit" value="Text without censored parts >">
                </form>
        </body></html>"""

    text = request.args.get("text", "")
    censored_word = request.args.get("censored_word", "")
    if text and censored_word:
        censored_text = str(censor(text, censored_word))
        print(censored_text)
    else:
        censored_text = ""

    return html_form + censored_text


def censor(text, censored_word):
    print(text)
    original_text = text
    while True:
        censored_word = censored_word.lower()
        text = text.lower()
        word_position = text.find(censored_word)
        if word_position < 0:
            break
        text = text[:word_position] + len(censored_word) * "*" + text[word_position + len(censored_word):]
    return "Original text: " + original_text + \
           "\nCensored word: '" + censored_word + \
           "' " "\nCensored text is: " + text


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
