class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows=len(board)
        columns=len(board[0])
        q=collections.deque()
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        visit=set()

        for r in range(rows):
            for c in range(columns):
                if (board[r][c] == 'O' and (r==0 or r==(rows-1)or c==0 or c==(columns-1))) :
                    q.append((r,c))
                    board[r][c]='T'
        while  q:
            row,column = q.popleft()
            visit.add((row,column))
            for r,c in directions :
                nr,nc=r+row ,c+column
                if(nr>=0 and  nc>=0 and nr<(rows-1) and  nc<(columns-1) and  (nr,nc) not in  visit and  board[nr][nc]=='O'):
                     board[nr][nc]='T'
                     q.append((nr,nc))
                     visit.add((nr,nc))
        for r in range(rows):
            for c in range(columns):
                if board[r][c] == 'O':
                    board[r][c] ='X'
                if board[r][c] =='T':
                    board[r][c]= 'O'
                


