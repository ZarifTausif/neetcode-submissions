class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seencol={i:set() for i in range(9)}
        seensqu={i:{j:set() for j in range(3)} for i in range(3)}
        
        for i in range(9):
            seenrow=set()
            if i<=2:cboardRow=0
            elif 3<=i<=5:cboardRow=1
            else:cboardRow=2
            for j in range (9):
                current=board[i][j]
                if j<=2:cboardCol=0
                elif 3<=j<=5:cboardCol=1
                else:cboardCol=2

                currentboard=seensqu[cboardRow][cboardCol]

                if current in seenrow:
                    return False
                if current in seencol[j]:
                    return False
                if current in currentboard:
                    return False
                
                if current != '.':
                    seenrow.add(current)
                    seencol[j].add(current)
                    currentboard.add(current)
        return True







