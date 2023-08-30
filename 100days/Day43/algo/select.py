# def selection(arr):
#     n = len(arr)
#     for i in range(n):
#         j 
#         min = 0
#         while j >= 0 and arr[j] < arr[min]:
#             arr[]


# def insertion(arr):
#     n = len(arr)
#     for i in range(n):
#         key = arr
# arr = ["hey", "are"]
# for i in arr:
#     a = str(i)
#     print(a)

# def reverse_sentence(sentence):
#     words = sentence.split()  # Split the sentence into a list of words
#     reversed_words = words[::-1]  # Reverse the order of the words
#     reversed_sentence = ' '.join(reversed_words)  # Join the reversed words into a sentence
#     swapped_sentence = reversed_sentence.swapcase()
#     return swapped_sentence
# sentence = "aWESOME is cODING"
# reversed_sentence = reverse_sentence(sentence)
# print(reversed_sentence)  # Output: "dOg rUns"

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
#             'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 
#             'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
#               't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
#             'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 
#             'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
#               't', 'u', 'v', 'w', 'x', 'y', 'z']
# numbers = [0,1,2,3,4,5,6,7,8,9,]

# def missing(s):

#     global alphabet
#     global numbers 
#     splitted = s.split()
#     for i in s:
#         if i not in alphabet:


def find_missing_chars(s):
    missing_digits = []
    missing_chars = []

    # Check for missing digits
    for digit in "0123456789":
        if digit not in s:
            missing_digits.append(digit)

    # Check for missing characters
    for char in sorted(set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")):
        if char not in s:
            missing_chars.append(char)

    return ''.join(missing_digits + missing_chars)


s = "8hypotheticall024y6wxz"