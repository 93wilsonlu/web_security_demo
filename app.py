from flask import Flask, render_template, make_response, redirect, request, session, send_file
import os
from datetime import timedelta
from urllib.request import urlopen

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=31)

from logic_flaw_lab import logic_flaw_lab
app.register_blueprint(logic_flaw_lab, url_prefix='/logic_flaw_lab')

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
    if request.cookies.get('username') is None:
        response = make_response(render_template('cookie.html'))
        response.set_cookie('username', 'guest')
        return response
    elif request.cookies['username'] == 'admin':
        return 'SCAIST{1_c4n_ch4n63_c00k135!}'
    return render_template('cookie.html')


@app.route('/session', methods=['GET'])
def change_session():
    if session.get('username_sess') is None:
        session['username_sess'] = 'guest'
        session.permanent = True
    if session['username_sess'] == 'admin':
        return 'SCAIST{1_c4n_ch4n63_535510n!}'
    return render_template('cookie.html')


@app.route('/logic_flaw', methods=['GET'])
def logic_flaw():
    site = 'index.html'
    if session.get('username_sess') == 'admin':
        print('Admin in!')
    site = 'logic_flaw_flag.html'
    return render_template(site)



@app.route('/logic_flaw_number', methods=['GET', 'POST'])
def logic_flaw_number():
    if session.get('amount') is None:
        session['amount'] = 10
    
    if request.form.get('count') is not None:
        try:
            count = int(request.form['count'])
            if session['amount'] >= count * 10:
                session['amount'] -= count * 10
        except:
            pass
    return render_template('logic_flaw_number.html', amount=session['amount'])


@app.route('/path_traversal', methods=['GET'])
def path_traversal():
    if request.args.get('filename') is not None:
        return send_file('./'+request.args.get('filename'))
    return render_template('path_traversal.html')



@app.route('/command_injection', methods=['GET'])
def command_injection():
    if request.args.get('ip') is None:
        return render_template('command_injection.html')
    ip = request.args['ip']
    with os.popen('ping -c 3 ' + ip, 'r') as f:
        content = f.read()
    return content


@app.route('/ssrf', methods=['GET'])
def ssrf():
    if request.args.get('url') is None:
        return render_template('ssrf.html')
    url = request.args['url']
    with urlopen(url) as resp:
        content = resp.read().decode()
    return content
