def matches( bank, find ):
    for i in range( 0,25 ):
        for j in range( 0,25 ):
            if i == j:
                continue
            if bank[i] + bank[j] == find:
                return True
    return False

bank = []

with open('9.txt') as f:
    lines = f.readlines()

    for line in lines:
        # build the bank during the preamble
        if ( len( bank ) < 25 ):
            bank.append( int(line) )
            continue

        # current value must be the sum of two previous values
        find = int(line)
        if not matches( bank, find ):
            print( "%d is not found in the bank" % find )
            break

        # maintain the last 25 entries
        bank.pop(0)
        bank.append( find )
