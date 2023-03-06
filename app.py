from flask import Flask, render_template, request, redirect, url_for, flash
from config import config
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.utils import secure_filename
from datetime import datetime
import os
import requests

# Models
from models import ModelPublicacion
from models.ModelPublicacion import ModelPublicaciones
from models.ModelUser import ModelUser

# Entities
from models.entities.Publicacion import Publicacion
from models.entities.User import User

app = Flask(__name__, template_folder='template')
csrf = CSRFProtect()
db = MySQL(app)
login_manager_app = LoginManager(app)

app.config['UPLOAD_FOLDER'] = 'static/img'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'NEF'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@login_manager_app.user_loader
def load_user(id_usuario):
    return ModelUser.get_by_id(db, id_usuario)


# URL PRINCIPAL
@app.route('/')
def index():
    return render_template('auth/index.html')


# URL PARA EL LOGIN
@app.route('/login', methods=['GET', 'POST'])  # persona o empresa
def login():
    if request.method == 'POST':
        user = User(0, 0, request.form['a_username'], request.form['a_password'], 0, 0, 0, 0, 0)
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


# URL DEL REGISTRO-
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        img_filename = ''
        if 'a_imagenperfil' in request.files:
            file = request.files['a_imagenperfil']
            if file.filename != '':
                img_filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], img_filename))

        user = User(
            None,
            request.form['a_name'],
            request.form['a_username'],
            User.hash_password(request.form['a_password']),
            request.form['a_email'],
            request.form['a_descripcion'],
            request.form['a_celular'],
            request.form['a_ubicacion'],
            img_filename
        )
        try:
            ModelUser.register(db, user)
            return redirect(url_for('login'))

        except Exception as ex:
            return str(ex)

    else:
        return render_template('auth/register.html')


# Redireccion para el cierre de sesion
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/buscar', methods=['GET','POST'])
def buscar():
    if request.method == 'POST':
        search_query = request.form['search_query']  # obtener el término de búsqueda
        # ejecutar una búsqueda en la base de datos para obtener resultados
        results = ModelUser.buscar_amigos(db, search_query)
        # renderizar la plantilla con los resultados
        return render_template('resultado_busqueda.html', results=results)
    else:
        # en caso de que el método no sea POST, redirigir al inicio
        return redirect(url_for('Home'))


# url de home para pagina principal
@app.route('/Home')
@login_required
def Home():
    return render_template('auth/home.html')


@app.route('/perfil', methods=['GET','POST'])
@login_required
def perfil():
    if request.method == 'POST':
        img_filename = ''
        if 'imagen' in request.files:
            file = request.files['imagen']
            if file.filename != '':
                img_filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], img_filename))

        publi = Publicacion(
            None,
            current_user.id_usuario,
            request.form['titulo'],
            request.form['contenido'],
            img_filename,
            datetime.now() # Agregamos la fecha actual
        )
        try:
            ModelPublicaciones.create_publicacion(db, publi)
            return redirect(url_for('perfil'))

        except Exception as ex:
            return str(ex)

    else:
        # publicaciones = Publicacion.query.all()
        publicaciones = ModelPublicaciones.get_publicaciones_usuario(db, current_user.id_usuario)
        return render_template('perfil/perfil.html', publicaciones=publicaciones)


@app.route('/chats')
@login_required
def chats():
    return render_template('Chat/chat_room.html')


@app.route('/carrito')
@login_required
def carrito():
    return render_template('carrito/mycart.html')


def status_401(error):
    return redirect(url_for('index'))


def status_404(error):
    return "<h1> Pagino no encontrada</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()
