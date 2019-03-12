# -*- coding: utf-8 -*-
"""
Created on Wed March 6 14:54:20 2019

@author: kkrishna
  
NAME: [Kundan Krishna]

This program (python 3.0) loads, and parses a .csv file and create 3 statistical
tables.

"""
import pandas as pd
import numpy as np

def main():
         
    #Load ss13hil.csv datasource file
    ss13hil_df = pd.read_csv('ss13hil.csv')
    
    #TABLE 1: Statistics of HINCP - Household income (past 12 months), grouped by HHT - Household/family type
    print("*** TABLE 1: Descriptive Statistics of HINCP, grouped by HHT ***")
    #Create list of HHT (Household/family type) description
    hht_discr = ["Married couple household", \
                "Other family household:Male householder, no wife present", \
                "Other family household:Female householder, no husband present", \
                "Nonfamily household:Male householder:Living alone", \
                "Nonfamily household:Male householder:Not living alone", \
                "Nonfamily household:Female householder:Living alone", \
                "Nonfamily household:Female householder:Not living alone"
                ]
    
    hincp_grp_by_hht_df = ss13hil_df.dropna(subset=['HINCP', 'HHT'], inplace=True)
    hincp_grp_by_hht_df = ss13hil_df["HINCP"].groupby(ss13hil_df['HHT'])
    stat_hincp_grp_by_hht_df = hincp_grp_by_hht_df.describe()
    #Re-index by HHT description
    stat_hincp_grp_by_hht_df.index.name = "HHL - Household/family type"
    stat_hincp_grp_by_hht_df.index = stat_hincp_grp_by_hht_df.index.map(str)
    stat_hincp_grp_by_hht_df.index.values[0] = hht_discr[0]
    stat_hincp_grp_by_hht_df.index.values[1] = hht_discr[1]
    stat_hincp_grp_by_hht_df.index.values[2] = hht_discr[2]
    stat_hincp_grp_by_hht_df.index.values[3] = hht_discr[3]
    stat_hincp_grp_by_hht_df.index.values[4] = hht_discr[4]
    stat_hincp_grp_by_hht_df.index.values[5] = hht_discr[5]
    stat_hincp_grp_by_hht_df.index.values[6] = hht_discr[6]
    #Sort by mean value in descending order
    stat_hincp_grp_by_hht_df.sort_values('mean', ascending=False, inplace=True)
    #Print only mean, std, count, min and max
    with pd.option_context('display.max_rows', 10, 'display.max_columns', 10):
        print((stat_hincp_grp_by_hht_df[['mean','std','count','min','max']]))
        print("\n")


    #TABLE 2: HHL - Household language vs. ACCESS - Access to the Internet (Frequency Table)
    print("*** TABLE 2 - HHL vs. ACCESS -  Frequency Table ***")
    hhl_descr = ["English only","Spanish","Other Indo-European languages",\
                 "Asian and Pacific Island languages","Other language"]
    
    access_descr = ["Yes, w/ subscr.",\
                    "Yes, w/o a subscr.",\
                    "No"]
    
    ss13hil_df.dropna(subset=['HHL', 'WGTP', 'ACCESS'], inplace=True)
    wgtp_grpby_hhl_and_access = (100*ss13hil_df['WGTP'].groupby([ss13hil_df['HHL'],ss13hil_df['ACCESS']]).sum().unstack()/ss13hil_df['WGTP'].sum())
    wgtp_grpby_hhl_and_access.index.name = "HHL - Household language"
    wgtp_grpby_hhl_and_access.index = wgtp_grpby_hhl_and_access.index.map(str)
    wgtp_grpby_hhl_and_access.index.values[0] = hhl_descr[0]
    wgtp_grpby_hhl_and_access.index.values[1] = hhl_descr[1]
    wgtp_grpby_hhl_and_access.index.values[2] = hhl_descr[2]
    wgtp_grpby_hhl_and_access.index.values[3] = hhl_descr[3]
    wgtp_grpby_hhl_and_access.index.values[4] = hhl_descr[4]
    
    wgtp_grpby_hhl_and_access.columns = access_descr
    
    wgtp_grpby_hhl_and_access['All'] = (wgtp_grpby_hhl_and_access.sum(axis=1))
    wgtp_grpby_hhl_and_access.loc['All', :] = wgtp_grpby_hhl_and_access.sum(axis=0).values
    wgtp_grpby_hhl_and_access = wgtp_grpby_hhl_and_access.round(2)
    wgtp_grpby_hhl_and_access = wgtp_grpby_hhl_and_access.astype(str) + '%'
    with pd.option_context('display.max_rows', 10, 'display.max_columns', 10):
        print(wgtp_grpby_hhl_and_access.head(10))
        print("\n")
    
    
    #TABLE 3: Quantile Analysis of HINCP - Household income (past 12 months)
    print("*** TABLE 3: Quantile Analysis of HINCP - Household income (past 12 months) ***")
    quantile_bucket = pd.qcut(ss13hil_df['HINCP'], 3,labels=["low", "medium", "high"])
    grouped_by_quantile_bucket = ss13hil_df['HINCP'].groupby(quantile_bucket)
    headcount_by_quantile_bucket = ss13hil_df['WGTP'].groupby(quantile_bucket).sum()
    combined_table = grouped_by_quantile_bucket.describe()[['min','max','mean']].join(headcount_by_quantile_bucket)
    combined_table.rename(columns={"WGTP": "household_count"},inplace=True)
    with pd.option_context('display.max_rows', 10, 'display.max_columns', 10):
        print(combined_table.head(10))


if __name__ == "__main__":
    main()
