# `y2m`: YouTube Live to m3u

[![M3U generator](https://github.com/eggplants/y2m/actions/workflows/update.yml/badge.svg)](https://github.com/eggplants/y2m/actions/workflows/update.yml)

- Enables to get m3u from YouTube live link(s) easily
  - A Python Library `y2m`
  - Two CLI `y2mconv` and `y2mlink`
- Forked from [benmoose39/YouTube_to_m3u](https://github.com/benmoose39/YouTube_to_m3u)

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
from y2m import y2m

# `<channel name> | <group name> | <logo> | <tvg-id>`
# -> `#EXTINF:-1 group-title="<group name>" tvg-logo="<logo>" tvg-id="<tvg-id>", <channel name>`
y2m.meta_fields_to_extinf(fields: str) -> str: ...

# `https://www.youtube.com/(?:user|channel)/[a-zA-Z0-9_-]+/live`
# -> `https://manifest.googlevideo.com/.../index.m3u`
y2m.convert_ytlive_to_m3u(url: str) -> str: ...

# url -> bool
y2m.is_valid_url(url: str) -> bool: ...

# `ytlive_channel.txt` -> `ytlive.m3u`
y2m.parse_info(info_file_path: str) -> list[str]: ...
```

### CLI

```shellsession
$ y2mconv ytlive_channel.txt -o ytlive.m3u
wrote: ytlive.m3u
$ y2mlink "https://www.youtube.com/c/mangalamtv/live"
https://manifest.googlevideo.com/api/manifest/hls_variant/.../file/index.m3u
```

```shellsession
$ y2mconv -h
usage: y2mconv [-h] [-o OUT] [-f] [-V] info

Convert YouTube Live info file into m3u

positional arguments:
  info               input YouTube Live info file path

optional arguments:
  -h, --help         show this help message and exit
  -o OUT, --out OUT  output m3u path (overwrite: `-f`)
  -f, --force        overwrite if output path is exist
  -V, --version      show program's version number and exit

example input file: https://git.io/JMQ7B
```

```shellsession
$ y2mlink -h
usage: y2mlink [-h] [-V] url

Convert YouTube Live link into m3u one

positional arguments:
  url            input YouTube url

optional arguments:
  -h, --help     show this help message and exit
  -V, --version  show program's version number and exit

valid url pattern:
/^https://www.youtube.com/(?:user|channel)/[a-zA-Z0-9_-]+/live/?$/
/^https://www.youtube.com/watch?v=[a-zA-Z0-9_-]+/
/^https://www.youtube.com/c/[a-zA-Z0-9_-]+/live/?$/
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
