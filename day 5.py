allIds = set()

with open('day 5 input.txt') as f:
    lines = f.readlines()
    mx = 0
    mn = 999

    for line in lines:
        line = line.strip()
        row = line[:7]
        seat = line[7:]

        # the puzzle descriptions over-complicates what to do. It's basically a binary number where F is a 0, B is 1, etc.
        row = row.replace("F","0").replace("B","1")
        row = int(row,2)
        seat = seat.replace("L","0").replace("R","1")
        seat = int(seat,2)
        
        seatId = row * 8 + seat
        mx = max( mx, seatId )
        mn = min( mn, seatId )
        allIds.add(seatId)

    # part one is simply to return the max value
    print(mx)

    # part two is to find the missing int between mn and mx
    for i in range(mn,mx):
        if ( i not in allIds ):
            print( i )
            break

