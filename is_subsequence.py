# Author: Delainee Lenss
# GitHub username: delainee64
# Date: 02/11/2023
# Description: Write a recursive function named is_subsequence that
# takes two string parameters and returns True if the first string
# is a subsequence of the second string, but returns False otherwise.

def is_subsequence(first_str, second_str):
    """Returns whether the first string is a subsequence of the second string."""
    if len(first_str) != 0 and len(second_str) == 0:
        return False
    if len(first_str) == 0:
        return True
    if first_str[0] == second_str[0]:
        return is_subsequence(first_str[1:], second_str[1:])
    else:
        return is_subsequence(first_str, second_str[1:])

# first_str = "aeiou"
# second_str = "facetious"
# print(is_subsequence(first_str, second_str))
