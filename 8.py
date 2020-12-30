with open('8.txt') as f:
    lines = f.readlines()
    
    i = 0
    safety = len( lines )
    visited = set()
    acc = 0

    while safety > 0:
        print( safety )
        # have we been to this line before?
        if ( i in visited ):
            print( "*** repeated instruction ***" )
            break

        # log the visit
        visited.add( i )
        safety = safety - 1

        # determine the new value of i based on the line's content
        cmd = lines[i][:3]
        val = int( lines[i][3:] )

        if ( cmd == 'nop' ):
            i = i + 1

        if ( cmd == 'acc' ):
            i = i + 1
            acc = acc + val

        if ( cmd == 'jmp' ):
            i = i + val

        # Does the new value of i go beyond the end of the file?
        if ( i >= len( lines ) ):
            print( "*** EOF ***" )
            break

print( "counter:%d instruction:%d acc:%d" % (safety,i,acc) )