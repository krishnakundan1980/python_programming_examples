# -*- coding: utf-8 -*-
"""
Created on Fri Feb 2 11:39:00 2019
  
NAME: [Kundan Krishna]

Nearest Neighbor Classification)

This program (python 3.0) loads, reads and parses the two .csv files. File, 
iris-training-data.csv carries training dataset while iris-training-data.csv 
test dataset. First 4 columns from each file acts as Iris flower's attributes, 
also called feature vector. Last column stores Iris type it belongs to, also 
called class label.

Nearest Neighbor Classification algorithm find distances of each test dataset 
instance from all training instances. Then it assigns the label of the training 
instance for which distance is the minimum.

"""
import numpy as np

def train_and_predict(training_x,testing_x):
    #Add extra axis to the training and test dataset so it can exploit the numpy 
    #broadcasting feature which can result into a 3d matrix (4X75X75) where each column 
    #represents feature vector of a test instance stacked for every training instances
    training_x = training_x[:,:,np.newaxis]#4X75X1
    testing_x = testing_x[:, np.newaxis, :]#4X1X75
    #Using numpy broadcasting functionalties with substraction operation 
    feature_vect_diff = training_x-testing_x#4X75X75
    #Sqaure the feature_vect_diff as per distance formula given in the exercise
    feature_vect_diff_square = np.square(feature_vect_diff)
    #Sum from feature vector axis wise i.e. axis = 0, required as per formula given in the exercise
    distance_vector = np.sqrt(np.sum(feature_vect_diff_square,axis=0))#75X75
    #Find the index of distance vector which has minimum distance value. This will 
    #determine the test instance label class prediction matching to which 
    #training instance label class
    test_prediction_indices = np.argmin(distance_vector,axis=0)#75X75
    return test_prediction_indices

def main():
          
    #Load training and test samples using input xls files
    training_x = np.loadtxt ('iris-training-data.csv',
                unpack = True,
                usecols = (0,1,2,3),
                delimiter = ',')
    training_y = np.loadtxt ('iris-training-data.csv',
                unpack = True,
                usecols = (4),
                delimiter = ',',
                dtype=np.str)
    
    testing_x = np.loadtxt ('iris-testing-data.csv',
            unpack = True,
            usecols = (0,1,2,3),
            delimiter = ',')
    testing_y = np.loadtxt ('iris-testing-data.csv',
            unpack = True,
            usecols = (4),
            delimiter = ',',
            dtype=np.str)
    
    prediction_index = train_and_predict(training_x,testing_x)
    
    test_prediction_classes =  [training_y[prediction_index[index]] for index in range(prediction_index.shape[0])]  
    
    #Print test instance no., its true Iris known class label and algorithm predicted class label
    print("# ,True, Prediction")
    for test_index in range(testing_y.shape[0]):
        print('{:d},{:s},{:s}'.format(test_index+1, str(testing_y[test_index]), str(test_prediction_classes[test_index])))
        
    accuracy = np.sum(test_prediction_classes == testing_y)
    print("Accuracy: {:.2f}".format(100*accuracy/len(testing_y)))
        
if __name__ == '__main__':
    main()