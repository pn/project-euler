#!/usr/bin/env python3

number = 1000000-1
elem_num = 10
elements = list(range(elem_num))
slot = elem_num
d = [1]
for i in range(1, elem_num + 1):
	d.append(d[i-1]*i)

result = ""
while number > 0 or slot > 0:
	elem = 0
	while d[slot-1] <= number:
		number -= d[slot-1]
		elem += 1
	result += str(elements[elem])
	elements.remove(elements[elem])
	slot-=1
print(result)
