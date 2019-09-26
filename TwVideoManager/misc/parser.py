import subprocess
from dataclasses import dataclass
from json import loads
from platform import platform

from ..constants import _FFPROBE_EXTRACT


@dataclass()
class MP4Parser:
    ffprobe_path: str = './ffprobe.exe' if platform() == 'Windows' else './ffprobe'

    def parse(self, path: str) -> dict:
        b = subprocess.check_output(_FFPROBE_EXTRACT.format(path=self.ffprobe_path, file=path))
        j = loads(b.decode())['format']
        return j
