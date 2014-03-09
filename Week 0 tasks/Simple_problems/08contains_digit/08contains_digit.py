def contains_digit(number, digit):
	while (number>0):
		my_digit=number%10		
		if my_digit == digit:
			return True
		number=number//10
		print(number)
	return False


def main():
	print(contains_digit(123,4))
	print(contains_digit(42,2))
	print(contains_digit(1000,0))
	print(contains_digit(12346789,5))

if __name__ == '__main__':
	main()