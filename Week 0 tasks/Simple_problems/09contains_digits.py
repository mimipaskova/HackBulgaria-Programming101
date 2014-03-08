def contains_digits(number, digits):
	br=0

	for digit in digits:
		my_number=number
		while (my_number>0):
			my_digit=my_number%10	
			if my_digit == digit:
				br=br+1
				my_number=int(number/10)
		#print(number)

	if br >= len(digits):
		return True
	return False


def  main():
	print(contains_digits(402123, [0, 3, 4]))
	print(contains_digits(666, [6,4]))
	print(contains_digits(123456789, [1,2,3,0]))
	#print(contains_digits(456, []))

if __name__ == '__main__':
	main()