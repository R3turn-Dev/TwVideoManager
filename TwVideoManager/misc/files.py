import os
from dataclasses import dataclass
from typing import List, Any, Optional, Union

from ..constants import _DEFAULT_SCRIPT_NAME


@dataclass()
class File:
    name: str
    path: str

    def __repr__(self) -> str:
        return """File('{}')""".format(self.name)

    def __pretty__(self) -> str:
        return self.name


@dataclass()
class Directory:
    name: str
    path: str
    parent: Any
    siblings: Optional[List[File]]

    def __pretty__(self, depth=0) -> str:
        out = ''

        if depth == 0:
            out += self.name + '\n'

            for dir in filter(lambda x: isinstance(x, Directory), self.siblings):
                out += dir.__pretty__(depth=depth+1) + '\n'

        else:
            return '│  ' * (depth - 1) + '├─' + self.name


        return out


class LocalFinder:
    def __init__(self,
                 script_name: str=_DEFAULT_SCRIPT_NAME,
                 video_dir: str=None):
        self.script_name = script_name
        self.video_dir = video_dir or os.path.abspath("Streams/")

    @classmethod
    def wrapper(cls, path: str) -> List[Union[File, Directory]]:
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

    @property
    def dir(self) -> Directory:
        return Directory(os.path.basename(self.video_dir), os.path.dirname(self.video_dir), None, self.wrapper(self.video_dir))
