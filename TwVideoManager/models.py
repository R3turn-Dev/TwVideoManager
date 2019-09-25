from os import path

# For variable static typing
import datetime
from typing import Optional, Union
from dataclasses import dataclass


@dataclass()
class Video():
    """Basic video structure

    :var str author: Streamer ID of the video
    :var Optional[datetime.datetime] date: Record-Started time of the video
    """

    author: str
    date: Optional[datetime.datetime]

    def __repr__(self):
        return f"""<Video `{self.author}`'s at `{self.date}`>"""

    def set_date(self, time: Union[str, datetime.datetime]):
        """Parse and set the record-started time of :class:`Video`"""
        if isinstance(time, str):
            time = self.parse_time(time)

        self.date = time

    @staticmethod
    def parse_time(time: str):
        """Parse a date-time string into :class:`datetime.datetime` object

        `time` must be matched the pattern `%Y%m%d_%H-%M-%S.mp4` or `%Y%m%d_%H-%M-%S`.

        :param str time: Time string to parse as a date
        :return datetime.datetime: Parsed data as a :class:`datetime.datetime` object
        """

        try:
            return datetime.datetime.strptime(time, "%Y%m%d_%H-%M-%S.mp4")
        except ValueError:
            try:
                return datetime.datetime.strptime(time, "%Y%m%d_%H-%M-%S")
            except ValueError as ex:
                raise ex


