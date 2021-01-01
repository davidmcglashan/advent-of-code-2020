# Load the input
with open('day 12 input.txt') as f:
	data = f.readlines()

	# initial boat state
	northSouth = 0
	eastWest = 0

	# waypoint delta
	wdNorth = 1
	wdEast = 10

	for line in data:
		op = line[0]
		mag = int(line[1:])

		# move to the waypoint _mag_ times.
		if op == 'F':
			northSouth += wdNorth*mag
			eastWest += wdEast*mag

		# move the waypoint
		if op == 'N':
			wdNorth += mag
		if op == 'E':
			wdEast += mag
		if op == 'S':
			wdNorth -= mag
		if op == 'W':
			wdEast -= mag

		# rotation means swapping the waypoint deltas around
		if op == 'R':
			if mag == 90:
				temp = wdEast
				wdEast = wdNorth
				wdNorth = 0-temp
			elif mag == 180:
				wdNorth *= -1
				wdEast *= -1
			elif mag == 270:
				temp = wdEast
				wdEast = 0-wdNorth
				wdNorth = temp
		if op == 'L':
			if mag == 90:
				temp = wdEast
				wdEast = 0-wdNorth
				wdNorth = temp
			elif mag == 180:
				wdNorth *= -1
				wdEast *= -1
			elif mag == 270:
				temp = wdEast
				wdEast = wdNorth
				wdNorth = 0-temp

		#print( op, mag, northSouth, eastWest, wdNorth, wdEast, abs(northSouth) + abs(eastWest) )

	# Calculate the Manhattan distance
	print abs(northSouth) + abs(eastWest) 