# import basic libarires
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

import warnings
warnings.filterwarnings("ignore")



def stats_1(train):
    '''
    This function run chi2 test to dertermine independence between loan status and loan term
    '''
    # create new df for subgroups for loan with term < 80 mo and > 80 mo
    term_less_80 = train[['term','loan_status']]

    # set column for subgroup that is >= 80 mo term and default
    term_less_80['term_group'] = np.where(term_less_80.term < 80, 'less_80', 'more_80')

    # set observed crosstab for subgropus with less or more than 80 mo term
    observed = pd.crosstab(term_less_80.term_group, term_less_80.loan_status)

    # run chi2 test to compare subgroups
    chi2, p, degf, expected = stats.chi2_contingency(observed)

    print('Observed\n')
    print(observed.values)
    print('---\nExpected\n')
    print(expected)
    print('---\n')
    print(f'chi^2 = {chi2:.4f}')
    print(f'p     = {p:.4f}')
    
    return



def stats_2(train):
    '''
    This functions rusn chi2 test to determine independence between naics and loan status
    '''
    # set observed crosstab for all naic groups and loan status
    observed = pd.crosstab(train.naics, train.loan_status)
    observed.head()


    # run chi2 test to compare subgroups
    chi2, p, degf, expected = stats.chi2_contingency(observed)

    print('Observed\n')
    print(observed.values)
    print('---\nExpected\n')
    print(expected)
    print('---\n')
    print(f'chi^2 = {chi2:.4f}')
    print(f'p     = {p:.4f}')
    
    return



def stats_2a(train):
    '''
    This function runs chi2 test to determine independence between top 3 naic defaulter and loan status
    '''
    
    # create new df subgroup column
    naics_test = train[['loan_status', 'naics']]
    naics_test = naics_test[(naics_test.naics==722110) | (naics_test.naics==722211) | (naics_test.naics==811111)]

    # set observed crosstab for subgrops
    observed = pd.crosstab(naics_test.naics, naics_test.loan_status)


    # run chi2 test to compare subgroups
    chi2, p, degf, expected = stats.chi2_contingency(observed)

    print('Observed\n')
    print(observed.values)
    print('---\nExpected\n')
    print(expected)
    print('---\n')
    print(f'chi^2 = {chi2:.4f}')
    print(f'p     = {p:.4f}')

    return


def stats_3(train):
    '''
    This function runs chi2 test to determine independence between states and loan_status
    '''
    
    # set observed crosstab for states and loan statues
    observed = pd.crosstab(train.state, train.loan_status)

    # run chi2 test to compare groups
    chi2, p, degf, expected = stats.chi2_contingency(observed)

    print('Observed\n')
    print(observed.values)
    print('---\nExpected\n')
    print(expected)
    print('---\n')
    print(f'chi^2 = {chi2:.4f}')
    print(f'p     = {p:.4f}')

    return



def stats_3a(train):
    '''
    This function runs chi2 test to determine independence between top 4 defaulters and loan status
    '''

    # create new df with subgroup column
    state_test = train[['loan_status', 'state']]
    state_test = state_test[(state_test.state == 'FL') | (state_test.state == 'GA') | (state_test.state == 'NV')]

    # set observed crosstab for subgroups
    observed = pd.crosstab(state_test.state, state_test.loan_status)


    # run chi2 test to compare subgroups
    chi2, p, degf, expected = stats.chi2_contingency(observed)

    print('Observed\n')
    print(observed.values)
    print('---\nExpected\n')
    print(expected)
    print('---\n')
    print(f'chi^2 = {chi2:.4f}')
    print(f'p     = {p:.4f}')

    return


def stats_4(train):
    '''
    This function runs chi2 test to determine independence between loan status and employee count <=10 or greater 
    '''
    
    # create new df with subgroup column
    emp_test = train[['loan_status', 'emp_num']]
    emp_test['emp_num_group'] = np.where(emp_test.emp_num <= 10, 'low','high') 

    # set observed crosstab for subgropus with <= 10 employees
    observed = pd.crosstab(emp_test.emp_num_group, emp_test.loan_status)

    # run chi2 test to compare subgroups
    chi2, p, degf, expected = stats.chi2_contingency(observed)

    print('Observed\n')
    print(observed.values)
    print('---\nExpected\n')
    print(expected)
    print('---\n')
    print(f'chi^2 = {chi2:.4f}')
    print(f'p     = {p:.4f}')

    return