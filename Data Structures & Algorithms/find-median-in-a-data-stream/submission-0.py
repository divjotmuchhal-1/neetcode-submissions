class MedianFinder:
    def __init__(self):
        self.array = []

    def addNum(self, num: int) -> None:
        self.array.append(num)
        self.array.sort()  # in-place

    def findMedian(self) -> float:
        n = len(self.array)
        mid = n // 2
        if n % 2 == 1:
            return float(self.array[mid])
        return (self.array[mid - 1] + self.array[mid]) / 2.0
