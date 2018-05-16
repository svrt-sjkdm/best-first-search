# -*- coding: utf-8 -*-
import nodo
import time

def validMoves(node):
    valid_moves = []
    nsu = node.shiftUp()
    nsd = node.shiftDown()
    nsl = node.shiftLeft()
    nsr = node.shiftRight()

    if nsu:
        valid_moves.append(nsu)
    if nsd:
        valid_moves.append(nsd)
    if nsl:
        valid_moves.append(nsl)
    if nsr:
        valid_moves.append(nsr)
        
    return valid_moves

"""
    Heuristic search: Best First Search
"""            
def bfsearch(start,goal):
    openl = []                # Open nodes list
    closedl = []              # Closed nodes list
    path = []                 # Path of the solution
    moves = 0                 # Number of movements to solve the puzzle
    expansions = 0            # Number of node expansions 
    start_time = time.time()  # Start time of the search
    
    start.h = 0
    openl.append([start.h,start])
    
    while openl:
        current = openl.pop(0)                         # Pop item from queue
        cm = current[1].matrix                          
        gm = goal.matrix
        if cm == gm:
            end_time = time.time()                     # End time of the search
            # Form the path by going from
            # the goal node to the root node
            node = current[1]
            while node.parent:
                path.append(node.matrix)
                node = node.parent
                moves += 1
            path.append(node.matrix)
            break
        else:
            # Expanssion of the valid nodes (returns a matrix)
            for node_matrix in validMoves(current[1]):
                if  node_matrix not in closedl:
                    n = nodo.node(current[1],node_matrix)
                    n.h = n.heuristic(goal.matrix)
                    current[1].childs.append([n.h,n])
                    openl.append([n.h,n])
                
            openl = sorted(openl,key=lambda x: x[0]) # Sort list based on heuristic
            closedl.append(current[1].matrix)
            expansions += 1
            
    if len(path) > 0:
        print('The puzzle was solved!')
        print('\nSolution statistics: ')
        print('\nNode expansions: ', expansions)
        print('Block movements : ', moves)
        print('Solution time: ',float(end_time-start_time),'[s]\n')
        path.reverse()
    else:
        print('\nNo solution was found...')
        
    return [path,expansions,moves,float(end_time-start_time)]

"""
    Heuristic searh: A*
"""
def astar(start,goal):
    
    openl = []
    closedl = []
    path = []
    start_time = time.time()
    expansions = 0
    moves = 0
    
    start.h = 0
    
    openl.append([start.h,start])
    
    while openl:
        
        current = openl.pop(0)
        cm = current[1].matrix
        gm = goal.matrix
        
        if cm == gm:
            end_time = time.time()
            node = current[1] 
            while node.parent:
                path.append(node.matrix)
                node = node.parent
                moves += 1
            path.append(node.matrix)
            break
        
        else:
            # Expanssion of the valid nodes (returns a matrix)
            for node_matrix in validMoves(current[1]):
                if  node_matrix not in closedl:
                    n = nodo.node(current[1],node_matrix)
                    n.h = n.heuristic(goal.matrix) + n.cost()
                    current[1].childs.append([n.h,n])
                    openl.append([n.h,n])
                
            openl = sorted(openl,key=lambda x: x[0]) # Sort list based on heuristic
            closedl.append(current[1].matrix)
            expansions += 1
            
    if len(path) > 0:
        print('The puzzle was solved!')
        path.reverse()
    else:
        print('\nNo solution was found...')
    return [path,expansions,moves,float(end_time-start_time)]