# `y2m`: YouTube Live to m3u

[![M3U generator](https://github.com/eggplants/y2m/actions/workflows/update.yml/badge.svg)](https://github.com/eggplants/y2m/actions/workflows/update.yml)

Forked from [benmoose39/YouTube_to_m3u](https://github.com/benmoose39/YouTube_to_m3u)

## Install

### From source

```bash
git clone --depth 1 https://githu.com/eggplants/y2m y2m
cd y2m
pip install .
```

<!--
## From PyPI

```shellsession
$ pip install y2m
```
-->

## Usage

### Library

```python
from y2m import *

# `<channel name> | <group name> | <logo> | <tvg-id>`
# -> `#EXTINF:-1 group-title="<group name>" tvg-logo="<logo>" tvg-id="<tvg-id>", <channel name>`
y2m.meta_fields_to_extinf(fields: str) -> str: ...

# `https://www.youtube.com/(?:user|channel)/[a-zA-Z0-9_-]+/live`
# -> `https://manifest.googlevideo.com/.../index.m3u`
y2m.convert_ytlive_to_m3u(url: str) -> str: ...

# `ytlive_channel.txt` -> `ytlive.m3u`
y2m.parse_info(info_file_path: str) -> list[str]: ...
```

### CLI

```shellsession
$ y2m ytlive_channel.txt -o ytlive.m3u
wrote: ytlive.m3u
```

```shellsession
$ y2m -h
usage: y2m [-h] [-o OUT] [-f] [-V] info

Grab m3u from YouTube live

positional arguments:
  info               input YouTubeLive info file path (ex:
                     https://git.io/JMQZz)

optional arguments:
  -h, --help         show this help message and exit
  -o OUT, --out OUT  output m3u path (overwrite: `-f`)
  -f, --force        overwrite if output path is exist
  -V, --version      show program's version number and exit
```

## Input file format

```txt
...
~~ comment
...
<channel name> | <group name> | <logo> | <tvg-id>
https://www.youtube.com/(?:user|channel)/[a-zA-Z0-9_-]+/live
...
```
