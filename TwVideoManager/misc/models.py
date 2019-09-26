from _io import BufferedReader
from dataclasses import dataclass
# For variable static typing
from datetime import datetime
from os import path
from typing import Any, List, Optional, Union

from ..models import Video


@dataclass()
class File:
    name: str
    path: str
    extension: str

    def __init__(self, name: str, path: str):
        self.name, self.extension = path.splitext(name)
        self.path = path

    def __repr__(self) -> str:
        return """File('{}{}')""".format(self.name, self.extension)

    def __pretty__(self) -> str:
        return self.name


@dataclass()
class Directory:
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

            full_path = path.abspath(file.name).replace("\\", "/")
            name: str= full_path.split("/")[-1]

            if "." not in name:
                extension = None
            else:
                extension, name = name[::-1].split(".", 1)
                name, extension = name[::-1], extension[::-1]

            vid_author: str = path.dirname(file.name).replace("\\", "/").split("/")[-1]
            vid_date: datetime = VideoFile.parse_time(name)

            return VideoFile(name=name, extension=extension, file=file, author=author or vid_author, date=date or vid_date)
        elif isinstance(file, File):
            if author == None or date == None:
                raise TypeError('author and date must be provided if the file is an instance of `File` model.')

            name = file.name
            extension = file.extension
            file: BufferedReader = open(path.join(file.path, file.name), 'rb')

            return VideoFile(author, date, name, extension, file)
        else:
            raise TypeError('File must be subcalss of `File` or `TextIOWrapper.')
