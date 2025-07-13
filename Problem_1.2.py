# // Time Complexity : O(n*m) 
# // Space Complexity : O(1)
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        
        upFlag = 1
        m = len(matrix)
        n = len(matrix[0])
        i,j = 0,0
        result = []
        while(i<m and j<n):
            result.append(matrix[i][j])
            if(upFlag):
                if(j == n-1):
                    i = i+1
                    upFlag = 0
                elif(i == 0):
                    j = j+1
                    upFlag = 0
                else:
                    i = i-1
                    j = j+1
            else:
                if(i == m-1):
                    j = j+1
                    upFlag = 1
                elif(j == 0):
                    i = i+1
                    upFlag = 1
                else:
                    i = i+1
                    j = j-1
        return result
                        
