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
	print(is_prime(1))
	print(is_prime(2))
	print(is_prime(8))
	print(is_prime(11))
	print(is_prime(-10))

if __name__ == '__main__':
	main()
