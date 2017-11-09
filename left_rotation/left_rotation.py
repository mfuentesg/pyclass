def left_rotation(rotations, array):
    if rotations != len(array):
        return array[rotations:] + array[:rotations]
    return array


print([1,2,3,4,5], ' -> ', left_rotation(4, [1,2,3,4,5]))
print([1,2,3], ' ' , left_rotation(3, [1,2,3]))