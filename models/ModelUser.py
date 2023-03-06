from .entities.User import User

class ModelUser():

    @classmethod
    def login(self, db,user):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id_usuario, a_name, a_username, a_password, 
                    a_email, a_descripcion, a_celular, a_ubicacion, a_imagenperfil 
                     FROM usuario where a_username = '{}' """.format(user.a_username)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                return User(row[0],row[1],row[2], User.check_password(row[3], user.a_password), row[4], row[5], row[6], row[7], row[8])

            else:
                return None
        except Exception as ex:
            raise Exception(ex)
    @classmethod
    def get_by_id(self, db,id_usuario):
        try:
            cursor = db.connection.cursor()
            print("Sigo vivo")
            sql = """SELECT id_usuario, a_name, a_username, a_email,
                    a_descripcion, a_celular, a_ubicacion, a_imagenperfil 
                     FROM usuario where id_usuario = '{}' """.format(id_usuario)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                return User(row[0],row[1],row[2],None,row[3],row[4], row[5], row[6], row[7] )

            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def register(cls, db, user):
        try:
            cursor = db.connection.cursor()

            sql = """INSERT INTO usuario(a_name, a_username, a_password, a_email, a_descripcion, a_celular, a_ubicacion, a_imagenperfil) 
                     VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')""".format(
                user.a_name, user.a_username, user.a_password, user.a_email, user.a_descripcion, user.a_celular, user.a_ubicacion, user.a_imagenperfil)
            cursor.execute(sql)
            db.connection.commit()
            return True
        except Exception as ex:
            db.connection.rollback()
            raise Exception(ex)

    @classmethod
    def get_publicaciones_by_user_id(cls, db, id_usuario):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id_publicacion, titulo, contenido, imagen, fecha_publicacion, id_usuario
                     FROM publicaciones
                     WHERE id_usuario = '{}' """.format(id_usuario)
            cursor.execute(sql)
            rows = cursor.fetchall()
            publicaciones = []
            for row in rows:
                publicaciones.append({
                    'id_publicacion': row[0],
                    'titulo': row[1],
                    'contenido': row[2],
                    'imagen': row[3],
                    'fecha_publicacion': row[4],
                    'usuario_id': row[5]
                })
            return publicaciones
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_amigos_by_user_id(cls, db, id_usuario):
        try:
            cursor = db.connection.cursor()
            sql = f"""SELECT usuario.id_usuario, usuario.a_name, usuario.a_username, usuario.a_email, 
                             usuario.a_descripcion, usuario.a_celular, usuario.a_ubicacion, usuario.a_imagenperfil
                      FROM usuario 
                      INNER JOIN amigos ON usuario.id_usuario = amigos.id_amigo 
                      WHERE amigos.id_usuario = '{id_usuario}'"""
            cursor.execute(sql)
            rows = cursor.fetchall()
            amigos = []
            for row in rows:
                amigos.append({
                    'id_usuario': row[0],
                    'a_name': row[1],
                    'a_username': row[2],
                    'a_email': row[3],
                    'a_descripcion': row[4],
                    'a_celular': row[5],
                    'a_ubicacion': row[6],
                    'a_imagenperfil': row[7]
                })
            return amigos
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def enviar_solicitud_amistad(cls, db, id_usuario1, id_usuario2):
        try:
            cursor = db.connection.cursor()
            sql = "INSERT INTO solicitud_amistad (id_usuario1, id_usuario2) VALUES (%s, %s)"
            cursor.execute(sql, (id_usuario1, id_usuario2))
            db.connection.commit()
            return True
        except Exception as ex:
            db.connection.rollback()
            raise Exception(ex)

    @classmethod
    def aceptar_solicitud_amistad(cls, db, id_solicitud):
        try:
            cursor = db.connection.cursor()
            # Obtener IDs de los usuarios en la solicitud
            sql = "SELECT id_usuario1, id_usuario2 FROM solicitud_amistad WHERE id_solicitud = %s"
            cursor.execute(sql, (id_solicitud,))
            row = cursor.fetchone()
            if row:
                id_usuario1, id_usuario2 = row[0], row[1]
                # Agregar a la tabla "amigo"
                sql = "INSERT INTO amigo (id_usuario1, id_usuario2) VALUES (%s, %s)"
                cursor.execute(sql, (id_usuario1, id_usuario2))
                # Eliminar la solicitud de amistad
                sql = "DELETE FROM solicitud_amistad WHERE id_solicitud = %s"
                cursor.execute(sql, (id_solicitud,))
                db.connection.commit()
                return True
            else:
                return False
        except Exception as ex:
            db.connection.rollback()
            raise Exception(ex)

    @classmethod
    def rechazar_solicitud_amistad(cls, db, id_solicitud):
        try:
            cursor = db.connection.cursor()
            sql = "DELETE FROM solicitud_amistad WHERE id_solicitud = %s"
            cursor.execute(sql, (id_solicitud,))
            db.connection.commit()
            return True
        except Exception as ex:
            db.connection.rollback()
            raise Exception(ex)
