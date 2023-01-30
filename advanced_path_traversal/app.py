from flask import Flask, render_template, request, send_file

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    if 'filename' in request.args:
        filename = request.args['filename'].replace('../', '')
        return send_file('images/' + filename)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=False)