#!/usr/bin/python3
""" Flask web Application """

from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from passlib.hash import sha256_crypt
from flask_mysqldb import MySQL
from functools import wraps

from db_storage import *
from forms import *

# other dependencies
import time

# initialize the app
app = Flask(__name__)


# configure mysql
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'cybercell'
app.config['MYSQL_PASSWORD'] = 'CyberCellCoin_dev_2021'
app.config['MYSQL_DB'] = 'CCC'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# initialize mysql
mysql = MySQL(app)

# wrap to define if the user is currently logged in from session


def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("Unauthorized, please login.", "danger")
            return redirect(url_for('login'))
    return wrap

# log in the user by updating session


def log_in_user(username):
    users = Table("users", "name", "email", "username", "password")
    user = users.getone("username", username)

    session['logged_in'] = True
    session['username'] = username
    session['name'] = user.get('name')
    session['email'] = user.get('email')

# Registration page


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)

    if request.method == 'POST' and form.validate():
        username = form.username.data
        email = form.email.data
        name = form.name.data

        if isnewuser(username) and isnewtable(username):
            password = form.password.data

            sql_raw(
                "INSERT INTO users(name,email,username,password)" +
                "VALUES(\"%s\", \"%s\", \"%s\", \"%s\")" % (
                    name, email, username, password
                )
            )

            send_money(username, 0, True)
            log_in_user(username)
            sflash('Welcome to your dashboard %s.' %username)
            return redirect(url_for('dashboard'))

        else:
            dflash('User already exists.')
            return redirect(url_for('register'))

    return render_template('register.html', form=form)

# Login page


@app.route("/login", methods=['GET', 'POST'])
def login():
    # if form is submitted
    if request.method == 'POST':
        # collect form data
        username = request.form['username']
        candidate = request.form['password']

        # access users table to get the user's actual password
        users = Table("users", "name", "email", "username", "password")
        user = users.getone("username", username)
        accPass = user.get('password')

        # if the password cannot be found, the user does not exist
        if accPass is None:
            flash("Username is not found", 'danger')
            return redirect(url_for('login'))
        else:
            # verify that the password entered matches the actual password
            if accPass:
                # log in the user and redirect to Dashboard page
                log_in_user(username)
                flash('You are now logged in.', 'success')
                return redirect(url_for('dashboard'))
            else:
                # if the passwords do not match
                flash("Invalid password", 'danger')
                return redirect(url_for('login'))

    return render_template('login.html')

# Transaction page


@app.route("/transaction", methods=['GET', 'POST'])
@is_logged_in
def transaction():
    form = SendMoneyForm(request.form)
    balance = get_balance(session.get('username'))

    # if form is submitted
    if request.method == 'POST':
        try:
            # attempt to execute the transaction
            send_money(session.get('username'),
                       form.username.data, form.amount.data)
            flash("Money Sent!", "success")
        except Exception as e:
            flash(str(e), 'danger')

        return redirect(url_for('transaction'))

    return render_template('transaction.html', balance=balance, form=form, page='transaction')

# Buy page


@app.route("/buy", methods=['GET', 'POST'])
@is_logged_in
def buy():
    form = BuyForm(request.form)
    balance = get_balance(session.get('username'))

    if request.method == 'POST':
        # attempt to buy amoun
        send_money("BANK", session.get('username'), form.amount.data)
        flash("Purchase Successful!", "success")
        

        return redirect(url_for('dashboard'))

    return render_template('buy.html', balance=balance, form=form, page='buy')

# logout the user. Ends current session


@app.route("/logout")
@is_logged_in
def logout():
    session.clear()
    flash("Logout success", "success")
    return redirect(url_for('login'))

# Dashboard page


@app.route("/dashboard")
@is_logged_in
def dashboard():
    balance = get_balance(session.get('username'))
    blockchain = get_blockchain().chain
    ct = time.strftime("%I:%M %p")
    return render_template('dashboard.html', balance=balance, session=session, ct=ct, blockchain=blockchain, page='dashboard')

# Index page


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')


# Run app
if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True)