class Solution:
    def findTheCity(self, n, edges, distanceThreshold):
        dist = [[float("inf")] * n for _ in range(n)]
        for i, j, w in edges:
            # i到j 和 j到i 的距离为相同
            dist[i][j] = dist[j][i] = w
        for i in range(n):
            # 自己到自己的距离为0
            dist[i][i] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    # Floyd-Warshall算法
                    # https://en.wikipedia.org/wiki/Floyd–Warshall_algorithm
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        res = {
            sum(d <= distanceThreshold for d in dist[i]): i for i in range(n)}
        return res[min(res)]
