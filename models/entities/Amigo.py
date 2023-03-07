

class Amigo():

    def __init__(self, id_amigo, usuario_id, amigo_id, fecha_amistad):
        self.id_amigo = id_amigo
        self.usuario_id = usuario_id
        self.amigo_id = amigo_id
        self.fecha_amistad = fecha_amistad

    def get_id(self):
        return self.id_amigo

