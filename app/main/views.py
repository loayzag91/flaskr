from flask import render_template, session, redirect, url_for, flash, request
from . import main
from ..models import Entries, db
from app import config


@main.route('/')
def show_entries():
    entries = Entries.query.all()
    return render_template('show_entries.html', entries=entries)

@main.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    new_post = Entries(request.form['title'], request.form['text'])
    db.session.add(new_post)
    db.session.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('main.show_entries'))


@main.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != config.DevelopmentConfig.USERNAME:
            error = 'Invalid username'
        elif request.form['password'] != config.DevelopmentConfig.PASSWORD:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('main.show_entries'))
    return render_template('login.html', error=error)


@main.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('main.show_entries'))
