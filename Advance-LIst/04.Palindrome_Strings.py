words = input().split(' ')
search_palindrome = input()
palindrome = []
for word in words:
    if word == "".join(reversed(word)):
        palindrome.append(word)


print(f"{palindrome}")
print(f'Found palindrome {palindrome.count(search_palindrome)} times')





#
# words = input().split(" ")
# search_palidrome = input()
# palidrome = [word for word in words if word == word[::-1]]
#
# found_palidrome = [word for word in words if word == search_palidrome]
# palidrome_count = len(found_palidrome)
#
# print(f'{palidrome}')
# print(f'Found palindrome {palidrome_count} times')

# First, read all the strings and the searched palindrome, and we create an empty list for the found palindromes
#2. Then, we create a loop that checks if each word is a palindrome:
# 3.We use the join() method with the reversed() method because reversed() returns an iterator, not a string, so we
# should make it into one.

# On the first line, you will receive words separated by a single space. On the second line,
# you will receive a palindrome. First, you should print a list containing all the found palindromes in the sequence.
# Then, you should print the number of occurrences of the given palindrome in the format: "Found palindrome {number} times