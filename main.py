from argparse import ArgumentParser
from joplin2obsidian.reader import Reader
from joplin2obsidian.parser import MdHandler
from joplin2obsidian.exporter import Exporter
from pathlib import Path

def main():
    parser = ArgumentParser(prog="joplin2obsidian")
    parser.add_argument(
        '-s', '--source-dir', type=Path,
        help='Specify the source directory where Joplin exported the MD data'
    )
    parser.add_argument(
        '-d', '--destination-dir', type=Path,
        help='The destination directory of Obsidian vault'
    )
    args = parser.parse_args()
    reader = Reader(args.source_dir)
    exporter = Exporter(args.destination_dir)
    exporter.copy_resources(reader.resource_dir)
    exporter.export_md(reader)


if __name__ == '__main__':
    main()