numlist = []
max = 99
maximum = 999999999

def factor(start, to):
	numlist.clear()
	for i in range(start,to + 1):
		numlist.append(i)
	while to > start:
		for i in range(start, to):
			if i == 0 or to == 0:
				pass
			elif to % i == 0 or to % i == -0:
				if i in numlist:
					numlist.remove(i)
		to = to - 1
	if to <= start:
		if 0 in numlist:
			numlist.remove(0)
		return(numlist)

def math(start, to):
	for numerator in range(to, maximum, to):
		if all(numerator % denominator == 0 for denominator in numlist):
			return(numerator)


def check(start, to,):
	if to < start:
		return(error())
	elif to - start > max:
		return(error())
	else:
		return(True)
def error():
	return('um... something went wrong')