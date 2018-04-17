import random
import math
import matplotlib.pyplot as pl

def generate_points(seed):
    points = []
    random.seed(seed)

    for _ in range(10):
        x = round(random.uniform(1.0, 100.0), 2)
        y = round(random.uniform(1.0, 100.0), 2)

        points.append((x,y))
    
    return points

def calculate_euclidean(centroid, point):
    distance = round(math.sqrt(((centroid[0]-point[0])**2)+((centroid[1]-point[1])**2)), 2)
    return distance

def calculate_manhattan(centroid, point):
    distance = round(abs(centroid[0]-point[0]) + abs(centroid[1]-point[1]), 2)
    return distance

def calculate_distances(centroids, points):
    euclidean_distances = []
    manhattan_distances = []

    for centroid in centroids:
        for point in points:
            euclidean_distances.append(calculate_euclidean(centroid, point))
            manhattan_distances.append(calculate_manhattan(centroid, point))

    print("Euclidean:")
    for each in euclidean_distances:
        print(each)
    print("Manhattan:")
    for each in manhattan_distances:
        print(each)

def calculate_centroid(points):
    sum_of_x = 0.0
    sum_of_y = 0.0
    x_coor = 0.0
    y_coor = 0.0


    for point in points:
        sum_of_x += point[0]
        sum_of_y += point[1]

    x_coor = round((1/len(points))*sum_of_x, 2)
    y_coor = round((1/len(points))*sum_of_y, 2)
    centroid = (x_coor, y_coor)

    return centroid

def print_points(points):
    x_values = []
    y_values = []

    for point in points:
        x_values.append(point[0])
        y_values.append(point[1])
    
    pl.plot(x_values, y_values, 'bo')
    pl.axis([0.0, 100.0, 0.0, 100.0])
    pl.show()
    

seed = 50
point_list = generate_points(seed)
print("Points:")
for each in point_list:
    print(each)
print("Centroids:")
centroids = [calculate_centroid(point_list)]
for each in centroids:
    print(each)
calculate_distances(centroids, point_list)

print_points(point_list)