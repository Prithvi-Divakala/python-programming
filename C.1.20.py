import random


def shuffle(data):
    for a in range(len(data) - 1, 0, -1):

        b = random.randint(0, a)

        data[a], data[b] = data[b], data[a]


my_list = [1, 2, 3, 4, 5]
print("Original list", my_list)
shuffle(my_list)   # calling the function
print("Shuffled list", my_list)
