# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 11:39:00 2019

This program (python 3.0) ask the user to enter a desired number of clusters, 
followed by reading the input file, 'prog2-input-data.txt' (stored 
in the program folder) parses and load it aslist of float numbers.After that 
it applies k-mean clustering method where it performs following steps:

1. Initialize clusters by picking one point from the list of input 1d numbers 
as centroid. For this assignment, picking the first k points as the initial 
centroids for each corresponding cluster.

2. Loop though each input point and put each one in the cluster whose distance 
from the current centroid is minimum.
3. After all points are assigned, centroids values are re-computed via mean of 
those points assigned to the cluster
4. Store cluster number assignment for later comparasion.
5. Repeat step 2 to 4 for the no. of iteratation until cluster assignment stop 
changing from the last iteration.

Example of an expected input .txt file format:
1.8
4.5
1.1
2.1
9.8
.
.

Expected output for the number of clusters = 2
Input set of single dimensional points = x1,x2,x3,x4
Point x1 in cluster 0
Point x2 in cluster 1 
Point x3 in cluster 1
Point x4 in cluster 1 

"""

"""
This method expects inputs - no. of clusters and list of 1d numbers.
1. Checks clusters size requested should be less than size of input data
2. Apply k-means algo, show final output and saves the output to a 
.txt file.
"""
def kmeansclustering_1d_algo(no_clusters, lst_of_1d_nums):
    if no_clusters > len(lst_of_1d_nums):
        print('Error: Number of clusters requested exceeds the total input data size')
        return

    # Init empty list of all clusters. 
    # First item in the cluster is always cluster's centroid value 
    clusters_of_points = [[] for _ in range(no_clusters)] 
    last_itr_clusters_of_points = [[] for _ in range(no_clusters)]
    
    #1. Pick first no_clusters points from the input list as our initial list of centroids
    for index in range(no_clusters):
        clusters_of_points[index].append(lst_of_1d_nums[index])
        last_itr_clusters_of_points[index].append(lst_of_1d_nums[index])

    iteration = 0
    bstop_iteration = False
    
    while(bstop_iteration == False):            
        #2. Compute the absolute distance of each point from all centroids and assing to the centrod which is closer.
        # First point in each cluster list is always its centroid value
        for point in lst_of_1d_nums:
            dist_from_centroids = [abs(clusters_of_points[cluster_index][0] - point) for cluster_index in range(no_clusters)]
            nearest_centroid_index = dist_from_centroids.index(min(dist_from_centroids))
            clusters_of_points[nearest_centroid_index].append(point)
        
        #Print the current clusters assignments
        print("Iteration {:d}".format(iteration))
        for centroid_index in range(no_clusters):
            print('{:d}'.format(centroid_index),end =" ")
            print(clusters_of_points[centroid_index][1:])
        
        #3 Compare if the old and new clsuter points assignment has changed if yes then carry on for the next iteration otherwise stop        
        for centroid_index in range(no_clusters):
            if len(set(clusters_of_points[centroid_index]).difference(set(last_itr_clusters_of_points[centroid_index]))) == 0:
                bstop_iteration = True
            else:
                bstop_iteration = False

        #4 Copy the current assignment to do the comparasion in the next iteration
        last_itr_clusters_of_points = [[i for i in row] for row in clusters_of_points]        
        
        #5 Re-compute centroid values for the next iteration
        if bstop_iteration == False:
            for cluster in range(no_clusters):                                
                clusters_of_points[cluster][0] = sum(clusters_of_points[cluster][1:])/len(clusters_of_points[cluster][1:])
                clusters_of_points[cluster][1:] = [] # empty cluster for next iteration
                
            
    #6 Print the final output and also save it a file, kMeans_output.txt
    with open('kMeans_output.txt', 'w') as f_handle:
        for point in lst_of_1d_nums:
            found_cluster_index = [cluster_index for cluster_index in range(no_clusters) if point in last_itr_clusters_of_points[cluster_index]]
            if point in last_itr_clusters_of_points[found_cluster_index[0]]:
                strMsg = "Point {:0.2f} in cluster {:d}".format(point, found_cluster_index[0])
                print(strMsg)
                f_handle.write(strMsg)
            f_handle.write('\n')

    
def main():        
    #Ask user for the no. of clusters required
    no_clusters = 0
    bvalid_usr_input = False
    while(bvalid_usr_input == False):
        try:
            usr_input = input("Enter the number of clusters:")
            no_clusters = int(usr_input)            
            bvalid_usr_input = True
        except:
            print("Invalid number of clusters entered... Try again...")
            continue
    
    #Load the input data .txt file
    input_1d_numbers = []
    try:
        with open('prog2-input-data.txt', 'r') as file_handle:
            input_1d_numbers = [float(x.rstrip()) for x in file_handle]
    except ValueError:
            print("Invalid input file. Program exited!")
            return
    #Call k-means clustering method
    kmeansclustering_1d_algo(no_clusters,input_1d_numbers)

if __name__ == '__main__':
    main()


