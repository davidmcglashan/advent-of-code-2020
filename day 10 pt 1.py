joltages = []

with open('day 10 input.txt') as f:
    lines = f.readlines()

    for line in lines:
        joltages.append( int(line) )

    # In order to consider the first joltage we need to start at zero. This means we have to
    # explicitly include it in the result set so we can count the step up to the first value
    # properly.
    joltages.append( 0 )

    joltages.sort()

    ones = 0
    threes = 0
    for i in range( 1,len(joltages) ):
        if ( joltages[i] - joltages[i-1] == 1 ):
            ones += 1
        elif ( joltages[i] - joltages[i-1] == 3 ):
            threes += 1
    
    # Add one to the threes because there's always a 3 jolt gap to the last device, according
    # to the instruction text.
    print( ones * (threes+1) )