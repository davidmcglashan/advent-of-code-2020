joltages = []
with open('day 10 input.txt') as f:
    lines = f.readlines()

    for line in lines:
        joltages.append( int(line) )

    joltages.sort()
    print( joltages )
    ones = 0
    threes = 0

    for i in range( 1,len(joltages) ):
        if ( joltages[i] - joltages[i-1] == 1 ):
            ones += 1
        elif ( joltages[i] - joltages[i-1] == 3 ):
            threes += 1
    
    print( ones * (threes+1) )