class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        
        left, right = 0, len(matrix)-1
        while left <= right:
            mid = (left + right) // 2
            median = matrix[mid]
            
            if(median[-1] >= target):
                for j in median:
                    if(j == target):
                        return True
                else:
                    continue
            
            elif(median[-1] < target):
                left = mid + 1
            
            else:
                right = mid - 1
        
        return False

s = Solution()
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
