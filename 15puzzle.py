# -*- coding: utf-8 -*-
import bfsearch as bfs
import nodo

ist0 = [[9, 1, 0, 7],
        [12, 14, 5, 3],
        [11, 13, 15, 10],
        [4, 6, 2, 8]]

ist1 = [[1, 2, 6, 3],
        [4, 9, 5, 7], 
        [8, 13, 11, 15],
        [12, 14, 10, 0]]

fst0 = [[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12],
       [13,14,15,0]]

fst1 = [[0, 1, 2, 3],
        [4, 5, 6, 7], 
        [8, 9, 10, 11],
        [12, 13, 14, 15]]

def main():
    
    """ Initial state node """
    initialState = nodo.node(None,ist0)
    #initialState.randMatrix()       
    """ Final state node """      
    finalState = nodo.node(None,fst0)

    print('\n\nInitial state:')
    initialState.printM()
    print('Final state')
    finalState.printM()
         

    """ Try to solve the puzzle using best first search """
    bfs_solution = bfs.astar(initialState,finalState)    
    """ Try to solve the puzzle using A* """
    #path1 = bfs.astar(initialState,finalState)

    """ Print the path to file """
    if len(bfs_solution[0]) > 0:
        with open('bfs_solution.txt','w') as file:
            file.write('Solution statistics:')
            file.write('\n\nNode expansions: ' + str(bfs_solution[1]))
            file.write('\nBlock movements: ' + str(bfs_solution[2]))
            file.write('\nSolution time: ' + str(bfs_solution[3]))
            file.write('\n\n\n')
            for matrix in bfs_solution[0]:
                for row in matrix:
                    file.write(str(row))
                    file.write('\n')
                    file.write('\n')
            
if __name__ == "__main__":
    main()