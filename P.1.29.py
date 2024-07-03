from itertools import permutations

characters = ['c', 'a', 't', 'd', 'o', 'g']
permu = permutations(characters)

for perm in permu:

     word = ''.join(perm)
     print(word)
     