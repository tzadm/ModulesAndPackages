def divide(first, second):
    import math as mt
    if second == 0:
        return mt.inf
    else:
        return first / second


if __name__ == '__main__':
    divide(0, 0)
