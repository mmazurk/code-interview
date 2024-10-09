
# Given two strings, write a funciton to check if they are one edit (or zero edits) away. One edit means: insert a character, remove a character, or replace a character

# The problem with using sets is that it doesn't preserve the order of the strings
# So ("abc", "cba") will return True and that's wrong
# Therefore, this problem is much harder than it looks

def one_word_away(str1, str2):

    length_difference = abs(len(str1) - len(str2))
    if length_difference > 1:
        return False
    elif length_difference <= 1:
        set1 = set(str1)
        set2 = set(str2)
        non_matching = set1.symmetric_difference(set2)
        if len(non_matching) > 2:
            return False

    return True

# You have to preserve the order so there are some tricks
# Obviously if the lengths are different by x > 1 you retun false
# If the strings are equal, you can use a trick whereby you zip them together
# Then you check the letter pairs to see if things are only off by one
# For the case where they are different by one, you use pointers
# You have to decide on putting the longer or shorter string first
# You can easily do this by comparing and swapping
# Then you iterate through them and set a found_difference boolean


def one_word_away_better(str1, str2):
    if abs(len(str1) - len(str2)) > 1:
        return False

    # if lengths are equal
    if len(str1) == len(str2):
        count = 0
        zipped_string = zip(str1, str2)
        for char1, char2 in zipped_string:
            if char1 != char2:
                count += 1
            if count > 1:
                return False

    # make the first longer
    if len(str2) > len(str1):
        str1, str2 = str2, str1

    index_str1 = 0
    index_str2 = 0
    found_diff = False

    while index_str1 < len(str1) and index_str2 < len(str2):
        if str1[index_str1] != str2[index_str2]:
            if found_diff:
                return False
            found_diff = True
            index_str1 += 1
        else:
            index_str2 += 1
            index_str1 += 1

    return True


a1 = one_word_away_better("pale", "ple")
a2 = one_word_away_better("pales", "pale")
a3 = one_word_away_better("pale", "bale")
a4 = one_word_away_better("pale", "bake")
a5 = one_word_away_better("spale", "pale")

print("True", a1)
print("True", a2)
print("True", a3)
print("False", a4)
print("True", a5)

# Take Homes:
# When you are compaing words, order matters so you can't use a set
# When you are matching words, think in terms of word length
# If one is longer, you can easily put the longer or shorter one first
# To compare words when order matters, you have to go letter by letter
# You can zip or use pointers
