class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        l = 0
        r = len(matrix) - 1 #3 because at the last index we want to shuffle(add) thats why we are minusing the last index here

        while l < r:
            for i in range(r-l):
                top = l 
                bottom = r

                #store topleft element
                top_left = matrix[top][l+i]

                #move bottomleft element to topleft
                matrix[top][l+i] = matrix[bottom-i][l]

                #move bottomright to bottomleft
                matrix[bottom-i][l] = matrix[bottom][r-i]

                #move topright to bottomright
                matrix[bottom][r-i] = matrix[top + i][r]

                #move topleft to my top right
                matrix[top+i][r] = top_left

            r-=1
            l+=1



