#!/usr/bin/env python
num = 1000

d = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', }
d2 = {100: 'hundred', 1000: 'thousand', }
sum = 0
for n in range(1, num+1):
	if n % 100 and n > 100: sum += 3
	for x in sorted(d2, reverse=True):
		if n >= x:
			sum += len(d[n//x]) + len(d2[x])
			n = n % x
	if n >= 20: sum += len(d[n-n%10]) + len(d[n%10])
	else: sum += len(d[n])
print sum
