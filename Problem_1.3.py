# // Time Complexity : O(n*m) 
# // Space Complexity : O(1)

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        min_n,max_n,min_m,max_m = 0,len(matrix),0,len(matrix[0])

        output = []
        
        while (min_n < max_n and min_m < max_m):
            
            for j in range(min_m,max_m):
                output.append(matrix[min_n][j])
            min_n += 1

            for i in range(min_n,max_n):
                output.append(matrix[i][max_m-1])
            max_m -= 1

            if min_n < max_n:
                for j in range(max_m-1,min_m-1,-1):
                    output.append(matrix[max_n-1][j])
                max_n -= 1
            if min_m < max_m:
                for i in range(max_n-1,min_n-1,-1):
                    output.append(matrix[i][min_m])
                min_m += 1

        return(output)