def calculate_powers(n):
    if not isinstance(n, (int, float)):
        raise ValueError("Input must be a number")

    return {
        "square": n ** 2,
        "cube": n ** 3,
        "fifth_power": n ** 5
    }
