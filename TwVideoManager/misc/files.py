import os
from dataclasses import dataclass
from typing import List, Any, Optional, Union

from ..constants import _DEFAULT_SCRIPT_NAME, _EXTENSION_VIDEO


@dataclass()
class File:
    name: str
    path: str
    extension: str

    def __init__(self, name: str, path: str):
        self.name, self.extension = os.path.splitext(name)
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


class LocalFinder:
    """Finds and manages the video-downloading directory to upload the video files to
    the google drive and remove from disc for better disc-usage.

    :var str script_name: the video-downloading script name (Default: 'bot.sh').
        This is used for determining whether the sub-directory is video-downloading
        directory to manage or not.
    :var str video_dir: the path to manage as a video-downloading directory.
    """

    def __init__(self,
                 script_name: str=None,
                 video_dir: str=None):
        self.script_name = script_name or _DEFAULT_SCRIPT_NAME
        self.video_dir = video_dir or './Streams'


    @property
    def dir(self) -> Directory:  # TODO: Doc
        """

        :return Directory:
        """
        return Directory(os.path.basename(self.video_dir), os.path.dirname(self.video_dir), None, self.wrapper(self.video_dir))

    @property
    def stream_dir(self) -> List[Directory]:  # TODO: Doc
        """

        :return List[Directory]: returns the stream-saving folders including script file.
        """
        return [*filter(lambda x: isinstance(x, Directory) and self.has_script(x), self.dir.subdirectories)]

    @property
    def video_files(self) -> List[File]:
        """returns all video files in the stream directories.

        The video files' extension must be included in pre-filled extension set (see `TwVideoManager.constants.
        _EXTENSION_VIDEO`.

        :return List[File]: the video files in stream directories.
        """
        l = []
        for directory in self.stream_dir:
            for file in directory.subfiles:
                if file.extension in _EXTENSION_VIDEO:
                    l.append(file)

        return l

    @classmethod
    def wrapper(cls, path: str) -> List[Union[File, Directory]]:
        """Wraps sub-directories and sub-files with each :class:`Directory` and :class:`File`.

        :param str path: the path to wrap with class.
        :return List[Union[File, Directory]]: Wrapped sub-directories and sub-files.
        """
        l = []
        for name in os.listdir(path):
            try:
                _path = os.path.join(path, name)

                if os.path.isfile(_path):
                    l.append(File(name, _path))
                else:
                    l.append(Directory(name, _path, None, cls.wrapper(_path)))
            except PermissionError:
                pass

        return l

    def has_script(self, target: Directory) -> bool:
        """Returns if the directory has script file

        The name of script file is determined based on class' :attr:`.script_name` and
        returns whether the directory has a file named 'bot.sh" (as default) or not.

        :param Directory target: the target directory to find script file
        :return bool: whether the directory has a file named 'bot.sh" (as default) or not
        """
        find = False
        for file in target.subfiles:
            if file.name == self.script_name:
                find = True
                break
        return find
