def max_purchase_rate(
    sale_rate,
    profit,
    processing,
    full_p, short_p, b2_p, b3_p
):
    factors = {
        "full": 1.0,
        "short": 0.5,
        "b2": 0.4,
        "b3": 0.3
    }

    effective_sale = (
        full_p * factors["full"] +
        short_p * factors["short"] +
        b2_p * factors["b2"] +
        b3_p * factors["b3"]
    ) * sale_rate

    max_rate = effective_sale - profit - processing
    return round(max_rate, 2)

