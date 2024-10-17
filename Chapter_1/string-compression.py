# Implement a method to peform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the compressed string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a-z).

def string_compression(user_string):

    letter_counts = []
    i = 0
    j = i + 1
    count = 1

    while i < len(user_string) and j < len(user_string):

        letter_counts.append(user_string[i])
        while j < len(user_string) and user_string[i] == user_string[j]:
            count += 1
            j += 1
        letter_counts.append(str(count))

        i = j
        j = i + 1
        count = 1

    compressed_string = "".join(letter_counts)
    if len(compressed_string) >= len(user_string):
        return user_string
    else:
        return compressed_string


answer = string_compression("aabcccccaaa")
print(answer)

# Take Home for While Loop Approach
# Read the question carefully: a {} object doesn't work here
# When you move pointers you typically use a while loop
# Always add checks with while loops to make sure pointers stay in bound
# When you move pointers around and count things, set the values at the end
# For example, if you move j forward, make sure to set i = j, j = i + 1 at the end


def string_compression2(user_string):
    letter_counts = []
    count = 1

    for i in range(1, len(user_string)):
        if user_string[i] == user_string[i-1]:
            count += 1
        else:
            letter_counts.append(user_string[i-1])
            letter_counts.append(str(count))
            count = 1

    letter_counts.append(user_string[-1])
    letter_counts.append(str(count))

    compressed_string = "".join(letter_counts)
    if len(compressed_string) >= len(user_string):
        return user_string
    else:
        return compressed_string

# Take Home for For Loop Approach
# This is harder to mentally grasp but cleaner
# You have to start at index 1 and look backward
# You add the i - 1 letter and count when there is no longer a match
# Because you are looking backward,
# You need to manually add the last letter at the end
# The logic is very confusing
