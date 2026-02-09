import sys
input = sys.stdin.readline

def solve():
    n,x,y=map(int,input().split())
    arr = []
    for i in range(1,n):
        if (y-x)%i==0:
            step = (y-x)//i
            smol = x%step
            if smol == 0:
                smol+=step
            total = smol+step*(n-1)
            arr.append((max(total,y),step))
        
    total,step = min(arr)
    print(*range(total-step*(n-1),total+1,step))

if __name__=="__main__":
    for _ in range(int(input())):
        solve()
