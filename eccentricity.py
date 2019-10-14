import matplotlib.pyplot as plt

def is_julian(year, month, day):
	value = False
	if year <= 1582:
		if month <= 10:
			if day < 4:
				value = True

	return value


def get_jd(year, month, day):
	if month < 3:
		year -= 1
		month += 12

	B = 0

	if not is_julian(year, month, day):
		A = int(year / 100)
		B = 2 - A + int(A / 4)

	JD = int(365.25*(year + 4716)) + int(30.6001*(month+1)) + day + B - 1524.5

	return JD


def get_eccen(year, month, day):
	JD = get_jd(year, month, day)
	T = (JD - 2451545)/365250
	e = 0.0167086342 - 0.0004203654*T - 0.0000126734*(T**2) + 0.0000001444*(T**3) - 0.0000000002*(T**4) + 0.0000000003*(T**5)

	return e


if __name__ == "__main__":
	x_list = []
	y_list = []

	for i in range(-4000, 8000, 1000):
		x_list.append(i)
		y_list.append(get_eccen(i, 1, 1))

	plt.plot(x_list, y_list, linewidth=2)
	plt.show()
