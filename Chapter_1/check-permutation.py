# Given two strings, write a method to decide if one is a permutation of the other

def is_permutation(str1, str2):
    if len(str1) == 0 or len(str1) != len(str2):
        return False

    str1_dict = {}
    str2_dict = {}

    for letter in str1:
        if letter in str1_dict.keys():
            str1_dict[letter] += 1
        else:
            str1_dict[letter] = 1

    for letter in str2:
        if letter in str2_dict.keys():
            str2_dict[letter] += 1
        else:
            str2_dict[letter] = 1

    return str1_dict == str2_dict


answer1 = is_permutation("abc", "cab")
answer2 = is_permutation("a", "abc")
answer3 = is_permutation("abc", "abb")

print("Should be True", answer1)
print("Should be False", answer2)
print("Should be False", answer3)
