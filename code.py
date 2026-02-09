n, l, r = map(int, input().split())
l -= 1
r -= 1
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Check elements outside the l..r range
for i in range(n):
    if i < l or i > r:
        if a[i] != b[i]:
            print("LIE")
            exit()

# Check if the subarrays are permutations
a_sub = a[l:r+1]
b_sub = b[l:r+1]
if sorted(a_sub) == sorted(b_sub):
    print("TRUTH")
else:
    print("LIE")