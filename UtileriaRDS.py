from dynaconf import settings


# Código genérico respecto a RDS
class UtileriaRDS():

    # Atributos de conexión referentes a RDS
    str_NombreDB = ''
    str_UsuarioDB = ''
    str_PassDB = ''
    str_EndPointDb = ''
    str_Port = ''

    # Constructor
    def __init__(self):

        # RDS
        self.str_NombreDB = settings.get('dbname')
        self.str_UsuarioDB = settings.get('user')
        self.str_PassDB = settings.get('password')
        self.str_EndPointDB = settings.get('host')
        self.str_Port = settings.get('port')

    # Crea y devuelve una conexión al RDS para poder usarla como queramos
    def CrearConexionRDS(self):

        import psycopg2
        import psycopg2.extras

        conn = psycopg2.connect(database=self.str_NombreDB,
                                user=self.str_UsuarioDB,
                                password=self.str_PassDB,
                                host=self.str_EndPointDB,
                                port=self.str_Port
                                )
        conn.autocommit = True

        return conn

    def InsertarEnRDSDesdeArchivo(self, conn, data_file, nombre_tabla):

        cur = conn.cursor()
        # Load table from the file with header
        cur.copy_expert("copy {} from STDIN CSV HEADER QUOTE '\"'".format(nombre_tabla), data_file)
        cur.execute("commit;")
        cur.close()
