import argparse
from os.path import isdir, isfile
from typing import List, Optional, Tuple

from y2m import __version__, y2m


def check_input_path(path: str) -> str:
    if isdir(path):
        raise ValueError("{} is dir".format(path))
    elif isfile(path):
        return path
    else:
        raise FileNotFoundError(path)


def check_output_path(path: str) -> Tuple[str, bool]:
    if isdir(path):
        raise ValueError("{} is dir".format(path))
    elif isfile(path):
        return (path, True)
    else:
        return (path, False)


def parse_args(test: Optional[List[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert YouTube Live info file into m3u",
        epilog=("example input file:\n" "https://git.io/JMQ7B"),
    )

    parser.add_argument(
        "info",
        type=check_input_path,
        help=("input YouTube Live info file path"),
    )
    parser.add_argument(
        "-o", "--out", type=check_output_path, help="output m3u path (overwrite: `-f`)"
    )
    parser.add_argument(
        "-f", "--force", action="store_true", help="overwrite if output path is exist"
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
    if args.out is None:
        res = y2m.parse_info(args.info)
        print("\n".join(res))
    elif args.out[0]:
        if (args.out[1] and args.force) or not args.out[1]:
            res = y2m.parse_info(args.info)
            print("\n".join(res), file=open(args.out[0], "w"))
            print("wrote:", args.out[0])
        else:
            raise ValueError("output path is already exist. use `-f` if overwrite")


if __name__ == "__main__":
    main()
