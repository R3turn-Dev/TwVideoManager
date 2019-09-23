from os import path

# For variable static typing
from datetime import datetime
from typing import Optional, Union
from dataclasses import dataclass


@dataclass()
class Video(object):
    """Basic video structure

    Variables
    ---------
    author: str
        Streamer ID of the video
    date: Optional[datetime]
        Record-Started time of the video
    """

    author: str
    date: Optional[datetime]

    def __repr__(self):
        return f"""<Video `{self.author}`'s at `{self.date}`>"""

    def set_date(self, time: Union[str, datetime]):
        """Parse and set the record-started time of :class:`VideoFile`"""
        if isinstance(time, str):
            time = self.parse_time(time)

        self.date = time

    @staticmethod
    def parse_time(time: str):  # TODO: Doc this parsing func
        try:
            return datetime.strptime(time, "%Y%m%d_%H-%M-%S.mp4")
        except ValueError:
            return datetime.strptime(time, "%Y%m%d_%H-%M-%S")


