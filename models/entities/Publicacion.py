class Publicacion():
    def __init__(self, id_publicacion, id_usuario, titulo, contenido, imagen, fecha_publicacion):
        self.id_publicacion = id_publicacion
        self.id_usuario = id_usuario
        self.titulo = titulo
        self.contenido = contenido
        self.imagen = imagen
        self.fecha_publicacion = fecha_publicacion

    def get_id(self):
        return self.id_publicacion

