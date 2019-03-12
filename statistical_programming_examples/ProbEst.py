# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 13:25:38 2019

@author: kkrishna
  
NAME: [Kundan Krishna]

This program (python 3.0) loads  a cars.csv file using pandas lib. Then it
implements an algorithm for computing probablity of each aspiration for every 
make type. It also computes probablity of each make from total makes present in
the csv file.

"""

import pandas as pd

def main():
    #Load cars input csv file
    cars_df = pd.read_csv('cars.csv')
    #Get distinct cars make and aspiration list
    makes = cars_df['make'].unique().tolist()
    aspirations = cars_df['aspiration'].unique().tolist()
    
    for make in makes:
        make_asp_series = cars_df['aspiration'][cars_df['make'] == make]
        for aspiration in aspirations:
            # iterate through aspiration column data for the matching asp type and count the total match found
            make_each_asp_count = len([item for item in make_asp_series if item == aspiration])
            #total matching make found from the make column data
            make_total = len(cars_df.loc[cars_df['make'].isin([make])]) 
            print("Prob(aspiration={:s}|make={:s}) = {:.2f}%".format(aspiration,make,100*make_each_asp_count/make_total))
    
    print('\n')
    
    for make in makes:
        #Find aspiration total count for the matching make type
        make_asp_series = cars_df['aspiration'][cars_df['make'] == make]
        print("Prob(make={:s}) = {:.2f}%".format(make,100*len(make_asp_series)/len(cars_df['make'])))

        
if __name__ == '__main__':
    main()