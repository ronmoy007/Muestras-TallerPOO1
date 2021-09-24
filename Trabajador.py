# Tareas específicas de nuestro problema
from UtileriaGral import UtileriaGral

# Clase trabajador
class Trabajador(UtileriaGral):

    # Aquí van los atributos
    str_UrlWebScraping1 = ''
    str_NomArchDesc1 = ''
    str_NomArchDesc2 = ''
    str_NomArchDesc3 = ''

    str_NombreDirectorio = ''
    str_NombreDirectorio = ''
    str_NombreDirectorio = ''

    # Constructor
    def __init__(self):
        super().__init__()

        self.str_UrlWebScraping1 = 'https://www.gutenberg.org/files/35/35-0.txt'
        self.str_NomArchDesc1 = 'archivo1_taller_POO.txt'

        self.str_UrlWebScraping2 = 'http://www.gutenberg.org/cache/epub/5200/pg5200.txt'
        self.str_NomArchDesc2 = 'archivo2_taller_POO.txt'

        self.str_UrlWebScraping3 = 'https://www.gutenberg.org/files/84/84-0.txt'
        self.str_NomArchDesc3 = 'archivo3_taller_POO.txt'

        self.str_NombreDirectorio1 = 'Directorio1/'
        self.str_NombreDirectorio2 = 'Directorio2/'
        self.str_NombreDirectorio3 = 'Directorio3/'

    def CrearInfraestructura(self):

        ############# Crear los directorios en S3 #############

        # Creamos conexión y directorio
        cnx_S3 = self.UtileriaS3.CrearConexionS3()
        cnx_S3.put_object(Bucket=self.UtileriaS3.str_NombreBucket, Key=(self.str_NombreDirectorio1))
        cnx_S3.put_object(Bucket=self.UtileriaS3.str_NombreBucket, Key=(self.str_NombreDirectorio2))
        cnx_S3.put_object(Bucket=self.UtileriaS3.str_NombreBucket, Key=(self.str_NombreDirectorio3))

        ############# Crear los esquemas y tablas en RDS #############

        str_Query1 = "drop schema if exists taller cascade;"
        str_Query2 = "create schema taller;"

        str_Query3 = "drop table if exists taller.tabla_ejemplo;"
        str_Query4 = "create table taller.tabla_ejemplo ( " \
                     + " nombre_archivo VARCHAR(40), " \
                     + " tamanio_archivo VARCHAR(35) " \
                     + " );"

        cnx_RDS = self.UtileriaRDS.CrearConexionRDS()
        with cnx_RDS.cursor() as (cur):
            cur.execute(str_Query1)
            cur.execute(str_Query2)
            cur.execute(str_Query3)
            cur.execute(str_Query4)

        return

    def HacerWebScraping(self):

        self.UtileriaWeb.DescargarRecurso(self.str_UrlWebScraping1, self.str_NomArchDesc1)
        self.UtileriaWeb.DescargarRecurso(self.str_UrlWebScraping2, self.str_NomArchDesc2)
        self.UtileriaWeb.DescargarRecurso(self.str_UrlWebScraping3, self.str_NomArchDesc3)

        return

    def EnviarInfoS3(self):

        cnx_S3 = self.UtileriaS3.CrearConexionS3()
        self.UtileriaS3.MandarArchivoS3(cnx_S3, self.UtileriaS3.str_NombreBucket, self.str_NombreDirectorio1, self.str_NomArchDesc1)
        self.UtileriaS3.MandarArchivoS3(cnx_S3, self.UtileriaS3.str_NombreBucket, self.str_NombreDirectorio2, self.str_NomArchDesc2)
        self.UtileriaS3.MandarArchivoS3(cnx_S3, self.UtileriaS3.str_NombreBucket, self.str_NombreDirectorio3, self.str_NomArchDesc3)

        return

    def ObtenerNombresArchivosDescargados(self):

        arr_Archivos = [self.str_NomArchDesc1,
                        self.str_NomArchDesc2,
                        self.str_NomArchDesc3]

        return arr_Archivos
