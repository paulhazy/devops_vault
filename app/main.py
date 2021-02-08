from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def test():
    return render_template('index.html')

@app.route("/echo", methods=["POST"])
def test_post():
    txt = request.form.get('text')
    return f'<h1>{txt}</h1>'

if __name__ == '__main__':
    app.run(debug=True)