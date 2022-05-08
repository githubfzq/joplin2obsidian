from argparse import ArgumentParser


def main():
    parser = ArgumentParser(prog="joplin2obsidian")
    parser.add_argument(
        '-s', '--source-dir', type=str,
        help='Specify the source directory where Joplin exported the RAW data'
    )
    parser.add_argument(
        '-d', '--destination-dir', type=str,
        help='The destination directory of Obsidian vault'
    )
    parser.parse_args()

if __name__ == '__main__':
    main()