import random
import math
import matplotlib.pyplot as pl
import copy

def generate_points(seed):
    points = []
    random.seed(seed)

    for _ in range(20):
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

def calculate_distances(centroid, points):
    euclidean_distances = []
    #manhattan_distances = []
 
    for point in points:
        euclidean_distances.append(calculate_euclidean(centroid, point))
        #manhattan_distances.append(calculate_manhattan(centroid, point))

    # print("Euclidean:")
    # for each in euclidean_distances:
    #     print(each)
    # print("Manhattan:")
    # for each in manhattan_distances:
    #     print(each)
    return euclidean_distances

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

def calculate_SSE(points):
    centroid = calculate_centroid(points)
    SSE = 0
    distances = calculate_distances(centroid, points)

    for distance in distances:
        SSE += round((distance)**2, 2)

    return round(SSE, 2)

def select_centroids(points):

    centroid = random.choice(points)
    points.remove(centroid)

    distances = calculate_distances(centroid, points)
    second_centroid = points[distances.index(min(distances))]

    return centroid, second_centroid

def create_clusters(centroids, points):
    cluster_1 = [centroids[0]]
    cluster_2 = [centroids[1]]
    points = list(set(points)-set(centroids))

    for point in points:
        if calculate_euclidean(centroids[0], point) <= calculate_euclidean(centroids[1], point):
            cluster_1.append(point)
        else:
            cluster_2.append(point)
    
    return cluster_1, cluster_2

def split_coordinates(points):
    x_values = []
    y_values = []

    for point in points:
        x_values.append(point[0])
        y_values.append(point[1])
    
    return x_values, y_values

def print_points(clusters):
    count = 0
    marker = ''
    for cluster in clusters:
        x_values, y_values = split_coordinates(cluster)
        if count == 0:
            marker = 'bo'
        elif count == 1:
            marker = 'go'
        elif count == 2:
            marker = 'ro'
        elif count == 3:
            marker = 'ko'
        pl.plot(x_values, y_values, marker)
        count += 1
    
    pl.axis([0.0, 100.0, 0.0, 100.0])
    pl.show()
    
def create_cluster_list(points):
    collected_clusters = []
    SSE_totals = []
    for _ in range(5):
        first_centroid, second_centroid = select_centroids(points)
        centroids = [first_centroid, second_centroid]
        cluster_1, cluster_2 = create_clusters(centroids, points)
        collected_clusters.append([cluster_1, cluster_2])
        SSE_cluster_1 = calculate_SSE(cluster_1)
        SSE_cluster_2 = calculate_SSE(cluster_2)
        SSE_totals.append(SSE_cluster_1+SSE_cluster_2)
        
    index = SSE_totals.index(min(SSE_totals))
    return collected_clusters[index]



seed = 100
point_list = generate_points(seed)
# print("Points:")
# for each in point_list:
#     print(each)

clusters = []
all_sizes = []
k = 2

while len(clusters) != k:
    
    clusters.extend(create_cluster_list(copy.deepcopy(point_list)))
    
    for each in clusters:
            print(each,"\n")

    if len(clusters) != k:
        for each in clusters:
            all_sizes.append(len(each))
        print("Length")
        print(all_sizes)
        point_list = clusters[all_sizes.index(max(all_sizes))]
        print("Next List")
        for each in point_list:
            print(each)
        clusters.remove(point_list)
        all_SSE = []

    

print(clusters)
    

print_points(clusters)