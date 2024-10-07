class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        
        visited = [[False for _ in range(n)] for _ in range(m)]

        result = []

        directions = [(0,1), (1,0), (0,-1),(-1,0)]
        current_direction = 0

        i, j = 0, 0

        for _ in range(m*n):
            result.append(matrix[i][j])
            visited[i][j] = True

            next_i = i + directions[current_direction][0]
            next_j = j + directions[current_direction][1]

            if not (0 <= next_i < m and 0 <= next_j < n and not visited[next_i][next_j]):
                current_direction = (current_direction+1) % 4
                next_i = i + directions[current_direction][0]
                next_j = j + directions[current_direction][1]
            
            i, j = next_i, next_j
        return result

                