#import pymysql # type: ignore
# Removed incorrect import
#pymysql.install_as_MySQLdb()
import mysql.connector


class Conexion:


    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.connection = None



    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Conexion establecida")
        except mysql.connector.Error as err:
            print("Error al conectar a la base de datos:", err)


    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Conexion cerrada.")

    def execute_query(self, query, params=None):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, params or ())
            if query.strip().lower().startswith('select'):
                result = cursor.fetchall()
                return result
            else:
                self.connection.commit()
                print("Consulta ejecutada exitosamente")
                return None
        except mysql.connector.Error as err:
            print("Error al ejecutar la consulta", err)
            return None
        finally:
            cursor.close()
