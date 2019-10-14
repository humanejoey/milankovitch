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


def get_obliquity(T):
	a = 23.0 + 26.0 / 60 + 21.448 / 3600
	b = 46.815 / 3600
	c = 0.00059 / 3600
	d = 0.001813 / 3600

	o = a - b*T - c*(T**2) + d*(T**3)
	return o


x_list = []
y_list = []

for i in range(-4000, 8000, 1000):
	x_list.append(i)
	y_list.append(get_jd(i, 1, 1))

plt.plot(x_list, y_list, linewidth=2)
plt.show()
