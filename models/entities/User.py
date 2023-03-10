from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

class User(UserMixin):

    def __init__(self, id_usuario, a_name, a_username, a_password, a_email, a_descripcion, a_celular, a_ubicacion, a_imagenperfil):
        self.id_usuario = id_usuario
        self.a_name = a_name
        self.a_username = a_username
        self.a_password = a_password
        self.a_email = a_email
        self.a_descripcion = a_descripcion
        self.a_celular = a_celular
        self.a_ubicacion = a_ubicacion
        self.a_imagenperfil = a_imagenperfil

    def get_id(self):
        return self.id_usuario
    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)

    @staticmethod
    def hash_password(password):
        return generate_password_hash(password)



#print(User.check_password('pbkdf2:sha256:260000$WuxTsXivJXCtlxPp$c1168c24862b68e9356bdd86866fdc2b4468eee91e8997cbe6941a9b1a0fef80','12345'))