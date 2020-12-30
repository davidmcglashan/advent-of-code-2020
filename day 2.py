with open('day 2 input.txt') as f:
    lines = f.readlines()
    ptOneValid = 0
    ptTwoValid = 0

    for line in lines:
	    token = line.split(' ')

	    # first token is the min and max separated by a -
	    rnge = token[0].split('-')
	    mn = int(rnge[0])
	    mx = int(rnge[1])

	    # second token is the character (and a :)
	    char = token[1][0]

	    # third token is the password itself. This we do the comparison on (twice as it turns out). First comparison
	    # is the count of char in the password must be between mn and mx
	    c = token[2].count(char)
	    if ( c >= mn and c <= mx ):
	    	ptOneValid = ptOneValid + 1

	    # Second comparison is actually XOR
	    if ( (token[2][mn-1] == char) ^ (token[2][mx-1] == char) ):
	    	ptTwoValid = ptTwoValid + 1

print( ptOneValid )
print( ptTwoValid )