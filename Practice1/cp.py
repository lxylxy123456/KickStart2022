try:
	import os, sys
	stdin = sys.stdin
	if len(sys.argv) > 1:
		stdin = open(sys.argv[1])
	else:
		# stdin = open('s.txt')
		stdin = open(os.path.splitext(__file__)[0] + '.txt')
	input = lambda: stdin.readline()[:-1]
except Exception:
	pass

# import math, sys
# sys.setrecursionlimit(100000000)
# from collections import defaultdict
# A = list(map(int, input().split()))

T = int(input())
for test in range(T):
	a = input()
	if any(map(a.endswith, 'aeiouAEIOU')):
		ans = 'Alice'
	elif any(map(a.endswith, 'yY')):
		ans = 'nobody'
	else:
		ans = 'Bob'
	ans = '%s is ruled by %s.' % (a, ans)
	print('Case #%d:' % (test + 1), ans)

