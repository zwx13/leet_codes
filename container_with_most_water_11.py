class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        max_area = 0

        while right > left:
            width = right - left
            current_height = min(height[left], height[right])
            current_area = width * current_height

            max_area = max(max_area, current_area)

            if height[right] > height[left]:
                left += 1
            else:
                right -= 1

        return max_area