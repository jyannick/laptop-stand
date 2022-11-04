from math import degrees

import svgwrite

from constants import CUT_WIDTH, CUT_COLOR


def rectangle(
    size: (float, float),
    center: (float, float),
    rotation_angle_rad: float,
    dwg: svgwrite.Drawing,
    fill: str,
) -> svgwrite.shapes.Rect:
    top_left_without_rotation = (
        (center[0] - size[0] / 2),
        (center[1] - size[1] / 2),
    )
    rect = dwg.rect(
        insert=top_left_without_rotation,
        size=size,
        fill=fill,
        stroke=CUT_COLOR,
        stroke_width=CUT_WIDTH,
    )
    rect.rotate(
        degrees(rotation_angle_rad),
        center=center,
    )
    return rect
