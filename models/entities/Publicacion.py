class Publicacion():
    def __init__(self, id_publicacion, id_usuario, titulo, contenido, imagen):
        self.id_publicacion = id_publicacion
        self.id_usuario = id_usuario
        self.titulo = titulo
        self.contenido = contenido
        self.imagen = imagen

    def get_id(self):
        return self.id_publicacion

