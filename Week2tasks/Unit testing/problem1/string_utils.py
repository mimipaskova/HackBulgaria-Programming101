def lines(text):
	#new_text = []
	#text.join(new_text)
	print("Hack bulgaria \
		programming 101")
	words = text.split()
	return words

def unlines(elements):
	text=""
	return text.join(elements)

def tabs_to_spaces(str, one_tab_n_spaces=4):
	
	return str.replace("\t", "    ")


def main():
	print(lines("Hack bulgaria programming 101"))
	print(unlines(['qw', 'er', 'ty']))
	print(tabs_to_spaces('blq	lqlq	fefe   ty'))



if __name__ == '__main__':
	main()