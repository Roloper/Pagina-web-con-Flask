from .entities.Producto import Producto

class ModelProducto():

    @classmethod
    def create_producto(cls, db, produc):
        try:
            cursor = db.connection.cursor()
            sql = """INSERT INTO producto (id_producto, id_usuario, p_nombreproducto, p_categoria, p_descripcion, p_precio, p_imagenpoducto )
                     VALUES (%s, %s, %s, %s,%s, %s, %s)"""
            cursor.execute(sql,(produc.id_producto, produc.id_usuario,produc.p_nombreproducto, produc.p_categoria, produc.p_descripcion, produc.p_precio, produc.p_imagenpoducto))
            db.connection.commit()
            return True
        except Exception as ex:
            db.connection.rollback()
            raise Exception(ex)

    #mejorar
    @classmethod
    def get(self, db, prod):
        try:
            cursor = db.connection.cursor()
            sql = """select a.*,b.* from usuario a INNER JOIN producto b on a.id_usuario = b.id_usuario; = '{}' """.format(
                prod.a_username)
            cursor.execute(sql)
            row = cursor.fetchone()

        except Exception as ex:
            raise Exception(ex)
