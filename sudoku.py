class Solution:
    
    def solve_sudoku_puzzle(self,board):
        """
        Args:
         board(list_list_int32)
        Returns:
         list_list_int32
        """
        # Write your code here.
        #To check if the board has blank spaces or 0
        def find_empty(board):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == 0:
                        return (i ,j)
            return None
            
        def valid(board, num, pos):
            
            # row check
            for i in range(len(board[0])):
                if board[pos[0]][i] == num and pos[1] != i:
                    return False
            # col check        
            for i in range(len(board)):
                if board[i][pos[1]] == num and pos[0] != i:
                    return False
                    
            # check Box
            box_x = pos[1] // 3
            box_y = pos[0] // 3
            
            for i in range(box_y*3, box_y*3 + 3):
                for j in range(box_x*3, box_x*3 + 3):
                    if board[i][j]==num and pos != (i,j):
                        return False
                        
            return True
            
        find = find_empty(board)
        
        if not find:
            return True
        else:
            row, col = find
            
        for i in range(1,10):
            if valid(board, i, (row, col)):
                board[row][col]=i
                
                if solve_sudoku_puzzle(board):
                    return board
                    
                board[row][col]=0
                
        return None

board= [
[8, 4, 9, 0, 0, 3, 5, 7, 0],
[0, 1, 0, 0, 0, 0, 0, 0, 0],
[7, 0, 0, 0, 9, 0, 0, 8, 3],
[0, 0, 0, 9, 4, 6, 7, 0, 0],
[0, 8, 0, 0, 5, 0, 0, 4, 0],
[0, 0, 6, 8, 7, 2, 0, 0, 0],
[5, 7, 0, 0, 1, 0, 0, 0, 4],
[0, 0, 0, 0, 0, 0, 0, 1, 0],
[0, 2, 1, 7, 0, 0, 8, 6, 5]
]
sol=Solution()
print(sol.solve_sudoku_puzzle(board))
