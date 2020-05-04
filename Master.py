from Orquestador import Orquestador

if __name__ == "__main__":

    # Se crea el objeto controlador
    obj_Orquestador = Orquestador()

    # Se ejecuta el pipeline principal
    obj_Orquestador.CrearInfraestructura()
    obj_Orquestador.HacerWebScraping()
    obj_Orquestador.EnviarInfoS3()
    obj_Orquestador.ProcesoAuditoria()
    obj_Orquestador.MostrarResultados()
