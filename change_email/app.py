from flask import Flask, render_template, session, request, redirect, url_for
import os
from datetime import timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=31)


@app.route('/', methods=['GET', 'POST'])
def index():
    if 'email' in request.form and not request.form['email'].endswith('@admin.scaict.com'):
        session['email'] = request.form['email']
    email = session.get('email', '')
    isAdmin = email.endswith('@admin.scaict.com')
    return render_template('index.html', email=email, isAdmin=isAdmin)


@app.route('/setting', methods=['GET', 'POST'])
def setting():
    if 'email' not in session:
        return redirect(url_for('index'))

    if 'email' not in request.form:
        return render_template('setting.html')

    session['email'] = request.form['email']
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=False)