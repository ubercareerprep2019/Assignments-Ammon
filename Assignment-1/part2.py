# Ammon S Mugimu
# Uber Career Prep 2019
# Assignment-1

# Question 1.

# Time complexity: O(M + N)
# Space complexity O(M)

def isStringPermution(s1, s2):
    if not s1 or not s2:
        return False
    elif type(s1) != str or type(s2) != str or len(s1) != len(s2):
        return False

    char_dict = dict()

    # Populate dictionary with character counts from s1.
    for char in s1:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1

    # Iterate over s2, checking dictionary for similar characters.
    for char in s2:
        if char not in char_dict:
            return False
        else:
            current_char_count = char_dict[char]
            if current_char_count > 0:
                char_dict[char] -= 1
            else:
                return False

    # If no edge case has been reached by this point, the strings are permutations.
    return True


# Question 2.

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

