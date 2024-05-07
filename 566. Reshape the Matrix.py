import numpy as np

class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        
        x = np.array(mat)

        if x.size != r * c:
            return mat
        
        new_x = x.reshape(r, c)

        reshaped_x = new_x.tolist()

        return reshaped_x

