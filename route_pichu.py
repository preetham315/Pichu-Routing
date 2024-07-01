
import sys

# Parse the map from a given filename
def parse_map(filename):
        with open(filename, "r") as f:
                return [[char for char in line] for line in f.read().rstrip("\n").split("\n")][3:]
                
# Check if a row,col index pair is on the map
def valid_index(pos, n, m):
        return 0 <= pos[0] < n  and 0 <= pos[1] < m

# Find the possible moves from position (row, col)
def moves(map, row, col):
        moves=((row+1,col), (row-1,col), (row,col-1), (row,col+1))

        # Return only moves that are within the house_map and legal (i.e. go through open space ".")

        return [ move for move in moves if valid_index(move, len(map), len(map[0])) and (map[move[0]][move[1]] in ".@")]


# Direction function to get the direction reaching the destination
def direction(move, curr_move, Next_step):
    if move[1] == curr_move[1]-1:         
        Next_step += "L"
    if move[1] == curr_move[1]+1:         
        Next_step += "R"
    if move[0] == curr_move[0] -1:        
        Next_step += "U"
    if move[0] == curr_move[0]+1:         
        Next_step += "D"
    return Next_step


def search(house_map):
        # Find the start position of pichu
        pichu_loc=[(row_i,col_i) for col_i in range(len(house_map[0])) for row_i in range(len(house_map)) if house_map[row_i][col_i]=="p"][0]
        fringe=[(pichu_loc,0,"")]
        while fringe:
                (curr_move, curr_dist, Next_step)=fringe.pop(0)
                for move in moves(house_map, *curr_move):
                        if house_map[move[0]][move[1]]=="@":
                                return (curr_dist+1, direction(move, curr_move, Next_step))  
                        fringe.append((move, curr_dist + 1, direction(move, curr_move, Next_step)))
        return -1    # return -1 if there is no solution

# Main Function
if __name__ == "__main__":
        house_map=parse_map(sys.argv[1])
        print("Shhhh... quiet while I navigate!")
        solution = search(house_map)
        print("Here's the solution I found:")
        print(str(solution[0]) + " " + str(solution[1]))
        