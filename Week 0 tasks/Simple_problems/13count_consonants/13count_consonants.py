def count_consonants(str):
	br=0
	x=0
	str=str.upper()
	while (x<=(len(str)-1)):		
		if (ord(str[x])>=65 and ord(str[x])<=90 and ord(str[x])!=65 and ord(str[x])!=69 and ord(str[x])!=73 and ord(str[x])!=79 and ord(str[x])!=85 and ord(str[x])!=89):
			br = br + 1
		x=x+1
	return br


def main():
	print(count_consonants('Python'))
	print(count_consonants("Theistareykjarbunga"))
	print(count_consonants("grrrrgh!"))
	print(count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))
	print(count_consonants("A nice day to code!"))


if __name__ == '__main__':
	main()