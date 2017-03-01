class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
    	for x in range(0,9):
    		setA=[]
    		setB=[]
    		for y in range(0,9):
    			if(board[x][y]!='.'):
    				if board[x][y] in setA:
    					#print "--a-",x,y
    					return False
    				else:
    					setA.append(board[x][y])
    			if(board[y][x]!='.'):
    				if board[y][x] in setB:
    					#print "--b-",y,x,board[y][x]
    					return False
    				else:
    					setB.append(board[y][x])
    	for x in range(0,3):
    		for y in range(0,3):
    			setC=[]
    			for i in range(0,3):
    				for j in range(0,3):
    					if board[x*3+i][y*3+j]!='.':
    						if board[x*3+i][y*3+j] in setC:
    							return False
    						else: 
    							setC.append(board[x*3+i][y*3+j])
    	return True
        
input=["..5.....6","....14...",".........",".....92..","5....2...",".......3.","...54....","3.....42.","...27.6.."]
s=Solution()
print s.isValidSudoku(input)