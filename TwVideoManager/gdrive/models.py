from ..misc.models import Video

from typing import Optional
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass()
class RemoteVideoFile(Video):
    """Video files in remote Google Drive

    :arg str author: Streamer ID of the video
    :arg Optional[datetime] date: Record-Started time of the video
    :arg str id: Google Drive File id of the video file
    :arg Optional[str] url: Google Drive Resource url directing the video file
    :arg Optional[str] parent: Parent directory of the Google Drive file
    """

    id: str
    url: Optional[str]
    parent: Optional[str]  # TODO: Change this to custom model

    def __repr__(self):
        return f"""<RemoteVideoFile `{self.id}` of `{self.author}` at `{self.date}`>"""
