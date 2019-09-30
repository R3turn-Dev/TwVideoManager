import os

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


class GoogleDriveAdapter:
    def __init__(self,
                 access_token: str='',
                 credentials_file: str='credentials.json'):
        self.gauth = GoogleAuth()

        if access_token:
            self.gauth.Auth(access_token)

        else:
            if os.path.exists(credentials_file):
                self.gauth.LoadCredentialsFile(credentials_file)
            else:
                self.gauth.CommandLineAuth()

        self.gdrive = GoogleDrive(self.gauth)

    @property
    def token(self) -> str:
        return self.gauth.credentials.access_token

