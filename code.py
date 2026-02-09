def solution(l1):
    l1.sort()
    l1.reverse()
    c_out=""
    for x in l1:
        if x==l1[0]:
            c_out+=x
    return c_out
def answer():
    l1 = list(input())
    print(solution(l1))
answer()