from pathlib import Path
from html.parser import HTMLParser
import re

class MdHandler:
    img_re = re.compile(r"<img.*/>")

    def __init__(self, file_path: Path):
        self.file_path = file_path
    
    
    def replace_iter(self):
        with self.file_path.open('r') as f:
            for line in f.readlines():
                yield self.img_re.sub(self._sub_group, line)
    
    def _sub_group(self, matchobj: re.Match):
        html = matchobj.group(0)
        parser = ImgParser()
        parser.feed(html)
        src = getattr(parser, 'src', None)
        width = getattr(parser, 'width', None)
        height = getattr(parser, 'height', None)
        if src:
            origin_path = Path(src)
            real_path = origin_path.name
            if width and height:
                return f"![[{real_path}|{width}x{height}]]"
            if width:
                return f"![[{real_path}|{width}]]"
            return f"![[{real_path}]]"
        return html


class ImgParser(HTMLParser):
    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "img":
            for attr in attrs:
                setattr(self, *attr)