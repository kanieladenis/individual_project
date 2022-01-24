# import basic libarires
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

def lowercase_rename(df):
    '''
    This function makes lowercase and renames columns for better
    readability
    '''
    # lowercase columns names
    df.columns = df.columns.str.lower()

    # rename columns
    df = df.rename(columns = {'loannr_chkdgt': 'loan_id',
     'bankstate':'bank_state',
     'approvaldate':'appv_date',
     'approvalfy': 'appv_fy',
        'noemp':'emp_num',
     'newexist': 'new_existing',
     'createjob': 'jobs_created',
     'retainedjob': 'jobs_retained',
     'franchisecode': 'franchise_code',
     'urbanrural': 'urban_rural',
     'revlinecr': 'rev_credit',
     'lowdoc': 'low_doc',
     'chgoffdate': 'default_date' ,
     'disbursementdate': 'disbursement_date',
     'disbursementgross': 'disbursement_gross',
     'balancegross': 'outstanding_gross',
     'mis_status': 'loan_status',
     'chgoffpringr': 'default_amount',
     'grappv': 'appv_loan_amount',
     'sba_appv': 'sba_appv_amount'})
      
    return df


def remove_nulls(df):
    '''
    This function remove nulls by dropping the defaul_date column which conatined majority of the columns, and
    then drops the rest of nulls.
    '''
    # drop column default_date
    df = df.drop(columns='default_date')

    # drop the rest of the nulls
    df = df.dropna()

    return df


def data_adjust(df):
    '''
    This function remove string $ and , from the columns of money. This is for scaling and modeling later.
    It removes A from 1976. Changes dtypes to datetime or float. Changes loan_status to paid or default for
    readability. It removes outliers for disbursement_date and appv_date.
    '''
    
    # select columns to change
    cols = ['disbursement_gross','outstanding_gross','default_amount','appv_loan_amount','sba_appv_amount']

    # remove $ and , from money columns
    for col in cols:
        df[col] = df[col].str.replace('$','').str.replace(',','_')

        # replace 1976A to 1976 to enable datetime converstion
    df.appv_fy = df.appv_fy.replace({'1976A':'1976'})

    # change dtypes for date columns and money columns
    df = df.astype({'appv_date':'datetime64',
              'appv_fy':'datetime64',
              'disbursement_date':'datetime64',
              'disbursement_gross': float,
              'outstanding_gross': float,
               'default_amount': float,
               'appv_loan_amount': float,
               'sba_appv_amount': float})
    
    # change loan_status values from PIF to paid and CHGOFF to default for readability
    df.loan_status = df.loan_status.map({'P I F':'paid','CHGOFF':'default'})

    # remove outlier from column disbursement_date for better analysis
    df = df[df.disbursement_date < '2020']

    # remove outlier from column appv_date for better analysis
    df = df[df.appv_date < '2020']

    return df


def column_adjust(df):
    '''
    This function drops the oustand_gross column because it's mosttly zero and
    it create is_new columns that indicated new businesses
    '''

    # drop column oustanding_gross since most are zero
    df = df.drop(columns='outstanding_gross')

    # create new column is_new where new is is assigned as 1 and everthing else is 0
    df['is_new'] = np.where(df.new_existing==2, 1, 0)

    return df


def remove_outliers(df):
    '''
    The function removes from identified columns outliers that are above the third quartile and below
    the first quartile by double the IQR 
    '''

    # Create list of continous columns to investigate/viz
    cols = ['emp_num',
            'jobs_created',
            'jobs_retained',
            'disbursement_gross',
            'appv_loan_amount',
            'sba_appv_amount',
            'term'
           ]

    # remove outliers from each column in cols_list
    for col in cols:

        q1, q3 = df[col].quantile([.25, .75])  # get quartiles

        iqr = q3 - q1   # calculate interquartile range

        upper_bound = q3 + 2 * iqr   # get upper bound
        lower_bound = q1 - 2 * iqr   # get lower bound

        # return dataframe without outliers

        df = df[(df[col] > lower_bound) & (df[col] < upper_bound)]

    return df


def feature_engineering(df):
    '''
    This function creates new columns from existing columns. It creates sba_percent: the percentage of the approved
    by SBA. Monthly Debt is the Approved Loan divided by the number of months in ther term. The jobs counts is the 
    sum of the created jobs and the retained jobs. is_default identifies the loans that defaulted.
    '''
    
    # add ratio column for sba approved amount over bank approved amount
    df['sba_percent'] = df.sba_appv_amount / df.appv_loan_amount

    # add ratio column for appv_loan_amount by term 'monthly_debt'
    df['monthly_debt'] = round((df.appv_loan_amount / df.term), 2)

    # create column for jobs count by adding job created and jobs retained
    df['jobs_count'] = (df.jobs_created + df.jobs_retained)

    # created columns for modeling
    df['is_default'] = df.loan_status.map({'default':1, 'paid':0})

    return df


def wrangle(df):
    '''
    This function funs all prepare fuctions
    '''
    
    df = lowercase_rename(df)
    
    df = remove_nulls(df)
    
    df = data_adjust(df)
    
    df = column_adjust(df)
    
    df = remove_outliers(df)
    
    df = feature_engineering(df)
    
    return df
    
    
    
    
    
    

    
    


