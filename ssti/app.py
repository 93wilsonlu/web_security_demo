from flask import Flask, request, render_template, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'name' in request.form:
        print('<h1>Hello '+request.form['name'] + '</h1>')
        return render_template_string('<h1>Hello '+request.form['name'] + '</h1>')
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8308, debug=False)