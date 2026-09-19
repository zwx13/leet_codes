class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        transp = []
        rows = len(matrix)
        cols = len(matrix[0])

        for row in range(cols):
            inner_list = []
            for col in range(rows):
                inner_list.append(matrix[col][row])
            
            transp.append(inner_list)

        return transp