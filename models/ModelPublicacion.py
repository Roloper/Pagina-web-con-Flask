from .entities.Publicacion import Publicacion


class ModelPublicaciones():

    @classmethod
    def get_publicaciones_by_user_id(cls, db, id_usuario):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id_publicacion, id_usuario, titulo, contenido, imagen, fecha_publicacion
                         FROM publicaciones
                         WHERE id_usuario = '{}' """.format(id_usuario)
            cursor.execute(sql)
            rows = cursor.fetchall()
            publicaciones = []
            for row in rows:
                publicaciones.append(Publicacion(*row))
            return publicaciones
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def create_publicacion(cls, db, id_usuario, titulo, contenido, imagen=None):
        try:
            cursor = db.connection.cursor()
            sql = """INSERT INTO publicaciones (id_usuario, titulo, contenido, imagen)
                         VALUES ('{}', '{}', '{}', {})""".format(id_usuario, titulo, contenido,
                                                                 "NULL" if not imagen else f"'{imagen}'")
            cursor.execute(sql)
            db.connection.commit()
            return cursor.lastrowid
        except Exception as ex:
            db.connection.rollback()
            raise Exception(ex)

    @classmethod
    def delete_publicacion(cls, db, id_publicacion):
        try:
            cursor = db.connection.cursor()
            sql = """DELETE FROM publicaciones WHERE id_publicacion = '{}'""".format(id_publicacion)
            cursor.execute(sql)
            db.connection.commit()
            return cursor.rowcount > 0
        except Exception as ex:
            db.connection.rollback()
            raise Exception(ex)
