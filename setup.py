from re import search
from setuptools import setup


# Reading version
# Reffered https://github.com/Rapptz/discord.py/blob/master/setup.py#L8-L30
with open("TwVideoManager/__init__.py") as f:
    version = search(r'^__VERSION__\s=\s[\'"]([\'"]*)[\'"]', f.read()).group(1)

    if version.endswith(("a", "b", "rp")):
        version += search(r'^__DATE__\s=\s[\'"](\d+)[\'"]', f.read()).group(1)

setup(
    name='TwVideoManager',
    version=version,
    packages=['TwVideoManager'],
    url='https://github.com/R3turn-Dev/TwVideoManager/',
    license='LGPL-3.0',
    author='Eunhak Lee(return0927)',
    author_email='admin@return0927.xyz',
    description='Unified Twitch Video manager via Local and Google Drive',
    )
