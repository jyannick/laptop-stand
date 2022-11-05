import svgwrite


def build_supports(dwg: svgwrite.Drawing, conf: dict) -> None:
    """
    Builds the two vertical crossed supports (NorthWest-SouthEast and SouthEast-NorthWest)
    :param dwg:
    :param conf:
    :return:
    """
    for which in ("NWSE", "SWNE"):
        pass
