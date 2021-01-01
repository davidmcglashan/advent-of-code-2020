# class to model the state of each chair. The geographic position of each neighbouring chair
# doesn't matter so we can cram them in a list.
class Chair:
	def __init__( self, row, column ):
		self.state = 'L'
		self.row = row
		self.column = column
		self.changeTo = 'L'
		self.neighbours = list()

	def addNeighbour( self,nb ):
		if self.column == nb.column and self.row == nb.row:
			return
		self.neighbours.append( nb )
		#print( 'chair at %d,%d has %d neighbours (%d,%d)' % (self.row,self.column,len(self.neighbours), nb.row,nb.column))

	def change( self ):
		count = 0
		for nb in self.neighbours:
			if nb.state == '#':
				count += 1

		# Empty chairs with no occupied neighbours become occupied. Occupied chairs need more than four
		# occupied nieghbours to become vacant.
		if self.state == 'L' and count == 0:
			self.changeTo = '#'
			return True
		elif self.state == '#' and count >= 4:
			self.changeTo = 'L'
			return True

		return False

	def commit( self ):
		self.state = self.changeTo

chairs = {}

# Load the input
with open('day 11 input.txt') as f:
	data = f.readlines()

	# hash the new chairs by their row/col position
	for row in range( 0, len(data)):
		for col in range( 0,len(data[row])):
			if data[row][col] == 'L':
				chair = Chair(row,col)
				chairs[row*100+col] = chair

	# Now build up the neighbouring relationships
	for chair in chairs.values():
		for r in range( chair.row-1, chair.row+2 ):
			for c in range( chair.column-1, chair.column+2 ):
				key = r*100+c
				if key >= 0 and key in chairs:
					chair.addNeighbour( chairs[key] )

	# Ask the chairs to change their state until none of them do
	while True:
		count = 0
		for chair in chairs.values():
			if chair.change():
				count += 1
		for chair in chairs.values():
			chair.commit()
		print( "%d changes" % count )
		if count == 0:
			break;

	# Now simply count the occupied chairs
	count = 0
	for chair in chairs.values():
		if chair.state == '#':
			count += 1
	print( "%d occupied chairs" % count )