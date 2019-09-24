from ..models import Video

from typing import Optional
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass()
class TwitchVideo(Video):
    """Twitch video

    Variables
    ---------
    author: str
        Streamer ID of the video
    uid: int
        Twitch API ID of the author
    vid: Optional[int]
        Twitch API Video ID of the stream video
    url: Optional[str]
        Twitch Video link of the stream video (if public and available)
    date: Optional[datetime]
        Record-Started time of the video
    start_time: Optional[datetime]
        Stream-Started time of the video
    uptime: Optional[timedelta]
        Uptime of the stream video
    """

    uid: int
    vid: Optional[int]
    url: Optional[str]
    start_time: Optional[datetime]
    uptime: Optional[timedelta]

    def __repr__(self):
        return f"""<TwitchVideo `{self.vid}` of `{self.author}({self.uid})` at `{self.date}`>"""

@dataclass()
class User(object):  # TODO: Doc this model class
    uid: int
    id: str
    display_name: str
    avatar_uri: Optional[str]


@dataclass()
class Watcher(User):
    header: User
