# Given a string, write a function to check if it is a pemutation of a palindrome. The palindrome isn't limited to dictionary words. You can ignore casing and non-letter characters.

# First Version (more memory overhead, more iteration, easy to understand)

def is_pal_permutation1(str):

    letter_counts = {}

    str = str.replace(" ", "").lower()

    for letter in str:
        if letter in letter_counts.keys():
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1

    letter_count_values = letter_counts.values()
    check_odds = [count for count in letter_count_values if count % 2 != 0]
    if len(check_odds) > 1:
        return False

    return True

# Refactored version (less memory overhead, less iteration, but harder to understand)


def is_pal_permutation2(str):

    letter_counts = {}
    odd_counts = 0

    for letter in str:
        if letter.isalpha():
            letter = letter.lower()
            if letter in letter_counts:
                letter_counts[letter] += 1
                if letter_counts[letter] % 2 != 0:
                    odd_counts += 1
                else:
                    odd_counts -= 1
            else:
                letter_counts[letter] = 1
                odd_counts += 1

    if odd_counts > 1:
        return False

    return True


value = is_pal_permutation2("aaa")
print("aaa", value)

value = is_pal_permutation2("aba")
print("aba", value)

value = is_pal_permutation2("a ba")
print("a ba", value)

value = is_pal_permutation2("abc")
print("abc", value)

value = is_pal_permutation2("abcdcba")
print("abcdcba", value)

value = is_pal_permutation2("Tact Coa")
print("Tact Coa", value)


# Take Home
# This problem is more about having the insight about what a palindrome is
# Once you know that it has to have duplicates of all letters and at most one unique letter, the rest is easy
