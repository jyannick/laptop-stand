import math
from pathlib import Path
from typing import Iterable

import svgwrite
import yaml
from svgwrite import cm

import shapes
from constants import PIECE_FILL, CUT_COLOR, CUT_WIDTH, WASTE_FILL


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
    for side, left_coord in zip(("left", "right"), (0, rest_width(conf))):
        top_left = (
            (conf["sheet"]["margin"] + left_coord),
            conf["sheet"]["margin"],
        )
        dwg.add(
            dwg.rect(
                insert=top_left,
                size=(rest_width(conf), rest_length(conf)),
                rx=conf["stand"]["corner_radius"],
                fill=PIECE_FILL,
                stroke=CUT_COLOR,
                stroke_width=CUT_WIDTH,
            )
        )
        add_top_notch(conf, dwg, side, top_left)
        add_bottom_notch(conf, dwg, side, top_left)


def add_top_notch(conf, dwg, side, top_left):
    notch_size = (
        conf["sheet"]["thickness"],
        conf["stand"]["supports_notches_length"],
    )
    notch_center = (
        (top_left[0] + rest_width(conf) / 2),
        (
            top_left[1]
            + conf["stand"]["supports_notches_margin"]
            + conf["stand"]["supports_notches_length"] / 2
        ),  # neglect rotation, increases margin
    )
    notch = shapes.rectangle(
        size=notch_size,
        center=notch_center,
        rotation_angle_rad=supports_small_half_angle(conf)
        if side == "right"
        else math.pi - supports_small_half_angle(conf),
        dwg=dwg,
        fill=WASTE_FILL,
    )
    dwg.add(notch)


def add_bottom_notch(conf, dwg, side, top_left):
    notch_size = (
        conf["sheet"]["thickness"],
        conf["stand"]["supports_notches_length"],
    )
    notch_center = (
        (top_left[0] + rest_width(conf) / 2),
        (
            top_left[1]
            + rest_length(conf)
            - conf["stand"]["supports_notches_margin"]
            - conf["stand"]["supports_notches_length"] / 2
        ),  # neglect rotation, increases margin
    )
    notch = shapes.rectangle(
        size=notch_size,
        center=notch_center,
        rotation_angle_rad=supports_small_half_angle(conf)
        if side == "left"
        else math.pi - supports_small_half_angle(conf),
        dwg=dwg,
        fill=WASTE_FILL,
    )
    dwg.add(notch)


def rest_width(conf):
    return (conf["laptop"]["width"] - conf["laptop"]["between_feet"]) / 2


def rest_length(conf):
    return conf["laptop"]["depth"] + conf["stand"]["front_margin"]


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
