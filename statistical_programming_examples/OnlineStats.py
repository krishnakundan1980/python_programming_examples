# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 11:39:00 2019
  
This program (python 3.0) ask the user to enter a nonnegative number, then 
computes the mean and variance using the online update formulas mentioned in 
the assignment #1. The output is displayed on the console. The program will 
terminate if user input a negative number.

"""
import numpy as np

def main():
    # Init the current mean, varinace and number of values to be entered by the 
    #user to zero.
    current_mean = 0.0
    current_variance = 0.0
    n = 0

    user_input_number = 0
    print("Mean is  {:f}, Variance is {:f}".format(current_mean,current_variance))
    print("(Note: To exit the program, enter a negative number...)")
    
    while(user_input_number != -1): # Loop terminate condition of negative number       
        try:
            user_input_number = input("Enter a number: ")
            #Type cast to float to ensure that user has entered only non-negative number
            user_input_number = float(user_input_number)
        except ValueError:
            continue
       
        if user_input_number < 0:
            print("Program exited!")
            break;
        
        n = n + 1
        old_mean = current_mean # Store for variance computation
        current_mean = current_mean + (user_input_number - current_mean)/n
       
        if n > 1:
            current_variance = np.multiply(((n-2)/(n-1)), current_variance) + np.square(user_input_number - old_mean)/n     
        print("Mean is  {:f} Variance is {:f}".format(current_mean,current_variance))

if __name__ == "__main__":
    main()
    