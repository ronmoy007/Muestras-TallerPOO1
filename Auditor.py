from UtileriaGral import UtileriaGral


class Auditor(UtileriaGral):

    str_ArchivoAuditoria = ''

    def __init__(self):
        super().__init__()
        self.str_ArchivoAuditoria = 'auditoria.csv'

    def AuditarDescargas(self, par_arrArchivos):

        import pandas as pd
        import numpy as np

        np_Campos = np.empty([0, 2])

        for elemento in par_arrArchivos:
            nbr_Tamanio=self.ObtenerTamanioArchivo(elemento)
            np_Campos = np.append(np_Campos, [[elemento,nbr_Tamanio]], axis=0)

        # Se pasa a un csv
        columns = ['id_archivo', 'tamanio']
        df = pd.DataFrame(data=np_Campos, columns=columns)
        df.to_csv(self.str_ArchivoAuditoria, index=False, header=True)

        return

    def EnviarAuditoriaRDS(self):

        archivo = open(self.str_ArchivoAuditoria)
        cnx_RDS = self.UtileriaRDS.CrearConexionRDS()
        self.UtileriaRDS.InsertarEnRDSDesdeArchivo(cnx_RDS, archivo, 'taller.tabla_ejemplo')

        return

    def MostrarAuditoria(self):
        # Obtenemos la conexión
        cnx_RDS = self.UtileriaRDS.CrearConexionRDS()

        # Se abre el cursor
        with cnx_RDS.cursor() as (cur):
            # Ejecutamos el query
            cur.execute('select * from taller.tabla_ejemplo')

            # Obtenemos las filas y las barremos
            filas = cur.fetchall()
            for fila in filas:
                print("Nombre archivo = ", fila[0])
                print("Tamaño archivo = ", fila[1])

        return
