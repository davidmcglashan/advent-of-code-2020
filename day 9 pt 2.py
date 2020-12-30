with open('day 9 input.txt') as f:
    lines = f.readlines()

    for i in range(0,len(lines)):
        sum = 0
        mn = 999999999999
        mx = 0
        for j in range( i,len(lines) ):
            val = int( lines[j] )
            mn = min( mn, val )
            mx = max( mx,val )
            sum += val
            if sum == 258585477:
                print( "%d + %d = %d" % (mn,mx,mn+mx) )