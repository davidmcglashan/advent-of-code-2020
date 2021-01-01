# map the way the boat is facing to a north-south and east-west delta.
faces =  [ 'N','E','S','W']
norths = [  1,  0, -1,  0 ]
easts =  [  0,  1,  0, -1 ]

# Load the input
with open('day 12 input.txt') as f:
	data = f.readlines()

	# initial boat state
	facing = 1
	northSouth = 0
	eastWest = 0

	for line in data:
		op = line[0]
		mag = int(line[1:])

		# Move according to the deltas.
		if op == 'F':
			northSouth += norths[facing]*mag
			eastWest += easts[facing]*mag

		# Move according to the compass
		if op == 'N':
			northSouth += mag
		if op == 'E':
			eastWest += mag
		if op == 'S':
			northSouth -= mag
		if op == 'W':
			eastWest -= mag

		if op == 'R':
			if mag == 90:
				facing += 1
			elif mag == 180:
				facing += 2
			elif mag == 270:
				facing -= 1
		if op == 'L':
			if mag == 90:
				facing -= 1
			elif mag == 180:
				facing += 2
			elif mag == 270:
				facing += 1

		# modulo will wrap the facing properly
		facing = facing % 4

	print abs(northSouth) + abs(eastWest) 