import random
import math

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


seed = 50
point_list = generate_points(seed)
print(point_list)
centroids = [(50.0, 50.0)]
calculate_distances(centroids, point_list)