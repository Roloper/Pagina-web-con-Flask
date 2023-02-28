from flask import Flask, render_template, request, redirect, url_for
from config import config

app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods = ['GET','POST']) #persona o empresa
def login():
    if request.method == 'POST':
        print(request.form['username'])
        print(request.form['password'])
        return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

@app.route('/Perfil')
def perfil():
    return  redirect(url_for('login'))



if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()