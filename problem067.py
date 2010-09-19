#!/usr/bin/env python
triangle_s = open('triangle.txt').read()

triangle = []
for row in triangle_s.split('\n'):
	try:
		triangle.append([int(num) for num in row.split(' ')])
	except:
		pass
	
result = triangle[len(triangle)-1]
for i in range(len(triangle)-2, -1, -1):
	r = []
	for j in range(len(triangle[i])):
		if triangle[i][j]+result[j] > triangle[i][j]+result[j+1]:
			r.append(triangle[i][j]+result[j])
		else: r.append(triangle[i][j]+result[j+1])
	result = r

print result[0]
