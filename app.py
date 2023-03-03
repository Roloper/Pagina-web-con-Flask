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
    
@app.route('/register', methods =['GET','POST'])
def register():
    if request.method == 'POST':
        return render_template('auth/AoE.html')
    else:
        return render_template('auth/AoE.html')

@app.route('/registerE', methods =['GET','POST'])
def registerE():
    if request.method == 'POST':
        return render_template('auth/registerE.html')
    else:
        return render_template('auth/registerE.html')

@app.route('/registerA', methods =['GET','POST'])
def registerA():
    if request.method == 'POST':
        return render_template('auth/registerA.html')
    else:
        return render_template('auth/registerA.html')

@app.route('/Home')
def Home():
    return  redirect(url_for('login'))

@app.route('/Mycart')
def Mycart():
    return  redirect(url_for('login'))

@app.route('/Pefil')
def Pefil():
    return  redirect(url_for('login'))

@app.route('/Mercado')
def Mercado():
    return  redirect(url_for('login'))

@app.route('/Mensaje')
def Mensaje():
    return  redirect(url_for('login'))


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()