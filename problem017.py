#!/usr/bin/env python
num = 1000

# solution 1
d = {0: '', 1: 'one', 2: 'two', 3: 'three',
4: 'four',
5: 'five',
6: 'six',
7: 'seven',
8: 'eight',
9: 'nine',
10: 'ten',
11: 'eleven',
12: 'twelve',
13: 'thirteen',
14: 'fourteen',
15: 'fifteen',
16: 'sixteen',
17: 'seventeen',
18: 'eighteen',
19: 'nineteen',
20: 'twenty',
30: 'thirty',
40: 'fourty',
50: 'fifty',
60: 'sixty',
70: 'seventy',
80: 'eighty',
90: 'ninety',
100: 'hundred',
1000: 'thousand',
}
sum = 0
for i in range(1, num+1):
	n = i
	w = ''
	ge_100 = False
	while n > 0:
		if n >= 1000:
			ge_100 = True
			w = "%s %s" % (d[n//1000], d[1000])
			sum += len(d[n//1000]) + len(d[1000])
			n = n % 1000
		elif n >= 100:
			ge_100 = True
			w += " %s %s" % (d[n//100], d[100])
			sum += len(d[n//100]) + len(d[100])
			n = n % 100
		else:
			if ge_100:
				w += ' and'
				sum += 3
			if n >= 20:
				w += " %s %s" % (d[n-n%10], d[n%10])
				sum += len(d[n//10]) + len(d[10])
				n = n % 1
			else:
				w += " %s" % d[n]
				sum += len(d[n])
				n = n % 1
		if n == 0: print '%d: %s' % (i, w)
		
print sum
