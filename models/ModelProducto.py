from .entities.Producto import Producto

class ModelProducto():

    @classmethod
    def get(self, db,prod):
        try:
            cursor = db.connection.cursor()
            sql = """select a.*,b.* from usuario a INNER JOIN producto b on a.id_usuario = b.id_usuario; = '{}' """.format(prod.a_username)
            cursor.execute(sql)
            row = cursor.fetchone()

        except Exception as ex:
            raise Exception(ex)