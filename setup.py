import re

from setuptools import setup

# Reading version
# Reffered https://github.com/Rapptz/discord.py/blob/master/setup.py#L8-L30
with open("TwVideoManager/constants.py") as f:
    data = f.read()
    version = re.search(r'^__VERSION__\s=\s[\'"]([^\'"]*)[\'"]', data, re.MULTILINE).group(1)

    if version.endswith(("a", "b", "rp")):
        version += "-" + re.search(r'^__DATE__\s=\s[\'"](\d+)[\'"]', data, re.MULTILINE).group(1)

# Reading long description
long_description = open("README.md", encoding="UTF-8").read()

# Reading requirements
requirements = ''
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name='TwVideoManager',
    version=version,
    install_requires=requirements,
    packages=['TwVideoManager'],
    requirements=requirements,
    url='https://github.com/R3turn-Dev/TwVideoManager/',
    license='LGPL-3.0',
    author='Eunhak Lee(return0927)',
    author_email='admin@return0927.xyz',
    description='Unified Twitch Video manager via Local and Google Drive',
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
    ],
    )
