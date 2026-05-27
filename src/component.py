def calculate_cancellation_fee(
    booking_amount,
    days_before,
    membership_level,
    peak_season,
    non_refundable
):
    # Validation
    if booking_amount < 0:
        raise ValueError("Booking amount cannot be negative")

    if days_before < 0:
        raise ValueError("Days before cannot be negative")

    valid_memberships = ["bronze", "silver", "gold"]
    if membership_level not in valid_memberships:
        raise ValueError("Invalid membership level")

    # Non-refundable override
    if non_refundable:
        return {
            "fee": booking_amount,
            "refund": 0.0
        }

    # Base fee percentage
    if days_before >= 30:
        fee_percent = 20
    elif days_before >= 7:
        fee_percent = 20
    elif days_before >= 1:
        fee_percent = 50
    else:
        fee_percent = 100

    # Peak season charge
    if peak_season:
        fee_percent += 10

    if fee_percent > 100:
        fee_percent = 100

    fee = booking_amount * (fee_percent / 100)

    # Membership discount
    discounts = {
        "bronze": 0,
        "silver": 10,
        "gold": 20
    }

    discount = discounts[membership_level]
    fee = fee - (fee * discount / 100)

    refund = booking_amount - fee

    return {
        "fee": round(fee, 2),
        "refund": round(refund, 2)
    }