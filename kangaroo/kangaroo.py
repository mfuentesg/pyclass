#!/bin/python3


def kangaroo(k1, k2):
    """"We need to find the jumps number to satisfy the follow equation.

    x1 + j * v1 = x2 + j * v2 -> where j is the jumps number

    Constraints:
        -  v1 > v2
        - j must be a positive number

    Solving the equation
        x1 + j * v1 = x2 + j * v2
        j * v1 - j * v2 = x2 - x1
        j = |x1 - x2|
            ---------
            |v2 - v1|
    """

    x1, v1 = k1
    x2, v2 = k2

    # if this condition is true, the kangaroos never will meet
    if v1 <= v2:
        return False

    # calculating the jumps number
    j = abs(x1 - x2) // abs(v1 - v2)

    return (x1 + v1 * j) == (x2 + v2 * j)