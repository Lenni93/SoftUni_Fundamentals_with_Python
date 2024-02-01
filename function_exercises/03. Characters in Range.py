characters_one = input()
characters_two = input()


def find_characters(num1, num2):
    num1 = int(ord(num1) + 1)
    num2 = int(ord(num2))
    for n in range(num1, num2):
        print(chr(n), end=" ")


find_characters(characters_one, characters_two)






# Write a function that receives two characters and returns a single string with all the characters in between them
# (according to the ASCII code), separated by a single space. Print the result on the console.