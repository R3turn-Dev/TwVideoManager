from TwVideoManager.misc.files import LocalFinder
from TwVideoManager.misc.parser import MP4Parser

lf = LocalFinder()
parser = MP4Parser()

for file in lf.video_files:
    print(parser.parse(file))
