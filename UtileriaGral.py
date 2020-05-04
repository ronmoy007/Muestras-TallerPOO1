import os
from UtileriaWeb import UtileriaWeb
from UtileriaS3 import UtileriaS3
from UtileriaRDS import UtileriaRDS


# En esta clase pondremos código mega genérico que no esté ligado a algún problema en particular
class UtileriaGral():

    UtileriaWeb = UtileriaWeb()
    UtileriaS3 = UtileriaS3()
    UtileriaRDS = UtileriaRDS()

    def ObtenerTamanioArchivo(self, str_NombreArchivo):
        nbr_file_size = os.stat(str_NombreArchivo).st_size
        return nbr_file_size
