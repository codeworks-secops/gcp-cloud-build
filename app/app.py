from flask import Flask
from flask import render_template
import socket
import os

app = Flask(__name__)

count = 0

@app.route('/', methods=["GET"])
@app.route('/hello/', methods=["GET"])
@app.route('/hello/<name>', methods=["GET"])
def hello(name=None):
    global count
    count += 1

    return render_template('hello.html', host=socket.gethostname(), name=name, count=count)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
