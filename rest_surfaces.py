import math

import svgwrite

import shapes
from constants import WASTE_FILL, PIECE_FILL, CUT_COLOR, CUT_WIDTH
from measurements import rest_width, rest_length, supports_small_half_angle


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
        conf["sheet"]["thickness"] - conf["cutter"]["kerf"],
        conf["stand"]["supports_notches_length"] - conf["cutter"]["kerf"],
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
        conf["sheet"]["thickness"] - conf["cutter"]["kerf"],
        conf["stand"]["supports_notches_length"] - conf["cutter"]["kerf"],
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
