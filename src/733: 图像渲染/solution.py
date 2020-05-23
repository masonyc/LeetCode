def floodFill(self, image: List[List[int]], sr: int, sc: int,
              newColor: int) -> List[List[int]]:
    def dfs(sr: int, sc: int):
        if (0 <= sr < len(image) and 0 <= sc < len(image[0])
                and image[sr][sc] != newColor and image[sr][sc] == oldColor):
            image[sr][sc] = newColor
            dfs(sr - 1, sc)
            dfs(sr + 1, sc)
            dfs(sr, sc - 1)
            dfs(sr, sc + 1)

    oldColor = image[sr][sc]
    dfs(sr, sc)
    return image
