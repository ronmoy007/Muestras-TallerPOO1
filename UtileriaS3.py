import os
import boto3
from dynaconf import settings


# Código genérico respecto a S3
class UtileriaS3():

    # Atributos de conexión referentes a S3
    str_NombreBucket = ''

    # Constructor
    def __init__(self):

        # S3
        self.str_NombreBucket = settings.get('bucket_name')

    # Crea y devuelve una conexión a S3 para usarla como queramos
    def CrearConexionS3(self):

        from boto3 import Session
        session = Session()

        credentials = session.get_credentials()
        current_credentials = credentials.get_frozen_credentials()

        s3 = boto3.client(
                's3',
                aws_access_key_id=current_credentials.access_key,
                aws_secret_access_key=current_credentials.secret_key,
                aws_session_token=current_credentials.token,
                region_name='us-west-2',  # Oregon
                use_ssl=False
            )

        return s3

    def MandarArchivoS3(self, cnx_S3, bucket_name, str_RutaS3, str_Archivo):

        str_NombreArchivoEnS3 = str_RutaS3+os.path.basename(str_Archivo)
        cnx_S3.upload_file(str_Archivo, bucket_name, str_NombreArchivoEnS3)

        return
