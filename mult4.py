import mult4code

print('find a number that is evenly divisible by all the numbers between x and y')
print('Type "exit" to quit!')

def main():
	print('what number would you like to start from?')
	start = input('')
	if str(start).lower() == 'exit':
		print('have a nice day')
		exit()
	print('what number would you like to go to?')
	to = input('')
	if str(to).lower() == 'exit':
		print('have a nice day')
		exit()
	try:
		val = int(to)
	except ValueError:
		print(mult4code.error())
		main()
	try:
		val = int(start)
	except ValueError:
		print(mult4code.error())
		main()

	start = int(start)
	to = int(to)
	check = mult4code.check(start, to)
	factor = mult4code.factor(start, to)
	math = mult4code.math(start, to)
	if check == True:
		print('the answer is', math)
		main()
	else:
		print(check)
		main()


	
main()
