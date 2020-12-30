# function used to evaluate records in part two. These are submitted as a single string which we'll tokenise
def partTwoEvaluate( rec ):
	eyeColours = {'amb','blu','brn','gry','grn','hzl','oth'}
	
	tokens = rec.split( " " )
	for token in tokens:

		# birth year is 1920-2002
		if ( token.startswith( "byr:" ) ):
			val = int( token[4:] )
			if ( val < 1920 or val > 2003 ):
				return 0

		# issue year is 2010-2020
		if ( token.startswith( "iyr:" ) ):
			val = int( token[4:] )
			if ( val < 2010 or val > 2020 ):
				return 0

		# expiry year is 2020-2030
		if ( token.startswith( "eyr:" ) ):
			val = int( token[4:] )
			if ( val < 2020 or val > 2030 ):
				return 0

		# height has two cases for in and cms
		if ( token.startswith( "hgt:" ) ):
			val = token[4:]
			if ( val.endswith( "cm" ) ):
				val = int(val[:len(val)-2])
				if ( val < 150 or val > 193 ):
					return 0
			elif ( val.endswith( "in" ) ):
				val = int(val[:len(val)-2])
				if ( val < 59 or val > 76 ):
					return 0
			else:
				return 0

		# hair colour is hexcode
		if ( token.startswith( "hcl:" ) ):
			val = token[4:];
			if ( len( val ) == 7 and val[0] == '#' ):
				# quick conversion from hex to validate the string
				hex = int(val[1:],16)
			else:
				return 0

		# eye colour is one of the supplied values
		if ( token.startswith( "ecl:" ) ):
			val = token[4:];
			if ( val not in eyeColours ):
				return 0

		# passport id is a nine digit number including leading zeroes
		if ( token.startswith( "pid:" ) ):
			val = token[4:];
			if ( len( val ) != 9 ):
				return 0

			# quick int conversion to validate the string
			val = int( val )

	# having survived all the tests return a valid record
	return 1

# main loop. Iterate the lines of the input file.
with open('4.txt') as f:
	lines = f.readlines()
		
	# Part one variables: Valid records have 8 colons, or 7 with the "cid:"" record also being present
	colons = 0
	cidFound = False
	partOneValid = 0

	# Part two variables: valid records meet stricter criteria - payload consolidates the record into a single string for processing
	payload = ""
	partTwoValid = 0

	for line in lines:
		line = line.strip()
		payload = payload + " " + line

		# A blank line means a new record so we can evaulate what we've found
		if ( len( line ) == 0 ):
			if ( colons == 8 or ( colons == 7 and not cidFound ) ):
				partOneValid = partOneValid + 1
				partTwoValid = partTwoValid + partTwoEvaluate( payload.strip() )

			# Reset the counters for the next record
			colons = 0
			cidFound = False
			payload = ""

		# part one counting
		colons = colons + line.count(':')
		cidFound = cidFound or line.count("cid:")

print( partOneValid )
print( partTwoValid )