#!/usr/bin/env python

names = open('names.txt').read().replace('"', '').split(',')
# solution 1
d = dict.fromkeys(names)
for i in d:
	d[i] = sum([ord(c)-ord('A')+1 for c in i])
s = 0
n = 1
for i in sorted(d):
	s += d[i] * n
	n+=1
print s

# solution 2
names.sort()
res = 0
for i in range(len(names)):
    res += sum([ord(ch) - ord('A')+1 for ch in names[i]]) * (i + 1)
print res
