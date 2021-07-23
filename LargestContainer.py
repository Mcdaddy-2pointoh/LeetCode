class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        area = 0
        while start != end:
            if height[start] > height[end]:
                temp_area = height[end] * (end - start)
                if temp_area >= area:
                    area = temp_area

                end = end - 1

            else:
                temp_area = height[start] * (end - start)
                if temp_area >= area:
                    area = temp_area

                start = start + 1

        return area