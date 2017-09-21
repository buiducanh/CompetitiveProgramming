class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        def area(a, b):
            return abs(b[0] - a[0]) * min(b[1], a[1])
        if len(height) <= 1:
            return None
        bars = list(map(height, lambda y, i: (i + 1, y)))
        max_left_bar = (1, height[0])
        next_bar = None
        next_right_bar = None
        max_area = 0
        for i, y in enumerate(height[1:]):
            right_bar = (i + 2, y)
            if right_bar[1] >= max_left_bar[1]:
                max_area = area(max_left_bar, right_bar)
                if (
                        next_bar is not None and right_bar[1] >= next_bar[1] and
                        area(right_bar, next_bar) > max_area
                    ):
                    next_right_bar = right_bar
            if y > max_left_bar[1] and next_bar is None:
                next_bar = (x, y)

        while next_bar:

