import flask
import subprocess

app = flask.Flask(__name__)

@app.route("/")
def hello():
#    cmd = ['ipconfig']
#    sub = subprocess.check_output(cmd, shell=True)
    user = {'username' : 'TEST'}
    return flask.render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)