partOneTotal = 0
partTwoTotal = 0

with open('6.txt') as f:
    lines = f.readlines()
    partOneGroup = set()
    partTwoGroup = set()
    first = True

    for line in lines:
        line = line.strip()

        # a blank line is a new set. Add the group total to the major part One Total
        if ( len( line ) == 0 ):
            print( partTwoGroup )
            partOneTotal = partOneTotal + len( partOneGroup )
            partTwoTotal = partTwoTotal + len( partTwoGroup )
            partOneGroup = set()
            partTwoGroup = set()
            first = True
            continue

        # Pile all the chars on this line into the partOneGroup set.
        for c in line:
            partOneGroup.add( c )

        # the part two group is the intersection of this line and the current part two group
        if ( len( partTwoGroup ) == 0 and first ):
            partTwoGroup = partTwoGroup.union( partOneGroup )
        else:
            tempGroup = set()
            for c in line:
                tempGroup.add( c )
            partTwoGroup = partTwoGroup.intersection( tempGroup )

        first = False

print( partOneTotal )
print( partTwoTotal )