import re
from urllib.request import urlopen


class YtLive2m3u:
    # type: (str) -> str
    @staticmethod
    def meta_fields_to_extinf(line):
        """<channel name> | <group name> | <logo> | <tvg-id>"""
        fields = [i.strip() for i in line.split("|")]
        nf = len(fields)
        if nf != 4:
            raise ValueError("fields got {}, expected 4\nline: {}".format(nf, line))
        else:
            ch_name, grp_title, tvg_logo, tvg_id = fields
            return '#EXTINF:-1 group-title="{}" tvg-logo="{}" tvg-id="{}", {}'.format(
                grp_title.title(), tvg_logo, tvg_id, ch_name
            )

    # type: (str) -> str
    @classmethod
    def convert_ytlive_to_m3u(cls, url):
        """https://www.youtube.com/(?:user|channel)/[a-zA-Z0-9_-]+/live"""
        if not cls.is_valid_url(url):
            raise ValueError(url)
        response = urlopen(url, timeout=15).read().decode('utf-8')
        m = re.findall(r'https://[^"]+.m3u', response)
        if len(m) != 1:
            return "https://raw.githubusercontent.com/eggplants/YouTube_to_m3u/main/assets/moose_na.m3u"
        else:
            return m[0]

    # type: (str) -> bool
    @staticmethod
    def is_valid_url(url):
        test1 = re.match(r'^https://www\.youtube\.com/(?:user|channel)/[a-zA-Z0-9_-]+/live/?$', url)
        test2 = re.match(r'^https://www\.youtube\.com/watch\?v=[a-zA-Z0-9_-]+', url)
        test3 = re.match(r'^https://www\.youtube\.com/c/[a-zA-Z0-9_-]+/live/?$', url)
        return any((test1, test2, test3,))

    # type: (str) -> list[str]
    @classmethod
    def parse_info(cls, path):
        res = []
        is_url = False
        for line in open(path, "r").readlines():
            line = line.strip()
            if line == "" or line.startswith("~~"):
                continue
            elif not is_url:
                res.append(cls.meta_fields_to_extinf(line))
                is_url = True
            elif is_url and cls.is_valid_url(line):
                res.append(cls.convert_ytlive_to_m3u(line))
                is_url = False
            else:
                raise ValueError("info file is maybe invalid syntax\n{}".format(line))
        else:
            return res
