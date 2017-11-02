from kangaroo import kangaroo


def test(base, expected):
    result = "SUCCESS" if base == expected else "FAILED"
    print("Case {} == {} ~> {}".format(base, expected, result))


test(kangaroo((0, 3), (4, 2)), True)
test(kangaroo((0, 3), (4, 2)), True)
test(kangaroo((0, 3), (4, 2)), True)
test(kangaroo((0, 3), (4, 2)), True)
test(kangaroo((0, 3), (4, 2)), True)
test(kangaroo((0, 3), (4, 2)), True)
test(kangaroo((0, 3), (4, 2)), True)
