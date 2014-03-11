def what_is_my_sign(day, month):
	if month == 3:
		if day>=21:
			return "Aries"
		else:
			return "Pisces"

	if  month == 4:
		if day < 20:
			return "Aries"
		else:
			return "Taurus"

	if month == 5:
		if day < 21:
			return "Taurus"
		else:
			return "Gemini"

	if month == 6:
		if day < 21:
			return "Gemini"
		else:
			return "Cancer"

	if month == 7:
		if day < 22:
			return "Cancer"
		else:
			return "Leo"

	if  month == 8:
		if  day < 22:
			return "Leo"
		else:
			return "Virgo"

	if month == 9:
		if day < 23:
			return "Virgo"
		else:
			return "Libra"

	if month == 10:
		if day < 23:
			return "Libra"
		else:
			return "Scorpio"

	if month == 11:
		if  day < 22:
			return "Scorpio"
		else:
			return "Sagittarius"

	if month == 12:
		if day < 21:
			return "Sagittarius"
		else:
			return "Capricorn"

	if month == 1:
		if day<20:
			return "Capricorn"
		else:
			return "Aquarius"

	if month == 2:
		if day < 19:
			return "Aquarius"
		else:
			return "Pisces"

	'''
    Aries: 21 3 – 20 4
    Taurus: 21 4 – 21 5
    Gemini: 22 5 – 21 6
    Cancer: 22 6 – 22 7
    Leo: 23 7 – 22 8
    Virgo: 23 8 – 23 9
    Libra: 24 9 – 23 10
    Scorpio: 24 10 – 22 11
    Sagittarius: 23 11 – 21 12
    Capricorn: 22 12 – 20 1
    Aquarius: 21 1 – 19 2
    Pisces: 20 2 – 20 3
'''


def main():
	print(what_is_my_sign(5,8))
	print(what_is_my_sign(29,1))
	print(what_is_my_sign(30,6))
	print(what_is_my_sign(31,5))
	print(what_is_my_sign(2,2))
	print(what_is_my_sign(8,5))
	print(what_is_my_sign(9,1))

if __name__ == '__main__':
	main()
