def list_to_number(digits):
	x = len(digits) - 1
	power=0
	my_number=0
	while (x>=0):
		my_number = digits[x]*(10**power) + my_number
		power = power + 1
		x = x - 1
	return my_number


def main():
	print(list_to_number([1,2,3]))
	print(list_to_number([9,9,9,9,9]))
	print(list_to_number([1,2,3,0,2,3]))

if __name__ == '__main__':
	main()