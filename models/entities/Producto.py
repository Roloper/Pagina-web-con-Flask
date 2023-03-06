
class Producto():

    def __init__(self, id_producto, id_usuario,p_producto, p_categoria, p_descripcion, p_precio, p_imagenproducto):
        self.id_usuario = id_producto
        self.id_usuario = id_usuario
        self.p_producto = p_producto
        self.p_categoria = p_categoria
        self.p_descripcion = p_descripcion
        self.p_precio = p_precio
        self.p_imagenproducto =  p_imagenproducto

    def get_id_usuario(self):
        return self.id_usuario

