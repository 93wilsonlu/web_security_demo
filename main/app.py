from flask import Flask, render_template, make_response, redirect, request, session, url_for, abort
import os
from datetime import timedelta
import subprocess

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=31)


@app.route('/free_flag', methods=['GET'])
def free_flag():
    return render_template('free_flag.html')


@app.route('/get_form', methods=['GET'])
def get_form():
    return render_template('get_form.html', username=request.args.get('username'))


@app.route('/post_form', methods=['GET', 'POST'])
def post_form():
    return render_template('post_form.html', username=request.form.get('username'))


@app.route('/302', methods=['GET'])
def halt_redirect_index():
    return render_template('302.html')


@app.route('/302-flag', methods=['GET'])
def halt_redirect():
    response = make_response(redirect(url_for('halt_redirect_index')))
    response.status_code = 302
    response.headers['Flag'] = 'NCHU{Red1r3Ct_is_cO0l!}'
    return response


@app.route('/cookie', methods=['GET'])
def change_cookie():
    if 'username' not in request.cookies:
        response = make_response(render_template('cookie.html'))
        response.set_cookie('username', 'guest')
        return response
    elif request.cookies['username'] == 'admin':
        return 'NCHU{1_c4n_ch4ng3_c00ki3s!}'
    return render_template('cookie.html')


@app.route('/session', methods=['GET'])
def change_session():
    if 'username_sess' not in session:
        session['username_sess'] = 'guest'
        session['Flag'] = 'NCHU{S0m3_s3ss10n_i5_r3ad4ble}'
        session.permanent = True
    if session['username_sess'] == 'admin':
        return 'NCHU{1_c4n_ch4ng3_s3ss10n!}'
    return render_template('cookie.html')


@app.route('/logic_flaw_number', methods=['GET', 'POST'])
def logic_flaw_number():
    if 'amount' not in session:
        session['amount'] = 10

    if 'count' in request.form:
        try:
            count = int(request.form['count'])
            if session['amount'] >= count * 10:
                session['amount'] -= count * 10
        except:
            pass
    return render_template('logic_flaw_number.html', amount=session['amount'])


@app.route('/broken_role', methods=['GET', 'POST'])
def broken_role():
    if 'role' not in request.args:
        return redirect(url_for('broken_role', role=1))

    return render_template('broken_role.html', role=request.args['role'])


@app.route('/ssrf', methods=['GET'])
def ssrf():
    if 'url' not in request.args:
        return render_template('ssrf.html')
    url = request.args['url']
    return subprocess.check_output(['curl', '-L', url])


@app.route('/ssrf_target', methods=['GET'])
def ssrf_target():
    if request.remote_addr != '127.0.0.1':
        abort(404)
    return 'NCHU{$$rf_c4n_9o_4nywh3r3!}'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=False)