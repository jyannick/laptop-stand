from math import degrees
from main import supports_small_half_angle, supports_big_half_angle
import pytest

ATAN_40_35 = 41.185925


@pytest.fixture
def conf():
    return {"laptop": {"width": 40, "depth": 30}, "stand": {"front_margin": 5}}


def test_supports_small_half_angle(conf):
    assert degrees(supports_small_half_angle(conf)) == pytest.approx(ATAN_40_35)


def test_supports_big_half_angle(conf):
    assert degrees(supports_big_half_angle(conf)) == pytest.approx(90 - ATAN_40_35)
