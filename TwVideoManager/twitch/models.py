from ..models import Video

from typing import Optional
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass()
class TwitchVideo(Video):
    """Twitch video

    :arg str author: Streamer ID of the video
    :arg int uid: Twitch API ID of the author
    :arg Optional[int] vid: Twitch API Video ID of the stream video
    :arg Optional[str] url: Twitch Video link of the stream video (if public and available)
    :arg Optional[datetime] date: Record-Started time of the video
    :arg Optional[datetime] start_time: Stream-Started time of the video
    :arg Optional[timedelta] uptime: Uptime of the stream video
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
