from .entities.Publicacion import Publicacion


class ModelPublicaciones():

    @classmethod
    def create_publicacion(cls, db, public):
        try:
            cursor = db.connection.cursor()
            sql = """INSERT INTO publicaciones (id_usuario, titulo, contenido, imagen)
                     VALUES (%s, %s, %s, %s)"""
            cursor.execute(sql,(public.id_usuario, public.titulo, public.contenido, public.imagen))
            db.connection.commit()
            return True
        except Exception as ex:
            db.connection.rollback()
            raise Exception(ex)

    @classmethod
    def get_publicaciones_usuario(cls, db, id_usuario):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT * FROM publicaciones WHERE id_usuario = %s"""
            cursor.execute(sql, (id_usuario,))
            result = cursor.fetchall()
            publicaciones = []
            for row in result:
                publicacion = Publicacion(*row)
                publicaciones.append(publicacion)
            return publicaciones
        except Exception as ex:
            raise Exception(ex)