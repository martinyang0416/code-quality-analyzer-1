import itertools

heroes = ['Anka', 'Chapay', 'Cleo', 'Troll', 'Dracul', 'Snowy', 'Hexadecimal']
hero_to_idx = {name: i for i, name in enumerate(heroes)}

n = int(input())
likes = [set() for _ in range(7)]
for _ in range(n):
    p, _, q = input().split()
    p_idx = hero_to_idx[p]
    q_idx = hero_to_idx[q]
    likes[p_idx].add(q_idx)

a, b, c = map(int, input().split())

candidates = []

for assignment in itertools.product([0, 1, 2], repeat=7):
    if 0 not in assignment or 1 not in assignment 