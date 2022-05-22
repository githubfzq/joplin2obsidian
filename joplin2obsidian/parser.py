from pathlib import Path
import re

class MdHandler:
    src_re = re.compile(r"<img.*src=\"(.*)\".*/>")

    def __init__(self, file_path: Path):
        self.file_path = file_path
    
    
    def replace_iter(self):
        with self.file_path.open('r') as f:
            for line in f.readlines():
                yield self.src_re.sub(self._sub_group, line)
    
    def _sub_group(self, matchobj):
        origin_path = Path(matchobj.group(1))
        real_path = origin_path.name
        return f"![[{real_path}]]"
