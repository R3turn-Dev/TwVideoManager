from ..misc.models import Video

from typing import Optional
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass()
class RemoteVideoFile(Video):
    """Video files in remote Google Drive

    Variables
    ---------
    author: str
        Streamer ID of the video
    date: Optional[datetime]
        Record-Started time of the video
    id: str
        Google Drive File id of the video file
    url: Optional[str]
        Google Drive Resource url directing the video file
    parent: Optional[str]
        Parent directory of the Google Drive file
    """

    id: str
    url: Optional[str]
    parent: Optional[str]  # TODO: Change this to custom model

    def __repr__(self):
        return f"""<RemoteVideoFile `{self.id}` of `{self.author}` at `{self.date}`>"""
