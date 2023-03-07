from .entities.User import User


class ModelUser():

    @classmethod
    def login(self, db, user):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id_usuario, a_name, a_username, a_password, 
                    a_email, a_descripcion, a_celular, a_ubicacion, a_imagenperfil 
                     FROM usuario where a_username = '{}' """.format(user.a_username)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                return User(row[0], row[1], row[2], User.check_password(row[3], user.a_password), row[4], row[5],
                            row[6], row[7], row[8])

            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_by_id(self, db, id_usuario):
        try:
            cursor = db.connection.cursor()
            print("Sigo vivo")
            sql = """SELECT id_usuario, a_name, a_username, a_email,
                    a_descripcion, a_celular, a_ubicacion, a_imagenperfil 
                     FROM usuario where id_usuario = '{}' """.format(id_usuario)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                return User(row[0], row[1], row[2], None, row[3], row[4], row[5], row[6], row[7])

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
                user.a_name, user.a_username, user.a_password, user.a_email, user.a_descripcion, user.a_celular,
                user.a_ubicacion, user.a_imagenperfil)
            cursor.execute(sql)
            db.connection.commit()
            return True
        except Exception as ex:
            db.connection.rollback()
            raise Exception(ex)

    @classmethod
    def enviar_solicitud(cls, db, user_id, connection_id):
        try:
            cursor = db.connection.cursor()
            print("bienn 1")
            # Verificar si ya existe una solicitud de conexión pendiente o aceptada entre los usuarios
            sql = """SELECT COUNT(*) FROM user_connections
                     WHERE (user_id = %s AND connection_id = %s)
                     OR (user_id = %s AND connection_id = %s)
                     AND status != 'rechazada'"""
            print("bienn 2")
            cursor.execute(sql, (user_id, connection_id, connection_id, user_id))
            print("bienn 3")
            count = cursor.fetchone()[0]  # lo asigna a la primera columna

            if count == 0:
                # Agregar una nueva solicitud de conexión pendiente
                sql = "INSERT INTO user_connections (user_id, connection_id, status) VALUES (%s, %s, 'pendiente')"
                cursor.execute(sql, (user_id, connection_id))
                db.connection.commit()
                return True
            else:
                # Ya existe una solicitud pendiente o aceptada
                return False
        except Exception as ex:
            db.connection.rollback()
            raise Exception(ex)

    @classmethod
    def get_solicitudes(cls, db, user_id):
        try:
            cursor = db.connection.cursor()

            # Obtener todas las solicitudes de conexión pendientes del usuario
            sql = """SELECT user_connections.id, usuario.a_name, usuario.a_username, usuario.a_ubicacion, usuario.a_imagenperfil
                         FROM user_connections
                         JOIN usuario ON user_connections.user_id = usuario.id_usuario
                         WHERE connection_id = %s AND status = 'pendiente'"""
            cursor.execute(sql, (user_id,))
            rows = cursor.fetchall()
            requests = []
            for row in rows:
                requests.append({
                    'id': row[0],
                    'name': row[1],
                    'username': row[2],
                    'location': row[3],
                    'profile_image': row[4]
                })
            return requests
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def aceptar_solicitud(cls, db, request_id):
        try:
            cursor = db.connection.cursor()

            # Cambiar el estado de la solicitud de conexión a aceptada
            sql = "UPDATE user_connections SET status = 'aceptada' WHERE id = %s"
            cursor.execute(sql, (request_id,))
            db.connection.commit()
            return True
        except Exception as ex:
            db.connection.rollback()
            raise Exception(ex)

    @classmethod
    def rechazar_solicitud(cls, db, request_id):
        try:
            cursor = db.connection.cursor()
            # Eliminar la solicitud de conexión
            sql = "DELETE FROM user_connections WHERE id = %s"
            cursor.execute(sql, (request_id,))
            db.connection.commit()
            return True
        except Exception as ex:
            db.connection.rollback()
            print("rechazar_soli")
            raise Exception(ex)

    @classmethod
    def get_amigos(cls, db, id_usuario):
        """
        Obtiene los amigos de un usuario dado su id_usuario
        """
        try:
            cursor = db.connection.cursor()
            # Seleccionamos los usuarios amigos de la tabla de amistades
            sql = """SELECT usuario.* FROM usuario 
                    JOIN user_connections 
                    ON (usuario.id_usuario = user_connections.user_id OR usuario.id_usuario = user_connections.connection_id) 
                    WHERE (user_connections.user_id = %s OR user_connections.connection_id = %s) 
                    AND usuario.id_usuario != %s 
                    AND user_connections.status = 'aceptada'"""

            cursor.execute(sql, (id_usuario, id_usuario, id_usuario))
            amigos = cursor.fetchall()

            # Convertimos los resultados en una lista de objetos Usuario
            amigos_list = []
            for amigo in amigos:
                amigo_obj = User(
                    amigo[0],
                    amigo[1],
                    amigo[2],
                    amigo[3],
                    amigo[4],
                    amigo[5]
                )
                amigos_list.append(amigo_obj)

            return amigos_list

        except Exception as ex:
            print("gets_amigos")
            print(str(ex))
            return None

    @classmethod
    def get_no_amigos(cls, db, id_usuario):
        """
        Obtiene los usuarios que no son amigos de un usuario dado su id_usuario
        """
        try:
            cursor = db.connection.cursor()
            # Seleccionamos los usuarios que no están en la tabla de amistades
            sql = """SELECT * FROM usuario 
                    WHERE id_usuario 
                    NOT IN 
                    (SELECT user_id FROM user_connections 
                        WHERE connection_id = %s AND status = 'aceptada' 
                        UNION SELECT connection_id FROM user_connections 
                            WHERE user_id = %s AND status = 'aceptada') 
                        AND id_usuario != %s"""
            print("bien 1")
            cursor.execute(sql, (id_usuario, id_usuario, id_usuario))
            print("bien 2")
            no_amigos = cursor.fetchall()
            print("bien 3")

            # Convertimos los resultados en una lista de objetos Usuario
            no_amigos_list = []
            print("bien 4")
            for no_amigo in no_amigos:
                no_amigo_obj = User(
                    no_amigo[0],
                    no_amigo[1],
                    no_amigo[2],
                    no_amigo[3],
                    no_amigo[4],
                    no_amigo[5],
                    no_amigo[6],
                    no_amigo[7],
                    no_amigo[8]
                )
                no_amigos_list.append(no_amigo_obj)
                print("bien 5")
            return no_amigos_list

        except Exception as ex:
            print("get_no_amigo")
            print(str(ex))
            return []
