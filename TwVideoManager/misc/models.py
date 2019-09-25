from os import path

from ..models import Video

# For variable static typing
from datetime import datetime
from _io import TextIOWrapper
from dataclasses import dataclass


@dataclass()
class VideoFile(Video):
    """Video files in local data directory

    :arg str name: The name of the video file
    :arg str extension: The extension of the video file
    :arg TextIOWrapper file: File object of the video file
    :arg str author: Streamer ID of the video file
    :arg Optional[datetime] date: Record-Started time of the video file
    """

    name: str
    extension: str
    file: TextIOWrapper

    def __repr__(self):
        return f"""<VideoFile `{self.name}` of `{self.author}`>"""

    @staticmethod
    def from_file(file: TextIOWrapper):  # TODO: Doc this func
        if file.mode != "rb":
            raise TypeError("Video file must be opened with binary mode.")

        full_path = path.abspath(file.name).replace("\\", "/")
        name: str= full_path.split("/")[-1]

        if "." not in name:
            extension = None
        else:
            extension, name = name[::-1].split(".", 1)
            name, extension = name[::-1], extension[::-1]

        author: str = path.dirname(file.name).replace("\\", "/").split("/")[-1]
        date: datetime = VideoFile.parse_time(name)

        return VideoFile(name=name, extension=extension, file=file, author=author, date=date)
