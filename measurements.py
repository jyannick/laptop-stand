import math


def rest_width(conf):
    return (conf["laptop"]["width"] - conf["laptop"]["between_feet"]) / 2


def rest_length(conf):
    return conf["laptop"]["depth"] + conf["stand"]["front_margin"]


def rest_notch_center_from_corner(conf: dict) -> (float, float):
    return (
        rest_width(conf) / 2,
        conf["stand"]["supports_notches_margin"]
        + conf["stand"]["supports_notches_length"] / 2,
    )


def rest_notch_size(conf):
    notch_size = (
        conf["sheet"]["thickness"] - conf["cutter"]["kerf"],
        conf["stand"]["supports_notches_length"] - conf["cutter"]["kerf"],
    )
    return notch_size


def supports_small_half_angle(conf: dict) -> float:
    return math.atan2(rest_length(conf), conf["laptop"]["width"])


def supports_big_half_angle(conf: dict) -> float:
    return math.pi / 2 - supports_small_half_angle(conf)
