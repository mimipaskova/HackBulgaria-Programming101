def count_vowels(str):
	br=0
	x=0
	while (x<=(len(str)-1)):
		if str[x] == "a" or str[x] == "e" or str[x] == "i" or str[x] == "o" or str[x] == "u" or str[x] == "y" or str[x] == "A" or str[x] == "E" or str[x] == "I" or str[x] == "O" or str[x] == "U" or str[x] == "Y":
			br = br + 1
		x=x+1
	return br


def main():
	print(count_vowels('Python'))
	print(count_vowels("Theistareykjarbunga"))
	print(count_vowels("grrrrgh!"))
	print(count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))
	print(count_vowels("A nice day to code!"))


if __name__ == '__main__':
	main()