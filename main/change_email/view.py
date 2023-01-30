from . import change_email
from flask import render_template, session, request, redirect, url_for


@change_email.route('/', methods=['GET', 'POST'])
def index():
    if 'email' in request.form and not request.form['email'].endswith('@admin.scaict.com'):
        session['email'] = request.form['email']
    email = session.get('email', '')
    isAdmin = email.endswith('@admin.scaict.com')
    return render_template('change_email/index.html', email=email, isAdmin=isAdmin)


@change_email.route('/setting', methods=['GET', 'POST'])
def setting():
    if 'email' not in session:
        return redirect(url_for('change_email.index'))

    if 'email' not in request.form:
        return render_template('change_email/setting.html')

    session['email'] = request.form['email']
    return redirect(url_for('change_email.index'))
