def slope( incx=3, incy=1 ):
	with open('3.txt') as f:
	    lines = f.readlines()
	    trees = 0
	    x = 0
	    skipCount = incy

	    for line in lines:
	    	# Are we skipping this line?
	    	if ( skipCount > 0 ):
	    		skipCount = skipCount - 1
	    		continue

	    	# reset the skip counter
	    	if ( skipCount == 0 and incy > 1 ):
	    		skipCount = incy-1

	    	line = line.rstrip()

	    	# Move three to the right and then modulo to wrap around the string ...
	    	x = (x+incx) % len(line)
	    	if ( line[x] == '#' ):
	    		trees = trees + 1

	return trees

# part one is just the default values for slope
print( slope() )

# part two is some multiplication ...
print( slope() * slope(1) * slope(5) * slope(7) * slope(1,2) )