"""

286. Walls and Gates

You are given a m x n 2D grid initialized with these three possible values:

    1. -1 - A water cell that can not be traversed.
    2. 0 - A treasure chest.
    3. INF - A land cell that can be traversed. 
       We use the integer 2^31 - 1 = 2147483647 to represent INF.

Fill each land cell with the distance to its nearest treasure chest. If a 
land cell cannot reach a treasure chest then the value should remain INF.

Assume the grid can only be traversed up, down, left, or right.

Modify the grid in-place.



Example 1:



Example 2:



"""