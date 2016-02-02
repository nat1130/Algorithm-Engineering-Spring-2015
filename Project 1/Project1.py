###############################################################################
# CPSC 335 Project 1
# Spring 2015
#
# Authors: <FILL IN YOUR NAME(S) HERE>
###############################################################################

# constant parameters
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 800
CANVAS_MARGIN = 20
BOX_OUTLINE_COLOR = 'olive'
BOX_FILL_COLOR = 'mint cream'
HULL_OUTLINE_COLOR = 'gold'
HULL_FILL_COLOR = 'linen'
INTERIOR_POINT_COLOR = 'gray'
POINT_RADIUS = 2
OUTLINE_WIDTH = 2

import math, random, time, tkinter

# Class representing one 2D point.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# input: a list of Point objects
# output: a 4-tuple (x_min, y_min, x_max, y_max)
# x_min, y_min, x_max, y_max
def bounding_box(points):
    # This stub code is not correct and needs to be replaced with your
    # working algorithm implementation.
    minXIndex = 0;
    maxXIndex = 0;
    minYIndex = 0;
    maxYIndex = 0;
    p = 0
    for p in range(p + 1, len(points)):
        #print(p)
        if (points[p].x < points[minXIndex].x):
            minXIndex = p
            # maxXIndex = minXIndex
        if (points[p].x > points[maxXIndex].x):
            maxXIndex = p
        if (points[p].y < points[minYIndex].y):
            minYIndex = p
        if (points[p].y > points[maxYIndex].y):
            maxYIndex = p
            # maxYIndex = minYIndex
    # return (p.minXIndex, p.minYIndex, p.maxXIndex, p.maxYIndex)
    minXValue = points[minXIndex].x
    minYValue = points[minYIndex].y

    maxXValue = points[maxXIndex].x
    maxYValue = points[maxYIndex].y
    return (points[minXIndex].x, points[minYIndex].y, points[maxXIndex].x, points[maxYIndex].y)


# def bounding_box(points):
# # This stub code is not correct and needs to be replaced with your
# # working algorithm implementation.
#     xList = []
#     yList = []
#     for i in range(len(points)):
#         xList.append(points[i].x)
#         yList.append(points[i].y)
#
#     SelectionSort(xList)
#     SelectionSort(yList)
#
#     return (xList[0], yList[0], xList[len(xList) - 1], yList[len(yList) - 1])

# def SelectionSort(list):
#     for k in range(len(list) - 1):
#         least = k
#         for i in range(k + 1, len(list)):
#             if(list[i] < list[least]):
#                 least = i
#
#         list[k], list[least] = list[least], list[k]
#
#     return list

# Are two Points the same or not
def areEqual(p, q):
    return p.x == q.x and q.y == q.y

# Find A Match
# Returns true if found, otherwise false
def findMatch(points, p):
    for k in range (len(points)):
        if areEqual(points[k], p):
            return True
    return False

# Cross product of 2 Points
# O is origin
def crossProduct(o, a, b):
    result = (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)
    return result

def convex_hull(points):
    # points in the hull boundary
    H = []
    # k = 0
    for i in range(len(points)):
        for j in range(len(points)):
            if areEqual(points[i],  points[j]) is False:
                k = 0
                for l in range(len(points)):
                    # k = 0
                    if areEqual(points[l], points[i]) is False and areEqual(points[l], points[j]) is False:
                        # cross is wrong, need to fix it
                        # for all point l, the cross has to be greater than 0 to add i and j into H
                        # otherwise, it will not add
                        cross = crossProduct(points[i], points[j], points[l])
                        if cross > 0:
                            k += 1
                        else:
                            if k == 0 or k == len(points) - 2:
                                continue
                            else:
                                break

                if k == 0 or k == len(points) - 2:
                    if findMatch(H, points[i]) is False:
                        H.append(points[i])
                    if findMatch(H, points[j]) is False:
                        H.append(points[j])
    return H




###############################################################################
# The following code is reponsible for generating instances of random
# points and visualizing them. You can leave it unchanged.
###############################################################################

# input: an integer n >= 0
# output: n Point objects with all coordinates in the range [0, 1]
def random_points(n):
    return [Point(random.random(), random.random())
            for i in range(n)]


# translate coordinates in [0, 1] to canvas coordinates
def canvas_x(x):
    return CANVAS_MARGIN + x * (CANVAS_WIDTH - 2 * CANVAS_MARGIN)


def canvas_y(y):
    return CANVAS_MARGIN + y * (CANVAS_HEIGHT - 2 * CANVAS_MARGIN)


# extract the x-coordinates (or y-coordinates respectively) from a
# list of Point objects
def xs(points):
    return [p.x for p in points]


def ys(points):
    return [p.y for p in points]


# input: a non-empty list of numbers
# output: the mean average of the list
def mean(numbers):
    return sum(numbers) / len(numbers)


# input: list of Point objects
# output: list of the same objects, in clockwise order
def clockwise(points):
    if len(points) <= 2:
        return points
    else:
        center_x = mean(xs(points))
        center_y = mean(ys(points))
        return sorted(points,
                      key=lambda p: math.atan2(p.y - center_y,
                                               p.x - center_x),
                      reverse=True)


# Run one trial of one or both of the algorithms.
#
# 1. Generates an instance of n random points.
# 2. If do_box is True, run the bounding_box algorithm and display its output.
# 3. Likewise if do_hull is True, run the convex_hull algorithm and display
#    its output.
# 4. The run-times of the two algorithms are measured and printed to standard
#    output.
def trial(do_box, do_hull, n):
    print('generating n=' + str(n) + ' points...')
    points = random_points(n)

    if do_box:
        print('bounding box...')
        start = time.perf_counter()
        (x_min, y_min, x_max, y_max) = bounding_box(points)
        end = time.perf_counter()
        print('elapsed time = ' + str(end - start) + ' seconds')

    if do_hull:
        print('convex hull...')
        start = time.perf_counter()
        hull = convex_hull(points)
        end = time.perf_counter()
        print('elapsed time = ' + str(end - start) + ' seconds')

    w = tkinter.Canvas(tkinter.Tk(),
                       width=CANVAS_WIDTH,
                       height=CANVAS_HEIGHT)
    w.pack()

    if do_box:
        w.create_polygon([canvas_x(x_min), canvas_y(y_min),
                          canvas_x(x_min), canvas_y(y_max),
                          canvas_x(x_max), canvas_y(y_max),
                          canvas_x(x_max), canvas_y(y_min)],
                         outline=BOX_OUTLINE_COLOR,
                         fill=BOX_FILL_COLOR,
                         width=OUTLINE_WIDTH)

    if do_hull:
        vertices = []
        for p in clockwise(hull):
            vertices.append(canvas_x(p.x))
            vertices.append(canvas_y(p.y))

        w.create_polygon(vertices,
                         outline=HULL_OUTLINE_COLOR,
                         fill=HULL_FILL_COLOR,
                         width=OUTLINE_WIDTH)

    for p in points:
        w.create_oval(canvas_x(p.x) - POINT_RADIUS,
                      canvas_y(p.y) - POINT_RADIUS,
                      canvas_x(p.x) + POINT_RADIUS,
                      canvas_y(p.y) + POINT_RADIUS,
                      fill=INTERIOR_POINT_COLOR)

    tkinter.mainloop()


###############################################################################
# This main() function runs multiple trials of the algorithms to
# gather empirical performance evidence. You should rewrite it to
# gather the evidence you need.
###############################################################################
def main():
    trial(True, True, 1000)


if __name__ == '__main__':
    main()
