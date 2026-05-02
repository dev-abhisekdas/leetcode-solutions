def length_of_longest_substring(s: str) -> int:
    char_index = {}
    left = 0
    max_length = 0

    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1

        char_index[char] = right
        max_length = max(max_length, right - left + 1)

    return max_length

    
if __name__ == '__main__':
    str1 = "abcabcbb"
    str2 = "bbbbb"
    str3 = "abcabcbb"
    print(length_of_longest_substring(str1))
    print(length_of_longest_substring(str2))
    print(length_of_longest_substring(str3))