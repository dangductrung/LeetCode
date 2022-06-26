class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        Row, Column = len(image), len(image[0])
        value = image[sr][sc]
        if value == color:
            return image 
        def transform(r, c):
            if image[r][c] == value:
                image[r][c] = color

                if r >= 1:
                    transform(r - 1, c)
                if r + 1 < Row:
                    transform(r + 1, c)
                if c >= 1:
                    transform(r, c - 1)
                if c + 1 < Column:
                    transform(r, c + 1)    

        transform(sr, sc)
        return image