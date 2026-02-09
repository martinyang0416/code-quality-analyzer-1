def read():
	return tuple(int(x) for x in input().split())

def main():
	(h, ) = read()
	a = read()
	tree = []
	fi = 0
	flag = False
	for i, x in enumerate(a):
		if fi == 0:
			if not flag and x > 1:
				flag = True
			elif flag and x > 1:
				fi = len(tree)
			else:
				flag = False
		tree.extend([len(tree)] * x)
	if fi == 0:
		print('perfect')
		return
	else:
		print('ambiguous')
	print(' '.join(str(x) for x in tree))
	tree[fi] = fi - 1
	print(' '.join(str(x) for x in tree))

main()