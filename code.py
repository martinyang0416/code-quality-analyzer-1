def sm(s):
    if len(s) % 2 == 1:
        return s
    s1 = sm(s[:len(s) // 2])
    s2 = sm(s[len(s) // 2:])
    if s1 < s2:
        return s1 + s2
    else:
        return s2 + s1
    
if sm(input()) == sm(input()):
    print("YES")
else:
    print("NO")