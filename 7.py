bags = {}
path = set()

def walk( colour ):
	if ( colour in bags ):
		parents = bags.get( colour )
		for parent in parents:
			path.add( parent )
			walk( parent )

with open('7.txt') as f:
    lines = f.readlines()

    # ignoring the numbers, reexpress the txt file as a dictionary containing keys to sets. Since the
    # puzzle wants us to travel "up" the bag hierarchy, we'll build it upside down.
    for line in lines:
    	line = line.split( " contain " )
    	parent = line[0].replace( " bags","" ).strip()
    	children = line[1].strip().split(",")

    	for child in children:
    		# This special stirng marks the end of the tree
	    	if ( child == 'no other bags.' ):
	    		continue

	    	# Ignore that number for now and reduce the string to just the colour
	    	child = child[2:].strip()
	    	child = child.replace( " bags","" ).replace( " bag", "" ).replace( ".", "" )

	    	# ensure there's a set to enter the parent into, and then do so.
	    	if ( child not in bags ):
	    		bags.update( {child: set()} )
	    	parents = bags.get( child )
	    	parents.add( parent )

walk( "shiny gold") 
print( len(path) )
