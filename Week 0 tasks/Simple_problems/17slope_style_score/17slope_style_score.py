def slope_style_score(scores):
	scores.remove(min(scores))
	scores.remove(max(scores))
	lenth=len(scores)
	x = 0
	sum = 0
	while (x<=lenth - 1):
		sum = sum + scores[x]
		x = x + 1

	medium_score = sum/(lenth)

	return  "{:.2f}".format(medium_score)


def main():
	print(slope_style_score([94, 95, 95, 95, 90]))
	print(slope_style_score([60, 70, 80, 90, 100]))
	print(slope_style_score([96, 95.5, 93, 89, 92]))


if __name__ == '__main__':
	main()