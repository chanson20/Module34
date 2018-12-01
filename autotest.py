import mult4code
givenstart = 1
givento = 10
expectedcheck = True
expectedfactor = [6, 7, 8, 9, 10]
expectedmath = 2520
expectedlist = [expectedcheck, expectedfactor, expectedmath]
check = mult4code.check(givenstart,givento)
factor = mult4code.factor(givenstart,givento)
math = mult4code.math(givenstart,givento)

if expectedmath == math and expectedfactor == factor and expectedcheck == check:
	print('Test Complete: Everything works dandily.')
else:
	if expectedmath != math:
		print('math failed')
		print('expected output %s, received output %s' % (expectedmath, math))
	if expectedfactor != factor:
		print('factor failed')
		print('expected output %s, received output %s' % (expectedfactor, factor))
	if expectedcheck != check:
		print('check failed')
		print('expected output %s, received output %s' % (expectedcheck, check))