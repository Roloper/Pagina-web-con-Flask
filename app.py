from flask import Flask, render_template, request, redirect, url_for, flash
from config import config
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required

#Models
from models.ModelUser import ModelUser

#Entities
from models.entities.User import User

app = Flask(__name__, template_folder='template')

db = MySQL(app)

#URL PRINCIPAL
@app.route('/')
def index():
    return redirect(url_for('login'))

#URL PARA EL LOGIN
@app.route('/login', methods = ['GET','POST']) #persona o empresa
def login():
    if request.method == 'POST':
        #print(request.form['username'])
        #print(request.form['password'])
        user = User(0,0,0,request.form['username'], request.form['password'],0,0,0,0)
        logged_user = ModelUser.login(db,user)

        if logged_user != None:
            if logged_user.e_password:
                return redirect(url_for('Home'))
            else:
                flash("Contraseña Incorrecta")
                return render_template('auth/login.html')
        else:
            flash("Usuario no encontrado")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

# #URL DEL REGISTRO (ELEGIR OPCION)
# @app.route('/register', methods =['GET','POST'])
# def register():
#     if request.method == 'POST':
#         return render_template('auth/AoE.html')
#     else:
#         return render_template('auth/AoE.html')
#
# @app.route('/registerE', methods =['GET','POST'])
# def registerE():
#     if request.method == 'POST':
#         return render_template('auth/registerE.html')
#     else:
#         return render_template('auth/registerE.html')

# @app.route('/registerA', methods =['GET','POST'])
# def registerA():
#     if request.method == 'POST':
#         return render_template('auth/registerA.html')
#     else:
#         return render_template('auth/registerA.html')
#
@app.route('/Home')
def Home():
    return  render_template('auth/home.html')
#
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