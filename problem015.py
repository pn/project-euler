#!/usr/bin/env python3
edge = 20

# solution 1
a = [[j for j in range(2, edge + 2)] for i in range(edge)]
for i in range(1, edge):
	for j in range(edge):
		if j: a[i][j] = a[i-1][j] + a[i][j-1]
		else: a[i][j] = a[i-1][j]+1
solution = a[edge-1][edge-1]
# solution 2
f1, f2 = 1, 1
for i in range(1, edge+1):
	f1 *= i
for i in range(edge+1, (2*edge)+1):
	f2 *= i
solution = f2//f1
print(solution)
