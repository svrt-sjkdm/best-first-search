import numpy as np

class node(object):
    """ Node class to represent the 4x4 matrix """
    def __init__(self, parent,matrix):
        self.parent = parent        # Parent of the current node
        self.h = None               # Heuristic of the node
        self.matrix = matrix        # 4x4 Matrix
        self.childs = list()        # List of childs
        
    def clone(self):
        clon = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        for i in range(4):
            clon[i] = self.matrix[i][:]
        return clon
    
    """ Find the index of the blank space in the matrix  """
    """ If found, it returns a list with the row and col """
    """ If not found, it returns an empty list..........."""
    def numIndex(self,num,*args):
        index = []
        j = 0
        if len(args)>0:
            m = args[0]
        else:
            m = self.matrix
        for i in range(0,len(m)):
            try:
                j = m[i].index(num)
            except ValueError:
                pass
            else:
                index.append(i)
                index.append(j)
        return index
        
    """ shifts up the blank space """
    def shiftUp(self):
        SUM = self.clone()
        indx = self.numIndex(0)
        if indx[0] == 0:
             return list()
        else:
            pastNum = SUM[indx[0]-1][indx[1]]
            SUM[indx[0]][indx[1]] = pastNum
            SUM[indx[0]-1][indx[1]] = 0
        return SUM

    """ shifts down the blank space """
    def shiftDown(self):
        SDM = self.clone()
        indx = self.numIndex(0)
        if indx[0] == len(SDM)-1:
            return list()
        else:
            pastNum = SDM[indx[0]+1][indx[1]]
            SDM[indx[0]][indx[1]] = pastNum
            SDM[indx[0]+1][indx[1]] = 0
        return SDM

    """ shifts left the blank space """
    def shiftLeft(self):
        SLM = self.clone()
        indx = self.numIndex(0)
        if indx[1] == 0:
            return list()
        else:
            pastNum = SLM[indx[0]][indx[1]-1]
            SLM[indx[0]][indx[1]] = pastNum
            SLM[indx[0]][indx[1]-1] = 0
        return SLM

    """ shifts right the blank space """
    def shiftRight(self):
        SRM = self.clone()
        indx = self.numIndex(0)
        if indx[1] == len(self.matrix)-1:
            return list()
        else:
            pastNum = SRM[indx[0]][indx[1]+1]
            SRM[indx[0]][indx[1]] = pastNum
            SRM[indx[0]][indx[1]+1] = 0
        return SRM

    """ compute the heuristic of the current node 
        using the manhatan distance
    """    
    def heuristic(self,goal):
        SUM = 0 
        for i in range(len(goal)**2+1):
            actualIndx = self.numIndex(i)
            goalIndx = self.numIndex(i,goal)
            SUM += sum([abs(x-y) for x,y in zip(goalIndx,actualIndx)])
        self.h = SUM
        return SUM
    
    """
        compute the cost of going to the start node
        to the current node
    """
    def cost(self):
        _cost = 0
        p = self.parent
        while p:
            p = p.parent
            _cost += 1
        return _cost 
    """
        generate a random 4x4 matrix
    """
    def randMatrix(self):
        m = []
        l = np.arange(16)
        l = np.random.permutation(l)
        m.append(list(l[0:4]))
        m.append(list(l[4:8]))
        m.append(list(l[8:12]))
        m.append(list(l[12:16]))
        self.matrix = m
        
    """
        print the node's matrix
    """
    def printM(self):
        for row in self.matrix:
            print(row)
        print('\n')
    