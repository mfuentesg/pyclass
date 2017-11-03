from kangaroo import kangaroo


def test(base, expected):
    result = "SUCCESS" if base == expected else "FAILED"
    print("Case {} == {} ~> {}".format(base, expected, result))


test(kangaroo((0, 3), (4, 2)), True)
test(kangaroo((3, 3), (2, 2)), False)
test(kangaroo((0, 3), (0, 3)), True)
test(kangaroo((35, 1), (45, 3)), False)
test(kangaroo((3585, 7317), (6994, 9610)), False)