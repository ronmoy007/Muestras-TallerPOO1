from Trabajador import Trabajador
from Auditor import Auditor


class Orquestador():

    Trabajador = Trabajador()
    Auditor = Auditor()

    def CrearInfraestructura(self):
        print('-Ini: Controlador.CrearInfraestructura()')
        self.Trabajador.CrearInfraestructura()

    def HacerWebScraping(self):
        print('-Ini: Controlador.HacerWebScraping()')
        self.Trabajador.HacerWebScraping()

    def EnviarInfoS3(self):
        print('-Ini: Controlador.EnviarInfoS3()')
        self.Trabajador.EnviarInfoS3()

    def ProcesoAuditoria(self):
        print('-Ini: Controlador.ProcesoAuditoria()')
        self.Auditor.AuditarDescargas(self.Trabajador.ObtenerNombresArchivosDescargados())
        self.Auditor.EnviarAuditoriaRDS()

    def MostrarResultados(self):
        print('-Ini: Controlador.MostrarResultados()')
        self.Auditor.MostrarAuditoria()
