from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    if 'ip' not in request.args:
        return render_template('index.html')
    ip = request.args['ip']
    if 'flag.txt' in ip:
        return 'Bad hacker! You cannot read flag.txt'
    if 'cat' in ip:
        return 'Don\'t touch my cat!'
    ip = ip.replace(';', '')
    ip = ip.replace(' ', '')
    with os.popen('ping -c 1 ' + ip, 'r') as f:
        content = f.read()
    return content


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10005, debug=False)