from werkzeug.security import check_password_hash

class User():

    def __init__(self, id_empresa, id_dueno, e_nombre, e_username, e_password, e_email, e_celular, e_ubicacion, e_imagenperfil):
        self.id_empresa = id_empresa
        self.id_dueno = id_dueno
        self.e_nombre = e_nombre
        self.e_username = e_username
        self.e_password = e_password
        self.e_email = e_email
        self.e_celular = e_celular
        self.e_ubicacion = e_ubicacion
        self.e_imagenperfil = e_imagenperfil

    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)
