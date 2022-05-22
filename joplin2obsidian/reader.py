from pathlib import Path


class Reader:
    def __init__(self, dir: Path):
        self.dir = dir
    
    def iter_md(self):
        for file in self.dir.iterdir():
            if file.is_file() and file.suffix == '.md':
                yield file
            elif file.is_dir():
                _sub_reader = Reader(file)
                yield from _sub_reader.iter_md()
    
    @property
    def resource_dir(self):
        return next((file for file in self.dir.iterdir() if file.is_dir() and file.name == '_resources'), None)