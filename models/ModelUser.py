from .entities.User import User

class ModelUser():

    @classmethod
    def login(self, db,user):
        try:
            cursor = db.connection.cursor()
            print("Sigo vivo")
            sql = """SELECT id_empresa, id_dueno, 
                    e_nombre, e_username, e_password, e_email,
                     e_celular, e_ubicacion, e_imagenperfil 
                     FROM empresa where e_username = '{}' """.format(user.e_username)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                user=User(row[0],row[1],row[2],row[3], User.check_password(row[4], user.e_password), row[5], row[6], row[7], row[8] )
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)