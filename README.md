## Problem 1 Pichu-Route

State space is the map1.txt and map2.txt. the initial state is the location of p at the start of the given map. Goal state is the destination that p is trying to reach with shortest number of steps. The Cost function for the map1.txt is 16.

Added the function **direction** to calculate the path of traversal to reach the destination of the given map. In the current function the value of next step is stored for every move. We are storing the values of Y in move 1 and X in move 0. In Y -1 for L and +1 for R. In X -1 for U and + for D. The main function search is calling the direction fuction to get the final output. If there is no path we return -1.

Rest of the functions are given already.

## References 

* Class presentation and Lectures
* Geeks for Geeks
* few Other websites in the direction of BFS, DFS and some blind search algorithms




## Problem 2 Arrange Pichu

State space is the given map1.txt and map2.txt. The initial state is the given map with one pichu and the goal state is to palce the pichu's such that they dont attack each other. Cost function for this is high as the number of steps required are more.

Updated the successor function with a traverse list to traverse on the matrix such that we cover all the directions left,right,up, down and diagonally. based on the K we move up or down in row, column and diagonally. based on the position of the pichu we change that flag variable and generate the new housemap and keep on appending it to the final one. If the number of pichus to be inserted is more than suffiecient then we return the false.


## References

* Class Presentations and Lectures
* Blind Search algorithms
* https://github.com/pjhanwar/N-Queens-with-Obstacles/blob/master/Nqueens.py

