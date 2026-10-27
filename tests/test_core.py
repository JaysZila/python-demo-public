import pytest

from pricecalc.core import add_tax, apply_discount, total


def test_apply_discount():
    assert apply_discount(200.0, 25) == 150.0


def test_discount_out_of_range():
    with pytest.raises(ValueError):
        apply_discount(10.0, 120)


def test_total_with_tax_and_discount():
    assert total([50.0, 50.0], discount=10, tax_rate=0.07) == 96.3
