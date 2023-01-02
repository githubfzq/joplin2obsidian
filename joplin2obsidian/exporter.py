from pathlib import Path
from joplin2obsidian.reader import Reader
from joplin2obsidian.parser import MdHandler
import shutil
from tqdm import tqdm


class Exporter:
    def __init__(self, root_dir: Path):
        self.root_dir = root_dir
        self.source_dir = None
    
    def copy_resources(self, source_dir: Path):
        dest = self.root_dir / source_dir.name
        if not dest.exists():
            shutil.copytree(source_dir, dest)
        self.source_dir = dest
    
    def export_md(self, reader: Reader):
        to_parse = list(reader.iter_md())
        for md in tqdm(to_parse):
            md_handler = MdHandler(md)
            dest_md = self.root_dir / md.relative_to(reader.dir)
            dest_md.parent.mkdir(parents=True, exist_ok=True)
            with dest_md.open('w') as f:
                for res_line in md_handler.replace_iter(self.source_dir, dest_md):
                    f.write(res_line)
