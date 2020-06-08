def is_power(x, y):
    """Check if y is a power of x"""
    if x == 1:
        return y == 1

    pow = 1
    while pow < y:
        pow *= x

    return pow == y


def is_power_10(y):
    """Check if y is a power of 10"""
    while y > 1:
        y /= 10
        if y % 1 != 0:
            return False

    return y == 1


print(is_power(10, 1000))
print(is_power_10(1000))
print(is_power_10(500))
