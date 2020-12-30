bags = {}

def walk( parent ):
    # count the bag we're in as 1. It'll be multiplied by the method caller
    childCount = 1

    # If this bag holds no others, return the count and end the treewalk.
    if ( parent[2:] not in bags ):
        return childCount
        
    # Extract each child's multipler and use it with the returned recursive walk() value.
    children = bags.get( parent[2:] )
    for child in children:
        multiplier = int( child[0] )
        childCount = childCount + ( multiplier * walk(child) )

    return childCount

with open('7.txt') as f:
    lines = f.readlines()

    # part two is a more conventional travel down the tree problem, but we need to count the numbers this time!
    for line in lines:
    	line = line.split( " contain " )
    	parent = line[0].replace( " bags","" ).strip()
    	children = line[1].strip().split(",")

    	for child in children:
    		# This special stirng marks the end of the tree
	    	if ( child == 'no other bags.' ):
	    		continue

	    	# Keep the numbers in this one. we'll do the counting when we walk the tree rather than 
            # build a special data structure now.
	    	child = child.strip()
	    	child = child.replace( " bags","" ).replace( " bag", "" ).replace( ".", "" )

            # this time we build the dictionary parent -> children
	    	# ensure there's a set to enter the parent into, and then do so.
	    	if ( parent not in bags ):
	    		bags.update( {parent: set()} )
	    	children = bags.get( parent )
	    	children.add( child )

# This tree counts the size of the tree, but the puzzle wants us to NOT include the tree's root
# (how many bags inside your bag) so we subtract one from the treewalk answer. 
print( walk( "1 shiny gold") - 1 )