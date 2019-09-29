import subprocess
from dataclasses import dataclass
from json import loads
from platform import platform
from typing import Union

from .models import File
from ..constants import _FFPROBE_EXTRACT


@dataclass()
class MP4Parser:
    """:class:`MP4Parser` fetches mp4 file meta-data like length, framerate, or screen resolution.

    :var str ffprobe_path: the path to the ffprobe. Default value is set based on assumption
        that the ffprobe file is on the working directory
    """
    ffprobe_path: str = './ffprobe.exe' if 'Windows' in platform() else './ffprobe'

    def parse(self, path: Union[str, File]) -> dict:
        """Parse the given video file and returns as :class:`dict`

        :param Union[str,File] path: The path to the file to parse
        :return dict: Parsed data as a :class:`dict`
        """
        if isinstance(path, File):  # If File object, convert into absolute path
            path = path.path

        b = subprocess.check_output(_FFPROBE_EXTRACT.format(path=self.ffprobe_path, file=path))
        j = loads(b.decode())['format']
        return j
