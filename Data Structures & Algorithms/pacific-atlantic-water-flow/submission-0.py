class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(r, c, visited):
            visited.add((r, c))
            canReachPacific = (r == 0 or c == 0)
            canReachAltantic = (r == rows - 1 or c == cols - 1)

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nr > rows - 1:
                    continue
                if nc < 0 or nc > cols - 1:
                    continue
                if heights[nr][nc] > heights[r][c]:
                    continue
                if (nr, nc) in visited:
                    continue

                
                childPacific, childAltantic = dfs(nr, nc, visited)
                canReachPacific = childPacific or canReachPacific
                canReachAltantic = childAltantic or canReachAltantic

            return canReachPacific, canReachAltantic

        rows = len(heights)
        cols = len(heights[0])
        output = []

        for r in range(rows):
            for c in range(cols):
                visited = set()
                canReachPacific, canReachAltantic = dfs(r, c, visited)

                if canReachPacific and canReachAltantic:
                    output.append([r, c])

        return output

        