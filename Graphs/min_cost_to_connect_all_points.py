import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        total_cost = 0
        heap = [(0,0)]
        seen = set()

        while len(seen) < n:
            dist, i = heapq.heappop(heap)
            if i in seen:
                continue

            seen.add(i)
            total_cost += dist
            xi, yi = points[i]

            for j in range(n):
                if j not in seen:
                    xj, yj = points[j]
                    nei_dist = abs(xi-xj) + abs(yi-yj)
                    heapq.heappush(heap, (nei_dist,j))

        return total_cost

    # Time Complexity : O(n^2 log(n)) where n is number of the points
    # or O(E log(E)) where E is the number of edges, which is n^2
    # Space Complexity : O(n^2) or O(E)