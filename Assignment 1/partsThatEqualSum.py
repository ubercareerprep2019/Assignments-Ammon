# Ammon S Mugimu
# Uber Career Prep 2019
# Assignment 1

# Time complexity: O(N)
# Space complexity O(N)

# The algorithm is bulletproofed to handle undefined arguments, types, empty
# arrays, and ignores variables in the input_array that are not integers.
# Further, Negative and non-unique values are assumed to be possible.

def partsThatEqualSum(input_array, target_sum):
    if not input_array or not target_sum:
        return []
    elif type(input_array) != list or type(target_sum) != int or len(input_array) == 0:
        return []

    num_dict = dict()

    for num in input_array:
        if type(num) == int:
            if num not in num_dict:
                num_dict[num] = 1
            else:
                num_dict[num] += 1

    pair_array = []

    for num in input_array:
        if type(num) == int:
            target_value = target_sum - num

            if target_value in num_dict:
                if target_value == num:
                    if num_dict[target_value] >= 2:
                        pair_array.append((num, target_value))
                elif num_dict[target_value] > 0:
                    pair_array.append((num, target_value))

                num_dict[target_value] -= 1
                num_dict[num] -= 1

    return pair_array

