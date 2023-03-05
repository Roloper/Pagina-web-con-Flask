from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

class User(UserMixin):

    def __init__(self, id_usuario, a_name, a_username, a_password, a_email, a_descipcion, a_celular, a_ubicacion, a_imagenperfil):
        self.id_usuario = id_usuario
        self.a_name = a_name
        self.a_username = a_username
        self.a_password = a_password
        self.a_email = a_email
        self.a_descipcion = a_descipcion
        self.a_celular = a_celular
        self.a_ubicacion = a_ubicacion
        self.a_imagenperfil = a_imagenperfil

    def get_id(self):
        return self.id_usuario
    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)
