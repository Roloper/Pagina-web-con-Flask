from flask import Flask, render_template, request, redirect, url_for, flash
from config import config
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required
from werkzeug.utils import secure_filename
import os
#Models
from models.ModelUser import ModelUser

#Entities
from models.entities.User import User

app = Flask(__name__, template_folder='template')
csrf=CSRFProtect()
db = MySQL(app)
login_manager_app = LoginManager(app)
app.config['UPLOAD_FOLDER'] = 'uploads'

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'net'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS




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
                return redirect(url_for('home'))
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
        # Validar que el archivo sea una imagen .png
        if 'a_imagenperfil' not in request.files:
            flash('No se seleccionó ningún archivo')
            return redirect(request.url)
        file = request.files['a_imagenperfil']
        if file.filename == '':
            flash('No se seleccionó ningún archivo')
            return redirect(request.url)
        if not allowed_file(file.filename):
            flash('Solo se permiten archivos con extensión .png')
            return redirect(request.url)
        filename = secure_filename(file.filename)

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
            filename
        )
        try:
            ModelUser.register(db, user)
            return "Registro exitoso"
        except Exception as ex:
            return str(ex)

    else:
        return render_template('auth/register.html')

#url de home para pagina principal
@app.route('/home')
@login_required
def home():
    return  render_template('auth/home.html')

@app.route('/perfil')
def perfil():
    return  render_template('./perfil/perfil.html')


@app.route('/chats')
def chats():
    return  render_template('Chat/chat_room.html')

@app.route('/carrito')
def carrito():
    return  render_template('carrito/mycart.html')


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