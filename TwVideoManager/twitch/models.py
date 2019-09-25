from twitch import TwitchClient
from twitch.api.users import User

from ..models import Video

from typing import Optional, Union
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
class User(User):
    id: int
    name: str
    display_name: Optional[str]
    type: str
    bio: Optional[str]
    created_at: datetime
    updated_at: datetime
    logo: Optional[str]

    # If my account
    email: Optional[str]
    email_verified: Optional[bool]
    partnered: Optional[bool]
    twitter_connected: Optional[bool]
    notifications: Optional[dict]

    def __repr__(self):
        return ("""User(name='{name}', id={id})""" if self.display_name == self.name else
                """User(name='{name}', display_name='{display_name}' id={id})""")\
            .format(**self)

    @property
    def uid(self):
        """str: User's known name"""
        return self.name

    @classmethod
    def from_user(cls, user: User):
        """Wrap :class:`twitch.users.User` into `User`

        :param twitch.api.users.User user: Target object to wrap
        :return User: Wrapped User object
        """
        if "email" not in user.keys():  # If other's account so don't have meta
            return cls(**user, email=None, email_verified=None, partnered=None,
                       twitter_connected=None, notifications=None)

        # If my account so have meta
        return cls(**user)

    @classmethod
    def from_login(cls, login: str, client: TwitchClient):
        return cls.from_uid(login ,client)

    @classmethod
    def from_uid(cls, uid: str, client: TwitchClient):
        """Get User from usernames

        :param str uid: User's name(known id) to find
        :param twitch.TwitchClient client: TwitchClient to use in translating login name into user
        :return User: Wrapped User object
        """
        user: User = client.users.translate_usernames_to_ids(uid)[0]
        return cls.from_user(user)

    def make_watcher(self, header: Union[str, User], client: TwitchClient=None):
        if isinstance(header, str):
            return Watcher(self, self.from_uid(header, client))

        return Watcher(self, header)


class Watcher(User):
    header: User

    def __repr__(self):
        return """Watcher(`{name}(id={id})` -> {header})""".format(
            name=self.name if self.name == self.display_name else "{}/{}".format(self.name, self.display_name),
            id=self.id,
            header="""`{name}(id={id})`""".format(
                name=self.header.name if self.header.name == self.header.display_name else
                "{}/{}".format(self.header.name, self.header.display_name),
                id=self.header.id,
                ),
            )

    def __init__(self, me: User, header: User):
        super().__init__(**me)
        self.header: User = header

    @classmethod
    def from_login(cls, me: str, header: str, client: TwitchClient):
        me = User.from_uid(me, client)
        header = User.from_uid(header, client)
        return Watcher(me, header)
