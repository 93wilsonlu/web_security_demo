from . import logic_flaw_lab
from flask import render_template, session, request, redirect, url_for


@logic_flaw_lab.route('/', methods=['GET', 'POST'])
def index():
    if request.form.get('email') is not None and not request.form['email'].endswith('@admin.com'):
        session['email'] = request.form['email']
    email = session.get('email') or ''
    isAdmin = email.endswith('@admin.com')
    return render_template('logic_flaw_lab/index.html', email=email, isAdmin=isAdmin)


@logic_flaw_lab.route('/setting', methods=['GET', 'POST'])
def setting():
    if session.get('email') is None:
        return redirect(url_for('logic_flaw_lab.index'))

    if request.form.get('email') is None:
        return render_template('logic_flaw_lab/setting.html')

    session['email'] = request.form['email']
    return redirect(url_for('logic_flaw_lab.index'))
