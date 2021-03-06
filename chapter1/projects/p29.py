# Given 'catdog' find all possible strings formed exactly once
from itertools import permutations 

def all_catdog():
    all_perm = [''.join(p) for p in permutations('catdog')]
    unique = set(all_perm)
    print(unique)

if __name__ == "__main__":
    all_catdog()