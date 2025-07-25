"""

2013. Detect Squares

You are given a stream of points on the X-Y plane. Design an algorithm that:

• Adds new points from the stream into a data structure. Duplicate points are 
  allowed and should be treated as different points.

• Given a query point, counts the number of ways to choose three points from 
  the data structure such that the three points and the query point form an 
  axis-aligned square with positive area.

An axis-aligned square is a square whose edges are all the same length and are 
either parallel or perpendicular to the x-axis and y-axis.

Implement the DetectSquares class:

• DetectSquares() Initializes the object with an empty data structure.

• void add(int[] point) Adds a new point point = [x, y] to the data structure.

• int count(int[] point) Counts the number of ways to form axis-aligned squares 
  with point point = [x, y] as described above.



Example 1:

Input
["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
[[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]
Output
[null, null, null, null, 1, 0, null, 2]

Explanation
DetectSquares detectSquares = new DetectSquares();
detectSquares.add([3, 10]);
detectSquares.add([11, 2]);
detectSquares.add([3, 2]);
detectSquares.count([11, 10]); // return 1. You can choose:
                               //   - The first, second, and third points
detectSquares.count([14, 8]);  // return 0. The query point cannot form a square 
                                  with any points in the data structure.
detectSquares.add([11, 2]);    // Adding duplicate points is allowed.
detectSquares.count([11, 10]); // return 2. You can choose:
                               //   - The first, second, and third points
                               //   - The first, third, and fourth points

"""

# Solution 1: Hash Map - I [✔️]
# Time Complexity: O(1) for add(), O(n) for count().
# Space Complexity: O(n)

class DetectSquares:

    def __init__(self):
        self.ptsCount = defaultdict(int) # type: ignore
        self.pts = []

    def add(self, point: List[int]) -> None: # type: ignore
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point: List[int]) -> int: # type: ignore
        res = 0
        px, py = point
        for x, y in self.pts:
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue
            res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]
        return res


######## ######## ######## ######## ######## ######## ########


# Solution 2: Hash Map - II (Optimal)
# Time Complexity: O(1) for add(), O(n) for count().
# Space Complexity: O(n)

class CountSquares:

    def __init__(self):
        self.ptsCount = defaultdict(lambda: defaultdict(int)) # type: ignore

    def add(self, point: List[int]) -> None: # type: ignore
        self.ptsCount[point[0]][point[1]] += 1

    def count(self, point: List[int]) -> int: # type: ignore
        res = 0
        x1, y1 = point
        for y2 in self.ptsCount[x1]:
            side = y2 - y1
            if side == 0:
                continue

            x3, x4 = x1 + side, x1 - side
            res += (self.ptsCount[x1][y2] * self.ptsCount[x3][y1] *
                    self.ptsCount[x3][y2])

            res += (self.ptsCount[x1][y2] * self.ptsCount[x4][y1] *
                    self.ptsCount[x4][y2])
        return res