# Implement and algorithm to determine if a string has all unique characters. What if you cannot use additional data strutures?

# Using a set
def has_unique1(str):
    return len(str) == len(set(str))

# Not using a data structure


def has_unique2(str):
    if len(str) <= 1:
        return False
    str_list = list(str)
    str_list.sort()

    for i in range(0, len(str_list)-1):
        if str_list[i] == str_list[i+1]:
            return False

    return True
