def longest_word(string):
    return max(string.split(), key=len)

def char_frequency(string, char):
    return string.count(char)

def is_palindrome(string):
    return string == string[::-1]

def first_appearance_index(string, substring):
    return string.find(substring)

def word_occurrences(string):
    words = string.split()
    return {word: words.count(word) for word in set(words)}


input_string = "hello world programming python programming hello"
character_to_check = 'o'
substring_to_find = 'programming'


print("Word with the longest length:", longest_word(input_string))


print(f"Frequency of '{character_to_check}':", char_frequency(input_string, character_to_check))


print("Is palindrome:", is_palindrome(input_string))


print(f"Index of first appearance of '{substring_to_find}':", first_appearance_index(input_string, substring_to_find))


word_count_result = word_occurrences(input_string)
print("Word occurrences:", word_count_result)
