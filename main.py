import math
from pathlib import Path
from typing import Iterable

import svgwrite
import yaml
from svgwrite import cm


def generate_svg(filename: Path, conf_file: Path) -> None:
    with open(conf_file) as f:
        conf = yaml.safe_load(f)
    dwg = create_drawing(conf, filename)
    build_rest_surfaces(dwg, conf)
    dwg.save(pretty=True)


def to_cm(iterable: Iterable) -> list:
    return [x * cm for x in iterable]


def supports_small_half_angle(conf: dict) -> float:
    return math.atan2(rest_length(conf), conf["laptop"]["width"])


def supports_big_half_angle(conf: dict) -> float:
    return math.pi / 2 - supports_small_half_angle(conf)


def build_rest_surfaces(dwg: svgwrite.Drawing, conf: dict) -> None:
    for left in (0, rest_width(conf)):
        top_left = (
            (conf["sheet"]["margin"] + left),
            conf["sheet"]["margin"],
        )
        dwg.add(
            dwg.rect(
                insert=to_cm(top_left),
                size=(rest_width(conf) * cm, rest_length(conf) * cm),
                rx=conf["stand"]["corner_radius"] * cm,
                fill="blue",
                stroke="red",
                stroke_width=3,
            )
        )
        top_notch = dwg.add(
            dwg.rect(
                insert=to_cm(
                    (
                        (
                            top_left[0]
                            + rest_width(conf) / 2
                            - conf["sheet"]["thickness"] / 2
                        ),
                        (top_left[1] + conf["stand"]["supports_notches_margin"]),
                    )
                ),
                size=to_cm(
                    (
                        conf["sheet"]["thickness"],
                        conf["stand"]["supports_notches_length"],
                    )
                ),
                fill="red",
            )
        )
        dwg.add(top_notch)


def rest_width(conf):
    return (conf["laptop"]["width"] - conf["laptop"]["between_feet"]) / 2


def rest_length(conf):
    return conf["laptop"]["depth"] + conf["stand"]["front_margin"]


def create_drawing(conf, filename):
    size = (conf["sheet"]["width"] * cm, conf["sheet"]["height"] * cm)
    dwg = svgwrite.Drawing(
        filename=filename,
        size=size,
        debug=True,
    )
    dwg.add(
        dwg.rect(
            insert=(0, 0),
            size=size,
            fill="grey",
            stroke="black",
            stroke_width=3,
        )
    )
    dwg.save(pretty=True)
    return dwg


if __name__ == "__main__":
    generate_svg(
        Path("laptop_stand.svg"),
        conf_file=Path("config.yaml"),
    )
