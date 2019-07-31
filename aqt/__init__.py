import argparse
import sys


def run():
    try:
        _run()
    except Exception as e:
        print(e)


def Parse(argv):
    parser = argparse.ArgumentParser(description="Anki ")
    parser.add_argument("-l", "--lang", help="interface language (en, de, etc)")
    print(type(parser.parse_args()))
    return parser.parse_args()


def _run( argv=None, exec=True):  # default parameters with argv = None (without sys.argv) and exec = True
    if argv is None:
        argv = sys.argv
    args = Parse(argv)# parse arguments
    print(args)
