from flask import render_template, session, redirect, url_for
from spider.hqyzm import hqyzm
from spider.mndl import mndl
from spider.pa import pa
from .forms import LoginForm
from . import main

s = None


@main.route('/', methods=['GET', 'POST'])
def index():
	form = LoginForm()
	if form.validate_on_submit():
		session['username'] = form.username.data
		session['password'] = form.password.data
		session['yzm'] = form.yzm.data
		return redirect(url_for('.login'))
	global s
	s = hqyzm()
	return render_template('index.html', form=form)


@main.route('/login')
def login():
	a = mndl(s, session['username'], session['password'], session['yzm'])
	b = pa(a)
	return render_template('a.html', a=b)
