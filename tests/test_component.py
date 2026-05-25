import pytest
from src.component import calculate_cancellation_fee



# Normal behaviour tests


def test_full_refund_early_cancellation():
    result = calculate_cancellation_fee(500, 40, "bronze", False, False)

    assert result["fee"] == 0.0
    assert result["refund"] == 500.0


def test_mid_cancellation_silver_discount():
    result = calculate_cancellation_fee(500, 10, "silver", False, False)

    # 20% fee = 100
    # Silver discount = 10%
    # Final fee = 90
    assert result["fee"] == 90.0
    assert result["refund"] == 410.0


def test_late_cancellation_gold_discount():
    result = calculate_cancellation_fee(500, 2, "gold", False, False)

    # 50% fee = 250
    # Gold discount = 20%
    # Final fee = 200
    assert result["fee"] == 200.0
    assert result["refund"] == 300.0


def test_same_day_cancellation():
    result = calculate_cancellation_fee(500, 0, "bronze", False, False)

    # 100% fee
    assert result["fee"] == 500.0
    assert result["refund"] == 0.0



# Peak season tests


def test_peak_season_mid_cancellation():
    result = calculate_cancellation_fee(500, 10, "bronze", True, False)

    # 20% + 10% = 30%
    # Fee = 150
    assert result["fee"] == 150.0
    assert result["refund"] == 350.0


def test_peak_season_late_gold_discount():
    result = calculate_cancellation_fee(500, 2, "gold", True, False)

    # 50% + 10% = 60% => 300
    # Gold discount 20% => 240
    assert result["fee"] == 240.0
    assert result["refund"] == 260.0



# Non-refundable override


def test_non_refundable_booking():
    result = calculate_cancellation_fee(500, 40, "gold", False, True)

    # Override everything
    assert result["fee"] == 500.0
    assert result["refund"] == 0.0



# Boundary tests


def test_boundary_30_days():
    result = calculate_cancellation_fee(500, 30, "bronze", False, False)

    # 0% fee
    assert result["fee"] == 0.0
    assert result["refund"] == 500.0


def test_boundary_29_days():
    result = calculate_cancellation_fee(500, 29, "bronze", False, False)

    # 20% fee
    assert result["fee"] == 100.0
    assert result["refund"] == 400.0


def test_boundary_7_days():
    result = calculate_cancellation_fee(500, 7, "bronze", False, False)

    # 20% fee
    assert result["fee"] == 100.0
    assert result["refund"] == 400.0


def test_boundary_6_days():
    result = calculate_cancellation_fee(500, 6, "bronze", False, False)

    # 50% fee
    assert result["fee"] == 250.0
    assert result["refund"] == 250.0


def test_boundary_1_day():
    result = calculate_cancellation_fee(500, 1, "bronze", False, False)

    # 50% fee
    assert result["fee"] == 250.0
    assert result["refund"] == 250.0


def test_boundary_0_days():
    result = calculate_cancellation_fee(500, 0, "bronze", False, False)

    # 100% fee
    assert result["fee"] == 500.0
    assert result["refund"] == 0.0


