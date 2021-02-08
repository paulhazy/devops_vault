from flask import Flask, render_template
import subprocess
from flask import request

app = Flask(__name__)

@app.route("/")
def test():
    return render_template('index.html')

@app.route("/echo", methods=["POST"])
def test_post():
    return request.form['text']
#    ar = request.args.get('txt')

if __name__ == '__main__':
    app.run(debug=True)