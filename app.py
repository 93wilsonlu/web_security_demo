from flask import Flask, render_template, make_response, redirect, request, session
import os
from datetime import timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=31)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/302', methods=['GET'])
def halt_redirect():
    response = make_response(redirect('/'))
    response.status_code = 302
    response.headers['Flag'] = 'SCAIST{Red1r3Ct_is_cO0l!}'
    return response

@app.route('/cookie', methods=['GET'])
def change_cookie():
    if not request.cookies.get('username'):
        response = make_response(render_template('cookie.html'))
        response.set_cookie('username', 'guest')
        return response
    elif request.cookies['username'] == 'admin':
        return 'SCAIST{1_c4n_ch4n63_c00k135!}'
    return render_template('cookie.html')

@app.route('/session', methods=['GET'])
def change_session():
    if not session.get('username_sess'):
        session['username_sess'] = 'guest'
        session.permanent = True
    if session['username_sess'] == 'admin':
        return 'SCAIST{1_c4n_ch4n63_535510n!}'
    return render_template('cookie.html')
