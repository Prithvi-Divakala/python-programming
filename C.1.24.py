def no_of_vowels(v):
    vowels = {'a', 'e', 'i', 'o', 'u'}

    vowel_count = 0

    for char in v:

        if char in vowels:
            vowel_count += 1

    return vowel_count


string = "Little boy from Rosario"
print("Number of vowels:", no_of_vowels(string))

