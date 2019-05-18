# Ammon S Mugimu
# Uber Career Prep 2019
# Assignment 1

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
