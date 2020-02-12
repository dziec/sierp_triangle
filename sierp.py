import matplotlib.pyplot as plt
import numpy as np
import random as rd

# length of stretch
def vec_len(A, B):
    z = np.sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2)
    return z

# point in half way between two other points
def vec_mid(A, B):
    Ps = [0, 0]
    Ps[0] = (A[0] - B[0]) / 2
    Ps[1] = (A[1] - B[1]) / 2
    return(Ps)

# random triangle vertex
def random_vertex(triangle):
    x_rand = rd.random() * 9
    if 0 <= x_rand < 3:
        base_point = triangle[0]
    elif 3 <= x_rand < 6:
        base_point = triangle[1]
    else:
        base_point = triangle[2]
    return(base_point)


# random point in defined triangle:
def point_on_triangle(triangle):
    pt1, pt2, pt3 = triangle[0], triangle[1], triangle[2]
    s, t = sorted([rd.random(), rd.random()])
    xs = s * pt1[0] + (s-t)*pt2[0] + (1-t)*pt3[0]
    ys = s * pt1[1] + (s-t)*pt2[1] + (1-t)*pt3[1]
    return (xs, ys)


# def draw_a_sierp(triangle, iter):
#     point = vec_mid(random_vertex(triangle), point_on_triangle(triangle))
#     # plt.scatter(point[0], point[1])
#     for i in range(0, iter):
#         point = vec_mid(point, random_vertex(triangle))
#         plt.scatter(point[0], point[1], s=0.1)
#     return()


def draw_a_sierp(triangle, iter, start_point):
    point = start_point
    for i in range(0, iter):
        point = vec_mid(point, random_vertex(triangle))
    return(point)


triangle = ((0, 0), (5, 5), (10, 0))
start_point = vec_mid(random_vertex(triangle), point_on_triangle(triangle))
iter = 10

# pt1 = (1, 1)
# pt2 = (2, 4)
# pt3 = (5, 2)
points = [draw_a_sierp(triangle, iter, start_point) for _ in range(10000)]
x, y = zip(*points)
plt.scatter(x, y, s=0.1)
plt.show()


A = [-1, -2]
B = [0, 0]
# print(random_point(triangle))
# print(vec_mid(A, B))
