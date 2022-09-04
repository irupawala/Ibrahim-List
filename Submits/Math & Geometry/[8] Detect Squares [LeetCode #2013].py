from collections import defaultdict

class DetectSquares:

    def __init__(self):
        self.ptsCount = defaultdict(int)
        self.pts = []

    def add(self, point) -> None:
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)
        

    def count(self, point) -> int:
        res = 0
        px, py = point
        #for x, y in self.ptsCount.keys():
        for x, y in self.pts:
            if (abs(px-x) != abs(py-y)) or x==px or y==py:
                continue 
            res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]

        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add([3, 10])
# obj.add([3, 10])
# obj.add([11, 2])
# obj.add([11, 2])
# obj.add([3, 2])
# obj.add([3, 2])
# param_2 = obj.count([11, 10])
# print(param_2)

'''
Time Complexity - O(n)
Space Complexity - O(n)
'''
