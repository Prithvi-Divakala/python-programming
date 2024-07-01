# list comprehension syntax to produce the list, but without having to type all 26 such characters.

letters = [chr(list('a') + i) for i in range(26)]
print(letters)
 