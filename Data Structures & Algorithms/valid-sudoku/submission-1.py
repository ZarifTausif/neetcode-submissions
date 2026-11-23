class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seencol={i:set() for i in range(9)}
        seensqu={i:{j:set() for j in range(3)} for i in range(3)}
        
        for i in range(9):
            seenrow=set()
            cboardRow=i//3
            for j in range (9):
                current=board[i][j]
                if current=='.':
                    continue
                cboardCol=j//3

                currentboard=seensqu[cboardRow][cboardCol]

                if(current in seenrow
                or current in seencol[j]
                or current in currentboard
                ):
                    return False
                
                seenrow.add(current)
                seencol[j].add(current)
                currentboard.add(current)
        return True







