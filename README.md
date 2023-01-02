![Python version](https://img.shields.io/static/v1?label=python&message=>=3.9&color=green)
[![poetry](https://img.shields.io/static/v1?label=poetry&message=^1&color=green)](https://python-poetry.org/)

# joplin2obsidian
Making the move from Joplin to Obsidian

A python version of another [joplin2obsidian project](https://github.com/luxi78/joplin2obsidian).

## Preparation

1. Install [poetry](https://python-poetry.org/) by pip or other method:
```
// if you use pip

pip install poetry 
```

2. Install packages to poetry virtual environment:
```
poetry install
```

3. Clone this repository
```
git clone https://github.com/githubfzq/joplin2obsidian.git
```

## How to use

### 

1. Firstly, Open Joplin, export *selected notes*, or *specific notebook*, or *all data* (notes and corresponding resources) as **MD - Markdown + 文章前言** to a directory.

2. Run command:
```
cd joplin2obsidian // Change directory to the cloned repository
poetry run python main.py -s <source> -d <destination>
```

where `<source>` is the directory **or subdirectory** with the Joplin-exported directory,
`<destination>` is the destination directory for joplin2obsidian.


> Check the following command to see help:
```
poetry run python main.py --help

usage: joplin2obsidian [-h] [-s SOURCE_DIR] [-d DESTINATION_DIR]

options:
  -h, --help            show this help message and exit
  -s SOURCE_DIR, --source-dir SOURCE_DIR
                        Specify the source directory where Joplin exported the MD data
  -d DESTINATION_DIR, --destination-dir DESTINATION_DIR
                        The destination directory of Obsidian vault
```

3. Open the destination directory as vault in Obsidian

4. In Obsidian settings *settings -> Files & Links*, Fill `_resources` into *Attachment folder path* to enable the newly converted attachment files such as images or audio recordings.


