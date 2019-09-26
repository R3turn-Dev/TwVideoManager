import subprocess
from dataclasses import dataclass
from json import loads
from platform import platform
from typing import Union

from .models import File
from ..constants import _FFPROBE_EXTRACT


@dataclass()
class MP4Parser:
    ffprobe_path: str = './ffprobe.exe' if 'Windows' in platform() else './ffprobe'

    def parse(self, path: Union[str, File]) -> dict:
        if isinstance(path, File):  # If File object, convert into absolute path
            path = path.path

        b = subprocess.check_output(_FFPROBE_EXTRACT.format(path=self.ffprobe_path, file=path))
        j = loads(b.decode())['format']
        return j
