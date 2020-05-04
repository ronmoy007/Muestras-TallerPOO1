import requests


class UtileriaWeb():

    def DescargarRecurso(self, par_Url, par_NombreArchivoLocal):
        file = requests.get(par_Url)
        open(par_NombreArchivoLocal, 'wb').write(file.content)
