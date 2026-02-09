t = int(input())
for _ in range(t):
    s, c = input().split()
    if s < c:
        print(s)
        continue
    s_list = list(s)
    n = len(s_list)
    found = False
    for i in range(n):
        min_char = s_list[i]
        min_pos = -1
        for j in range(i + 1, n):
            if s_list[j] < min_char:
                min_char = s_list[j]
                min_pos = j
            elif s_list[j] == min_char:
                min_pos = j
        if min_pos != -1 and min_char < s_list[i]:
  