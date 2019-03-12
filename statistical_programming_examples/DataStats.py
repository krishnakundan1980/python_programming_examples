# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 16:29:39 2019

@author: kkrishna
  
NAME: [Kundan Krishna]

(Data Preparations and Statistics)

This program (python 3.0) loads, and parses a .csv file and create some statistics 
after preparing the data. 

"""
import pandas as pd
import re

def main():
    #Load the input file, cps.csv  
    df = pd.read_csv('cps.csv')
    #Generate dataframe which require subset of data columns from loaded input file.
    df_generated = pd.DataFrame({'School_ID': df.School_ID, 'Short_Name': df.Short_Name, 'Is_High_School': df.Is_High_School, 'Zip': df.Zip, \
                         'Student_Count_Total': df.Student_Count_Total, 'College_Enrollment_Rate_School': df.College_Enrollment_Rate_School})
    #Make column, School_ID as index to the newly created dataframe
    df_generated.set_index('School_ID', inplace=True)
    # Parse Grades_Offered_All column data and store into new columns for Lowest Grade and Highest Grade offered in each school
    df_generated["Lowest_Grade_Offered"] = [str(item).split(',')[0] for item in df["Grades_Offered_All"]]
    df_generated["Highest_Grade_Offered"] = [str(item).split(',')[-1] for item in df["Grades_Offered_All"]]
    
    # Prepare School Start hour while parsing Starting_Hours column data 
    df_generated["School_Hours"] = [item for item in df["School_Hours"]]
    #a. Split hour string by am/AM, select the very first part of the splitted string
    df_generated["School_Hours"] = [re.split("am", str(item), flags=re.IGNORECASE)[0] for item in df_generated["School_Hours"]]
    #b. iterate through all characters of the column series data and find digit via using regular expression then store the first found digits
    df_generated["School_Hours"] = [[int(s) for s in re.findall(r'\b\d+\b', item)] for item in df_generated["School_Hours"]]
    #c. column series data from last step is stored as list string i.e. '[',7','3',']'. Pick second one assuming hour string was 7:20 etc.
    df_generated["School_Hours"] = [str(item)[1] for item in df_generated["School_Hours"]]
    #df_generated.to_csv('cps_output4.csv', encoding='utf-8', index=False) Testing
    #d. Convert column series data to numeric value e.g. '7' to 7
    df_series_school_hrs = pd.to_numeric(df_generated["School_Hours"], errors='coerce')
    
    df_generated['College_Enrollment_Rate_School'].fillna(df_generated['College_Enrollment_Rate_School'].mean(), inplace=True)
    #Display top rows of the dataframe as per the assignment instruction
    with pd.option_context('display.max_rows', 10, 'display.max_columns', 8):
        print(df_generated.head(10))  
    
    #Mean and standard deviation of College Enrollment Rate for High Schools as per the assignment instruction
    std = df_generated.loc[df_generated['Is_High_School'] == 1]['College_Enrollment_Rate_School'].std()
    mean = df_generated.loc[df_generated['Is_High_School'] == 1]['College_Enrollment_Rate_School'].mean()
    print("\nCollege Enrollment Rate for high Schools = {:.2f} (sd={:.2f})".format(mean,std))
    
    #Mean and standard deviation of Student_Count_Total for non-High Schools as per the assignment instruction
    std_nonhigh = df_generated.loc[df_generated['Is_High_School'] == 0]['Student_Count_Total'].std()
    mean_nonhigh = df_generated.loc[df_generated['Is_High_School'] == 0]['Student_Count_Total'].mean()
    print("\nTotal student count for non-High Schools = {:.2f} (sd={:.2f})".format(mean_nonhigh,std_nonhigh))
    
    #Distribution of starting hours for all schools
    print("\nDistribution of Starting Hours")
    distr_of_school_hrs = df_series_school_hrs.value_counts()
    for index, value in distr_of_school_hrs.iteritems():
        print("{:d}am{:s} {:d}".format(int(index),':',value))
    
    school_loop_zip = [60601, 60602, 60603, 60604, 60605, 60606, 60607, 60616]
    school_count_outof_loop = len([item for item in df["Zip"] if item not in school_loop_zip])
    print("\nNumber of schools outside the Loop: {:d}".format(school_count_outof_loop))
        
if __name__ == '__main__':
    main()