# Write a method to replace all spaces in a string with %20. You may assume that the string has sufficient space at the end, and that you are give the "true" length of the string.

# To solve this, you need to write down how you want to use the pointer
# You rearrange items within a fixed-length array during iteration

def urlify_c(str, true_length):
    list_string = list(str)
    pointer = len(list_string)

    for i in reversed(range(true_length)):
        if list_string[i] == " ":
            list_string[pointer - 3: pointer] = "%20"
            pointer -= 3

        else:
            list_string[pointer - 1] = list_string[i]
            pointer -= 1

    return "".join(list_string)


answer = urlify_c("Mr John Smith    ", 13)
print(answer)


# What we can do in Python instead

def urlify_python(str, true_length):
    new_string = str[:true_length:1].replace(" ", "%20")
    return new_string


answer = urlify_python("Mr John Smith    ", 13)
print(answer)

# Take Home:
# You have to know how you are moving pointers around
# Personally, I can't track multiple pointers in my head
# I need some method to write out or I get immediately lost
# I also didn't know these concepts:
# reversed(range(10)) will count from 9 back to zero
# my_list[2:5] = "abc" will replace indices 2, 3, 4 with a, b, c
