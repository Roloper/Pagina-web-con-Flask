from .entities.Amigo import Amigo


class ModelAmigo:

    @classmethod
    def enviar_solicitud(cls, db, id_usuario, id_amigo):
        try:
            cursor = db.connection.cursor()
            sql = """INSERT INTO amigo (usuario_id, amigo_id, fecha_amistad, estado)
                     VALUES ('{}', '{}', CURRENT_TIMESTAMP(), 'Pendiente')""".format(id_usuario, id_amigo)
            cursor.execute(sql)
            db.connection.commit()
            return True
        except Exception as ex:
            db.connection.rollback()
            raise Exception(ex)

    @classmethod
    def aceptar_solicitud(cls, db, id_amigo):
        try:
            cursor = db.connection.cursor()
            sql = """UPDATE amigo SET estado = 'Aceptada', fecha_amistad = CURRENT_TIMESTAMP() WHERE id_amigo = '{}'""".format(
                id_amigo)
            cursor.execute(sql)
            db.connection.commit()
            return True
        except Exception as ex:
            db.connection.rollback()
            raise Exception(ex)

    @classmethod
    def rechazar_solicitud(cls, db, id_amigo):
        try:
            cursor = db.connection.cursor()
            sql = """DELETE FROM amigo WHERE id_amigo = '{}'""".format(id_amigo)
            cursor.execute(sql)
            db.connection.commit()
            return True
        except Exception as ex:
            db.connection.rollback()
            raise Exception(ex)

    @classmethod
    def get_amigos_by_user_id(cls, db, id_usuario):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT amigo_id, fecha_amistad, estado
                     FROM amigo
                     WHERE usuario_id = '{}' AND estado = 'Aceptada'""".format(id_usuario)
            cursor.execute(sql)
            rows = cursor.fetchall()
            amigos = []
            for row in rows:
                amigos.append({
                    'id_amigo': row[0],
                    'fecha_amistad': row[1],
                    'estado': row[2]
                })
            return amigos
        except Exception as ex:
            raise Exception(ex)