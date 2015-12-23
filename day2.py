def area(l, w, h):
	return 2*l*w + 2*w*h + 2*h*l

def smallest(l, w, h):
	return sorted([l*w, w*h, h*l])[0]


def wrap(l, w, h):
	return sum(map(lambda x: x*2, sorted([l, w, h])[0:2]))

def bow(l, w, h):
	return l * w * h

with open('day2.txt') as f:

	totalpaper = 0
	totalribbon = 0

	for line in f:
		l, w, h = map(int, line.split('x'))

		totalpaper += area(l, w, h) + smallest(l, w, h)

		totalribbon += wrap(l, w, h) + bow(l, w, h)

	print 'Paper: ', totalpaper
	print 'Ribbon: ', totalribbon


