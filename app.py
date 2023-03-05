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

csrf=CSRFProtect()
db = MySQL(app)
login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id_usuario):
    return ModelUser.get_by_id(db, id_usuario)

#URL PRINCIPAL
@app.route('/')
def index():
    return render_template('auth/index.html')

#URL PARA EL LOGIN
@app.route('/login', methods = ['GET','POST']) #persona o empresa
def login():
    if request.method == 'POST':
        print(request.form['a_username'])
        print(request.form['a_password'])
        user = User(0,0,request.form['a_username'], request.form['a_password'],0,0,0,0,0)
        logged_user = ModelUser.login(db,user)

        if logged_user != None:
            if logged_user.a_password:
                login_user(logged_user)
                return redirect(url_for('Home'))
            else:
                print("contra incorrecta")
                flash("Contraseña Incorrecta")
                return render_template('auth/login.html')
        else:
            print("No se encontro usuario")
            flash("Usuario no encontrado")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

#Redireccion para el cierre de sesion
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

#URL DEL REGISTRO-
@app.route('/register', methods =['GET','POST'])
def register():
    if request.method == 'POST':
        user = User(
            None,
            request.form['a_name'],
            request.form['a_username'],
            User.hash_password(request.form['a_password']),
            request.form['a_email'],
            request.form['a_descripcion'],
            request.form['a_celular'],
            request.form['a_ubicacion'],
            request.form['a_imagenperfil']
        )

        try:
            ModelUser.register_user(db, user)
            return "Registro exitoso"
        except Exception as ex:
            return str(ex)

    else:
        return render_template('auth/register.html')

#url de home para pagina principal
@app.route('/Home')
@login_required
def Home():
    return  render_template('auth/home.html')
<<<<<<< HEAD
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

@app.route('/Chats')
def Chats():
    return  render_template('Chat/chat_room.html')

def status_401(error):
    return redirect(url_for('index'))

def status_404(error):
    return "<h1> Pagino no encontrada</h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401,status_401)
    app.register_error_handler(404, status_404)
    app.run()