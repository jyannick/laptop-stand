from pathlib import Path
from typing import Iterable

import svgwrite
import yaml
from svgwrite import cm

from constants import WASTE_FILL
from rest_surfaces import build_rest_surfaces
from supports import build_supports


def generate_svg(filename: Path, conf_file: Path) -> None:
    with open(conf_file) as f:
        conf = yaml.safe_load(f)
    dwg = create_drawing(conf, filename)
    build_rest_surfaces(dwg, conf)
    build_supports(dwg, conf)
    dwg.save(pretty=True)


def to_cm(iterable: Iterable) -> list:
    return [x * cm for x in iterable]


def create_drawing(conf, filename):
    size = (conf["sheet"]["width"], conf["sheet"]["height"])
    dwg = svgwrite.Drawing(
        filename=filename,
        size=to_cm(size),
        viewBox=(f"0 0 {size[0]} {size[1]}"),
        debug=True,
    )
    dwg.add(
        dwg.rect(
            insert=(0, 0),
            size=size,
            fill=WASTE_FILL,
        )
    )
    dwg.save(pretty=True)
    return dwg


if __name__ == "__main__":
    generate_svg(
        Path("laptop_stand.svg"),
        conf_file=Path("config.yaml"),
    )
