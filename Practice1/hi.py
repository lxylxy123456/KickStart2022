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
	N = int(input())
	C = list(map(int, input().split()))
	assert len(C) == N
	if 0:
		# Google does not support sortedcontainers?
		import sortedcontainers
		ans = []
		papers = sortedcontainers.SortedList(key=lambda x: -x)
		cur_index = 0
		for i in C:
			papers.add(i)
			while cur_index < len(papers) and papers[cur_index] > cur_index:
				cur_index += 1
			ans.append(cur_index)
	if 1:
		import heapq
		accepted = []
		rejected = []
		cur_index = 0
		ans = []
		for i in C:
			heapq.heappush(rejected, -i)
			while rejected and accepted and -rejected[0] > accepted[0]:
				tmp1 = heapq.heappop(rejected)
				tmp2 = heapq.heappop(accepted)
				heapq.heappush(rejected, -tmp2)
				heapq.heappush(accepted, -tmp1)
			while rejected and -rejected[0] > cur_index:
				cur_index += 1
				tmp = heapq.heappop(rejected)
				heapq.heappush(accepted, -tmp)
			# print(rejected, accepted)
			ans.append(cur_index)
	print('Case #%d:' % (test + 1), *ans)

