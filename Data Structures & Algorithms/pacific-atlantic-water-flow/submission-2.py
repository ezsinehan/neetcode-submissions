class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows = len(heights)
        cols = len(heights[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        output = []

        def dfs(r, c, visited):
            visited.add((r, c))
            canReachPacific = (r == 0 or c == 0)
            canReachAtlantic = (r == rows - 1 or c == cols - 1)

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if not (0 <= nr < rows):
                    continue
                if not (0 <= nc < cols):
                    continue
                if (nr, nc) in visited:
                    continue
                if heights[nr][nc] > heights[r][c]:
                    continue

                childPacific, childAtlantic = dfs(nr, nc, visited)
                canReachPacific |= childPacific
                canReachAtlantic |= childAtlantic

                if canReachPacific and canReachAtlantic:
                    return True, True

            return canReachPacific, canReachAtlantic

        for r in range(rows):
            for c in range(cols):
                visited = set()
                canReachPacific, canReachAtlantic = dfs(r, c, visited)

                if canReachPacific and canReachAtlantic:
                    output.append([r, c])

        return output