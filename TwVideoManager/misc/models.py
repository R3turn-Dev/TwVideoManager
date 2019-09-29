import os
from _io import BufferedReader
from dataclasses import dataclass
# For variable static typing
from datetime import datetime
from typing import Any, List, Optional, Union

from ..models import Video


@dataclass()
class File:
    """Wrap class for sub-files on :class:`Directory`.

    :arg str name: the name of the file (without extension).
    :arg str path: the path of the file (with full filename with the extension).
    :arg int size: the size of the file (in Bytes)
    :arg Any meta: metadata of the file.
    :arg str extension: the extension of the file, starting with a dot.
        Can be `None` if the file extension is unexplicit.
    """
    name: str
    path: str
    _size: Optional[int]
    meta: Any
    extension: str

    def __init__(self, name: str, path: str, size=None, meta: Any=''):
        self.name, self.extension = os.path.splitext(name)
        self.path = path
        self._size = size
        self.meta = meta

    def __repr__(self) -> str:
        return """File('{}{}')""".format(self.name, self.extension)

    def __pretty__(self) -> str:
        return self.name

    @property
    def size(self) -> int:
        if not isinstance(self._size, int):
            self._size = os.path.getsize(self.path)

        return self._size


@dataclass()
class Directory:
    """Wrap class for sub-files and sub-directories.

    :arg str name: the name of the directory.
    :arg str path: the path of the directory.
    :arg Directory parent: the parent :class:`Directory` containing this directory.
    :arg List[File,Directory] siblings: the sub-directories and sub-files,
        and each is wrapped with the wrapping class.
    """
    name: str
    path: str
    parent: Any
    siblings: Optional[List[File]]

    @property
    def subdirectories(self) -> list:
        return [*filter(lambda x: isinstance(x, Directory), self.siblings)]

    @property
    def subfiles(self) -> List[File]:
        return [*filter(lambda x: isinstance(x, File), self.siblings)]

    @property
    def names(self) -> List[str]:
        return [x.name for x in self.siblings]

    @property
    def size(self) -> int:
        return sum(x.size for x in self.siblings)

    def __pretty__(self, depth=0) -> str:  # TODO: prettify printing
        out = ''

        if depth == 0:
            out += self.name + '\n'

            for dir in self.subdirectories:
                out += dir.__pretty__(depth=depth+1) + '\n'

        else:
            return '│  ' * (depth - 1) + '├─' + self.name


        return out

@dataclass()
class VideoFile(Video, File):
    """Video files in local data directory

    :arg str name: The name of the video file
    :arg str extension: The extension of the video file
    :arg TextIOWrapper file: File object of the video file
    :arg str author: Streamer ID of the video file
    :arg Optional[datetime] date: Record-Started time of the video file
    """

    name: str
    extension: str
    file: BufferedReader


    def __repr__(self):
        return f"""<VideoFile `{self.name}` of `{self.author}`>"""

    @staticmethod
    def from_file(file: Union[BufferedReader, File], author=None, date=None):  # TODO: Doc this func
        if isinstance(file, BufferedReader):
            if file.mode != "rb":
                raise TypeError("Video file must be opened with binary mode.")

            full_path = os.path.abspath(file.name).replace("\\", "/")
            name: str= full_path.split("/")[-1]

            if "." not in name:
                extension = None
            else:
                extension, name = name[::-1].split(".", 1)
                name, extension = name[::-1], extension[::-1]

            vid_author: str = os.path.dirname(file.name).replace("\\", "/").split("/")[-1]
            vid_date: datetime = VideoFile.parse_time(name)

            return VideoFile(name=name, extension=extension, file=file, author=author or vid_author, date=date or vid_date)
        elif isinstance(file, File):
            if author == None or date == None:
                raise TypeError('author and date must be provided if the file is an instance of `File` model.')

            name = file.name
            extension = file.extension
            file: BufferedReader = open(os.path.join(file.path, file.name), 'rb')

            return VideoFile(author, date, name, extension, file)
        else:
            raise TypeError('File must be subcalss of `File` or `TextIOWrapper.')
