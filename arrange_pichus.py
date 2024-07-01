
import sys
# Parse the map from a given filename
def parse_map(filename):
	with open(filename, "r") as f:
		return [[char for char in line] for line in f.read().rstrip("\n").split("\n")][3:]

# Count total # of pichus on house_map
def count_pichus(house_map):
    return sum([ row.count('p') for row in house_map ] )

# Return a string with the house_map rendered in a human-pichuly format
def printable_house_map(house_map):
    return "\n".join(["".join(row) for row in house_map])

# Add a pichu to the house_map at the given position, and return a new house_map (doesn't change original)
def add_pichu(house_map, row, col):
    a=house_map[0:row] + [house_map[row][0:col] + ['p',] + house_map[row][col+1:]] + house_map[row+1:]
    #print(printable_house_map(a))
    return a
    
#generating successors based on the house map,
# checking diagonally, row and column
def successors(house_map):
    traverse=[1,0]
    updated_housemap=[]
    row_len=len(house_map)
    col_len=len(house_map[0])
    #Initialising pichu as true initially
    pichu = True
    
    for row in range(row_len):
        for col in range(col_len):
            pichu = True
            if house_map[row][col] == '.':
                for k in traverse:
                    if k==1:
                        w= row-1
                        q= -1
                        s=-1
                    else:
                        w=row+1
                        q= row_len
                        s=1
                    #left up and down diagonally
                    for i,j in zip(range(w,q,s),range(col-1,-1,-1)):
                    
                        if house_map[i][j] == 'p':
                            #add false
                            pichu = False
                            break
                        if house_map[i][j] == 'X':
                            break
                        if house_map[row][j] == '@':
                            break
                    #right up and down diagonally
                    for i,j in zip(range(w,q,s),range(col+1,col_len,1)):
                        if house_map[i][j] == 'p':
                            #add false
                            pichu = False
                            break
                        if house_map[i][j] == 'X':
                            break
                        if house_map[row][j] == '@':
                            break
                    #row up and down
                    for i in range(w,q,s): 
                        if house_map[i][col] == 'p':
                            #add false
                            pichu = False
                            break
                        if house_map[i][col] == 'X':
                            break
                        if house_map[row][j] == '@':
                            break
                
                #col left and right
                for k in traverse:
                    if k==1:
                        w= col-1
                        q= -1
                        s= -1
                    else:
                        w=col+1
                        q= col_len
                        s=1
                    for j in range(w,q,s):
                        if house_map[row][j] == 'p':
                            #add false
                            pichu = False
                            break
                        if house_map[row][j] == 'X':
                            break
                        if house_map[row][j] == '@':
                            break
                #checking pichu flag if it has encountered any pichu's
                if (pichu):
                    updated_housemap.append(add_pichu(house_map, row, col))
                    print(updated_housemap)
    
    return updated_housemap
    #pass
    #return [ add_pichu(house_map, r, c) for r in range(0, len(house_map)) for c in range(0,len(house_map[0])) if house_map[r][c] == '.' ]

# check if house_map is a goal state
def is_goal(house_map, k):
    return count_pichus(house_map) == k


def solve(initial_house_map,k):
    fringe = [initial_house_map]
    while len(fringe) > 0:
        for new_house_map in successors( fringe.pop() ):
            if is_goal(new_house_map,k):
                return(new_house_map,True)
            fringe.append(new_house_map)
            
    #return false if it didn't find a solution by checking length of fringe
    if len(fringe) == 0:
        return(0,False)
# Main Function
if __name__ == "__main__":
    house_map=parse_map(sys.argv[1])
    # This is k, the number of agents
    k = int(sys.argv[2])
    print ("Starting from initial house map:\n" + printable_house_map(house_map) + "\n\nLooking for solution...\n")
    solution = solve(house_map,k)
    print ("Here's what we found:")
    print (printable_house_map(solution[0]) if solution[1] else "False")
