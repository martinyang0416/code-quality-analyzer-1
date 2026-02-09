n = int(input())
for _ in range(n):
    word = input().strip()
    count_a = word.count('a')
    if count_a == 0:
        print(0)
    else:
        total = 2 ** len(word)
        non_a = len(word) - count_a
        subtract = 2 ** non_a
        print(total - subtract)