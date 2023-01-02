from pathlib import Path
from html.parser import HTMLParser
import re
from joplin2obsidian.utils import relative_path


class MdHandler:
    img_re = re.compile(r"<img.*/>")
    number_re = re.compile(r"\#(?![\#\s])")
    link_re = re.compile(r"\!\[(.*)\]\((.*)\)")

    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.export_path = None

    def replace_iter(self, source_dir: Path, export_path: Path):
        def fix_sub_func(matchobj: re.Match):
            return self._sub_path(matchobj, source_dir, export_path)
        with self.file_path.open('r') as f:
            for line in f.readlines():
                attached = self.img_re.sub(self._sub_img, line)
                escaped = self.number_re.sub('\#', attached)
                if attached != line:
                    fixed = self.link_re.sub(fix_sub_func, escaped)
                    yield fixed
                else:
                    yield escaped

    def _sub_img(self, matchobj: re.Match):
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

    def _sub_path(self, matchobj: re.Match, source_dir: Path, export_path: Path):
        source: str = matchobj.group(2)
        source_path = Path(source).name
        absolute_source_path = source_dir / source_path
        if len(source_path) < 50 and absolute_source_path.exists():
            relative_source_path = relative_path(
                absolute_source_path, export_path)
            return f"![{matchobj.group(1)}]({relative_source_path})"
        return matchobj.group(0)


class ImgParser(HTMLParser):
    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "img":
            for attr in attrs:
                setattr(self, *attr)
