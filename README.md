# Robot Safe Coordinate Search

## What am I trying to solve?

There is a robot which can move around on a grid. The robot is placed at point (0, 0). From (x, y)
the robot can move to (x+1, y), (x-1, y), (x, y+1), and (x, y-1). Some points are dangerous and
contain EMP Mines. To know which points are safe, we check whether the sum digits of abs(x)
plus the sum of the digits of abs(y) are less than or equal to 23. For example, the point (59, 75) is
not safe because 5 + 9 + 7 + 5 = 26, which is greater than 23. The point (-51, -7) is safe because 5+ 1 + 7 = 13, which is less than 23.

How large is the area that the robot can access?

It was an **interview** task, details are [here](https://github.com/EsratMaria/RobotSafeSpaceSearch/blob/master/ProblemDescription.pdf).
