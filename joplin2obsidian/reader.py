from pathlib import Path
from functools import cached_property


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
    
    @cached_property
    def resource_dir(self):
        return self._get_resource_dir()
    

    def _get_resource_dir(self, search_dir=None):
        search_dir = search_dir or self.dir
        cur_resource_dir = next((file for file in search_dir.iterdir() if file.is_dir() and file.name == '_resources'), None)

        return cur_resource_dir or self._get_resource_dir(search_dir.parent)