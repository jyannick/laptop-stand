import math


def rest_width(conf):
    return (conf["laptop"]["width"] - conf["laptop"]["between_feet"]) / 2


def rest_length(conf):
    return conf["laptop"]["depth"] + conf["stand"]["front_margin"]


def supports_small_half_angle(conf: dict) -> float:
    return math.atan2(rest_length(conf), conf["laptop"]["width"])


def supports_big_half_angle(conf: dict) -> float:
    return math.pi / 2 - supports_small_half_angle(conf)
