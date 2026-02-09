def main():
    n = int(input().strip())
    s = input().strip()
    result = []
    a, b = "", ""
    for c in s:
        if c >= a:
            a = c
            result.append("1")
        elif c >= b:
            b = c
            result.append("0")
        else:
            print("NO")
            return
    print("YES")
    print("".join(result))


main()
