def sort(n,a):
    list = a
    for i in range(0,n):
        for j in range(0,n):
            if(list[i]>list[j]):
                t = list[i]
                list[i] = list[j]
                list[j] = t
    return list
def erase(n,a):
    temp=1
    list = sort(n,a)
    t=0
    print(a[(n)//2])
n = int(input())
a = [int(i) for i in input().split()]
erase(n,a)
            
            
    