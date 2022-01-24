# import needed libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import warnings
warnings.filterwarnings("ignore")





def explore_1(train):
    '''
    This function creates a dataframe of loan_status by count and builds a bar plot of loan status
    '''
    # create dataframe that groups by loan_status and counts each row
    loan_status = pd.DataFrame(train.groupby('loan_status').loan_id.count()).reset_index().rename(columns={'loan_id':'loan_count'})
    
    # plot loan count by loan status
    plt.figure(figsize=(15,5))
    sns.barplot(data=loan_status, x='loan_status', y='loan_count')
    plt.title('There are less Defaulted Loans than Paid Off?')
    plt.xlabel('Loan Count')
    plt.ylabel('Loan Status')
    plt.show()

    return


def explore_2(train):
    '''
    This function plots loan amount loan term and hue  by loan status
    '''
    # Plot loan amount by term hue by loan status
    plt.figure(figsize=(15,5))
    sns.scatterplot(data=train, x='term', y='appv_loan_amount', hue='loan_status')
    plt.axvline(x=80, color='black')
    plt.title('Loans with Less Than 80 Months Term Have Higher Risk of Default?')
    plt.xlabel('Loan Term in Months')
    plt.ylabel('Approved Loan Amount')
    plt.show()

    return


def explore_3(train):
    '''
    This function plots loan disbursement date by loan disbursement gross and hue by loan status to see defaults overtime
    '''
    
    # Plot Loan Disbursement Date by Disburment Gross hue by Loan Status
    plt.figure(figsize=(15,5))
    sns.scatterplot(data=train, x='disbursement_date', y='disbursement_gross', hue='loan_status')
    plt.title('Defaulted Loans Align with Economic Recession')
    plt.xlabel('Disbursement Date')
    plt.ylabel('Disbursement Amount')
    plt.show()

    return


def explore_3a(train):
    '''
    This function plots loan approval date and loan disbursement gross and hue by loan status to see defaults overtime
    '''
    
    # Plot Loan Approval Date by Loan Disbrursement Gross hue by Loan Status
    plt.figure(figsize=(15,5))
    sns.scatterplot(data=train, x='appv_date', y='disbursement_gross', hue='loan_status')
    plt.title('Loans Overtime by Status')
    plt.xlabel('Loan Approval Date')
    plt.ylabel('Loaon Disbursement Gross')
    plt.show()

    return

def explore_3b(train):
    '''
    This function plots loan approval date by loan disbursement gross and hues by loan status for loans after 1990.
    To see defaults  overtime but zoomed in to avoid all the defautls from 1990 and before
    '''
    
    # Plot Defaults with Loan Approval Data and Loan Disbursement Gross for loan approved after 1990
    defaults_1990 = train[train.appv_date >= '1990']
    plt.figure(figsize=(15,5))
    sns.scatterplot(data=defaults_1990, x='appv_date', y='disbursement_gross', hue='loan_status')
    plt.title('Default Timeline Aligns with Economic Recession')
    plt.xlabel('Loan Approval Date')
    plt.ylabel('Loan Disbursement Gross')
    plt.show()

    return



def explore_4(train):
    '''
    This function creates a dataframe by groping by naics and loan status to determine loan status counts.
    It plots the default counts by naics in a bar graph.
    '''
    
    # create dataframe that groups by naics and loan status then counts each loan
    naics_df = pd.DataFrame(train.groupby(['naics','loan_status']).loan_id.count()).reset_index().rename(columns={'loan_id':'loan_count'})

    # filter dataframe to remove naics 0 and include counts > 500
    naics_df = naics_df[(naics_df.naics > 0) & (naics_df.loan_count > 500) & (naics_df.loan_status == 'default')]

    # plot default count by naics and mark average horizonal line
    plt.figure(figsize=(15,5))
    sns.barplot(data=naics_df, x='naics', y='loan_count', hue='loan_status')
    plt.axhline(y=naics_df.loan_count.mean(), color='black', label='Avg Count')
    plt.title('Restaurants and General Automotive Have Most Defaults')
    plt.ylabel('Default Count')
    plt.xlabel('NAICS Code')
    plt.show()

    return



def explore_5(train):
    '''
    This function builds a dataframe that groups all by states and counts defaults.
    It plots the default count by state
    '''
    
    # plot default count by state
    default_df = train[train.loan_status=='default']
    default_state = pd.DataFrame(default_df.groupby('state').loan_status.count()).reset_index().rename(columns={'loan_status':'default_count'}).sort_values('default_count', ascending=False)

    # plot defaults by state with an average horizontal line
    plt.figure(figsize=(15,5))
    sns.barplot(data=default_state, x='state', y='default_count')
    plt.axhline(y=default_state.default_count.mean(), color='black', label='Avg Count')
    plt.title('Default Counts by State')
    plt.ylabel('Default Counts')
    plt.xlabel('State')
    plt.show()

    return



def explore_5a(train):
    '''
    This function builds a dataframe of loans with disbursement date greater than 1990 and then 
    groupby states and counts defaults
    '''
    
    # create df for disbursement date > 1990
    train_1990 = train[train.disbursement_date > '1990']
    train_1990 = pd.DataFrame(train_1990.groupby('state').loan_status.count()).reset_index().rename(columns={'loan_status':'default_count'}).sort_values('default_count', ascending=False)

    # plot defaults by state for loans approved after 1990
    plt.figure(figsize=(15,5))
    sns.barplot(data=train_1990, x='state', y='default_count')
    plt.axhline(y=train_1990.default_count.mean(), color='black', label='Avg Count')
    plt.title('Default Counts by State for Loans approved after 1990')
    plt.ylabel('Default Counts')
    plt.xlabel('State')
    plt.show()

    return



def explore_5b(train):
    '''
    This function builds a dataframe that groups by state, sums the defaults, and then claculates the 
    percentage of defaults (defaulted loans / total loans) for each state
    '''
    
    # create df for defaults pecentage by state
    default_state_percent = pd.DataFrame(train.groupby('state').is_default.sum()).reset_index()
    default_state_percent['total'] = train.groupby('state').is_default.count().values
    default_state_percent['percent'] = round((default_state_percent.is_default / default_state_percent.total) * 100, 2)
    default_state_percent = default_state_percent.sort_values('percent', ascending=False)

    # plot defaults by state for loans approved after 1990
    plt.figure(figsize=(15,5))
    sns.barplot(data=default_state_percent, x='state', y='percent')
    plt.axhline(y=default_state_percent.percent.mean(), color='black', label='Avg Percent')
    plt.title('Default Percents by State')
    plt.ylabel('Default Percents')
    plt.xlabel('State')
    plt.show()

    return



def explore_6(train):
    '''
    This function plots employee number by jobs count and hue by loan status.
    '''
    
    # plot default count by state
    default_df = train[train.loan_status=='default']

    # plot defaults by emp_num and jobs_count
    plt.figure(figsize=(15,5))
    sns.scatterplot(data=default_df, x='emp_num', y='jobs_count', hue='loan_status')
    plt.title('Loans with Less than 10 Employees have Higher Risk of Default')
    plt.ylabel('Jobs Count')
    plt.xlabel('Employee Number')
    plt.show()

    return



def explore_7(train):
    '''
    this fuctiop plots monthly debt by sba percent to see if either variable is aligned with defaults
    '''
    
    # plot defaults for monthly debt by sba_percent
    plt.figure(figsize=(15,5))
    sns.scatterplot(data=train, x='sba_percent', y='monthly_debt', hue='loan_status')
    plt.axhline(y=5000, color='black')
    plt.title('Loans with Higher Monthly Debt have Higher Risk of Default')
    plt.ylabel('Monthly Debt')
    plt.xlabel('SBA Covered Percent')
    plt.show()

    return


def explore_7a(train):
    '''
    This function adjusts train to include only rows with monthly debut < 5000, and then plots monthly debt by sba percen
    and hues by loan status in order to see if either variable align with defautls
    '''
    
    # plot SBA covered percentage by monthluy debt for monthly debt < 10,000 andh hue for loan status
    mo_debt_10k = train[train.monthly_debt < 5000]

    plt.figure(figsize=(15,5))
    sns.scatterplot(data=mo_debt_10k, x='sba_percent', y='monthly_debt', hue='loan_status')
    plt.title('Loans with More than $4K Monthly Debt have Higher Risk of Default')
    plt.ylabel('Monthly Debt')
    plt.xlabel('SBA Covered Percent')
    plt.show()

    return



