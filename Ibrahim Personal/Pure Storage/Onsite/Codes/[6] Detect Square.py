from collections import defaultdict

class DetectSquares:

    def __init__(self):
        self.pts = []
        #self.ptsCount = {}
        self.ptsCount = defaultdict(int)
        

    def add(self, point: List[int]) -> None:
        self.pts.append(point)
        #self.ptsCount[tuple(point)] = self.ptsCount.get(tuple(point), 0) + 1
        self.ptsCount[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        #print(self.ptsCount)
        count = 0
        qx, qy = point
        for x, y in self.pts:
            if x == qx and y == qy: 
                continue # area > 0
            elif (abs(qx-x)) == (abs(qy-y)):
                #if (qx, y) in self.ptsCount and (x, qy) in self.ptsCount:
                    count += (self.ptsCount[(qx, y)] * self.ptsCount[(x, qy)])
                
        return count
                
# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)