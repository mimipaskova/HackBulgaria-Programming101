def prime_number_of_divisors(n):
	sum=0
	i=n
	while (i>0):
		if n%i == 0:
			sum+=1
		i=i-1
	return is_prime(sum)

	

def is_prime(n):
	sum=0
	i=n
	if n ==1:
		return True
	while (i>0):
		if n%i == 0:
			sum+=i
		i=i-1
	if sum>1+n:
		return False
	return True


def main():
	print(prime_number_of_divisors(7))
	print(prime_number_of_divisors(8))
	print(prime_number_of_divisors(9))

if __name__ == '__main__':
	main()