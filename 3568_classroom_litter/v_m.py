class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        total_rows = len(classroom)
        total_cols = len(classroom[0])

        max_energy = energy

        l_index = 0
        l_index_map = {}

        best_visited = {}

        for r in range(total_rows):
            for c in range(total_cols):
                if classroom[r][c] == 'S':
                    start_r = r
                    start_c = c
                    break

        for r in range(total_rows):
            for c in range(total_cols):
                if classroom[r][c] == 'L':
                    l_index_map[r * total_cols + c] = l_index
                    l_index += 1
                    
        total_bit_map = (1 <<  l_index) - 1

        best_visited[start_r, start_c, 0] = energy

        if total_bit_map == 0:
            return 0

        def bfs(r, c, energy, bmap = 0, steps = 0):
            q = deque()

            q.append((r, c, energy, bmap, steps))

            directions = (
                (0, 1),
                (0, -1),
                (-1, 0),
                (1, 0)
            )

            while q:
                r, c, energy, bmap, steps = q.popleft()

                if energy == 0:
                    continue

                for d_r, d_c in directions:
                    curr_r = d_r + r
                    curr_c = d_c + c

                    new_bmap = bmap

                    if curr_r >= total_rows or curr_r < 0 or curr_c >= total_cols or curr_c < 0:
                        continue
                    
                    if classroom[curr_r][curr_c] == 'X':
                        continue

                    if classroom[curr_r][curr_c] == 'L':
                        new_bmap |= 1 << l_index_map[curr_r * total_cols + curr_c]
                    
                    if new_bmap == total_bit_map:
                        return steps + 1

                    curr_energy = energy - 1

                    if classroom[curr_r][curr_c] == 'R':
                        curr_energy = max_energy

                    state = (curr_r, curr_c, new_bmap)
                    if state in best_visited and best_visited[state] >= curr_energy:
                        continue
                    
                    best_visited[state] = curr_energy

                    q.append((curr_r, curr_c, curr_energy, new_bmap, steps + 1))
                
            return -1

        total_steps = bfs(start_r, start_c, energy)
        
        return total_steps