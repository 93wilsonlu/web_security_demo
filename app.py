from flask import Flask, render_template, make_response, redirect, request, session
import os
from datetime import timedelta
from urllib.request import urlopen

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=31)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/get_form', methods=['GET'])
def get_form():
    return render_template('get_form.html', username=request.args.get('username'))


@app.route('/post_form', methods=['GET', 'POST'])
def post_form():
    return render_template('post_form.html', username=request.form.get('username'))


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


@app.route('/ssrf', methods=['GET'])
def ssrf():
    url = request.args['url']
    with urlopen(url) as resp:
        content = resp.read().decode()
    return content
