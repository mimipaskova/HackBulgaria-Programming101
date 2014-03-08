def number_to_list(n):
	list=[]
	my_number=n
	while (my_number>0):
		my_digit=my_number%10	
		list = [my_digit] + list			
		my_number=my_number // 10
		#print(n)
	return list

	#list =  [int(i) for i in str(n)]
	#return list


def main():
	print(number_to_list(123))
	print(number_to_list(99999))
	print(number_to_list(123023))


if __name__ == '__main__':
	main()