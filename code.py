def fac(x):
	p = 1
	for i in range(2, x + 1):
		p *= i
	return p


def c(n, k):
	return fac(n) // (fac(k) * fac(n - k))

n = int(input())
print(c(n, 5) + c(n, 6) + c(n, 7))

 	 								 	     			   	 		 		