class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        def calc_slope(a: list[int], b: list[int]) -> float:
            rise = b[1] - a[1]
            run = b[0] - a[0]
            if run == 0:
                return float('inf')
            else:
                return rise / run
        slope = calc_slope(coordinates[0], coordinates[1])
        for i in range(2, len(coordinates)):
            if calc_slope(coordinates[0], coordinates[i]) != slope:
                return False
        return True
