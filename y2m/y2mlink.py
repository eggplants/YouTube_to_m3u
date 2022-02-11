import argparse
from typing import List, Optional

from y2m import __version__, y2m


def check_input_url(url: str) -> str:
    if y2m.is_valid_url(url):
        return url
    else:
        raise ValueError("{} is invalid url".format(url))


def parse_args(test: Optional[List[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert YouTube Live link into m3u one",
        epilog=(
            "valid url pattern:\n"
            "/^https://www.youtube.com/(?:user|channel)/[a-zA-Z0-9_-]+/live/?$/\n"
            "/^https://www.youtube.com/watch?v=[a-zA-Z0-9_-]+/\n"
            "/^https://www.youtube.com/c/[a-zA-Z0-9_-]+/live/?$/"
        ),
    )

    parser.add_argument(
        "url",
        type=check_input_url,
        help="input YouTube url",
    )
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version="%(prog)s {}".format(__version__),
    )
    if test is None:
        args = parser.parse_args(test)
    else:
        args = parser.parse_args()
    return args


def main(test: Optional[List[str]] = None) -> None:
    if test is None:
        args = parse_args(test)
    else:
        args = parse_args()
    print(y2m.convert_ytlive_to_m3u(args.url))


if __name__ == "__main__":
    main()
