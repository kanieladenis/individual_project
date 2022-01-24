# Individual Project - Predicting SBA Loan Defaults

## About the Project 

### Project Goals
- Using classifcation models, discover drivers of SBA gauranteed loans that predict if that loan will default

### Project Description

- Loans are keys to making dreams come true from buying a house to starting a business. Small business loans come with high risk and it is the goal of this project to create a classification model that can predict if a loan will default.
- Referenced from Kaggle: https://www.kaggle.com/mirbektoktogaraev/should-this-loan-be-approved-or-denied
- References from Journal of Statistics Education https://www.tandfonline.com/doi/full/10.1080/10691898.2018.1434342 

### Initial Questions

- Are there more defaulted loans?
- What term lengths are common for defaulted loans?
- What is the timeline of default loans vs non-default loans
- In what industries do loan defaults occur most?
- In what locations do loan defaults occur most 

### Data Dictionary

Provided in Repo

### Steps to Reproduce

1. Clone repo
2. No credentials required
3. Follow notebook


## The Plan

### Plan
- Pick Data Set
    - Kaggle ***
    - Data.gov
    - Data.worldbank.org
    - census.gov
- Define Target
    - is_default
    
### Acquire
- Pull from Kaggle
- Clean

### Prepare
- Clean
- Remove Nulls
- Remove Outliers
- Remove Useless (keep simple)
- Rename for Readability
- Keep Simple

### Explore
- Find Drivers 
- Need 4 Visuals
- Need 3 Stats Tests
- Attemp 3 Cluster Combos
- Charts:
    - Status His()
    - Scatterplot default locatoins overlay on map
    - Timeline of default dates
    - Timeline of approve dates
    - Timeline of US GDP
    - Scatterplot of NAICS hue by default
- Columns to Start Explore:
    - is_default
    - appv_loan_amount
    - sba_appv_amount
    - new_exist
    - naics
    - no_emp

### Model
- Use classification
- Need 3 Models + Baseline
    - Decision Tree
    - Random Forest
    - K_Nearest Neighbor
    - Evaluate and Choos best Model for Test Data
- What the accuracy rates?
- Visual of Model Predictions vs Actual

### Deliver
- Conclusion:
    - Were the goals reached
- Repo with Final Report, Woring Notebook, Modules, Readme
    - link to presentation video if time allows

## Prepare

##### Modules (prepare.py)

- acquire not needed since csv was downloaded from kaggle
- write code to lower_case and lower-case columns for readability, combine to function and test, then add to prepare.py
- write code to remove nulls, combine to function, test, and then add to prepare.py
- write code to remove $ and , from string in order to change column dtupe to foat, combine to function, test, then add to prepare.py
- write code to change date columns to datetime, add to function, test, add to prepare.py
- write code to change loan_status column values to default or paid
- wte code to remove outliers, add to function, test, then add to prepare.py
- write code for feature engineering, add to function, test, than added to prepare.py
- write function that acculates all prepare functions, add to prepare.py, test

##### Missing Values (report.ipynb)

- removed default-date since most were nulls
- dropped all other nulls since counts were relatively small, less than 15K total

##### Data Split (prepare.py (def function), report.ipynb (run function))

- Used function splits data into the train, validate, and test set at portions: 56%, 24%, 20%, stratify on is_default 

##### Using your modules (report.ipynb)

- import and test each function in the report for better troublshooting. Run all function withour error.


#### Explore

##### Ask a clear question, [discover], provide a clear answer (report.ipynb)

- Question 1: Are There More Defaulted Loans Than Paid Loans?
- Question 2: What Term Lengths Are Common with Defaulted Loans?
- Question 3: What is the Timeline for Default Loans?
- Question 4: In What Industries do Loan Defaults Occur Most?
- Question 5: In What States do Loan Defaults Occur Most by Percentage of Total Loans?
- Question 6: Are There More Defaults for Businesses with Less Employees and Less Jobs?
- Question 7: Are There More Defaults with Higher Monthly Debt and/or Lower SBA Coverage Percent?s? 


##### Exploring through visualizations (report.ipynb)

- Question 1: Are There More Defaulted Loans Than Paid Loans?
    - barplot with a count of loans that were default or paid 
- Question 2: What Term Lengths Are Common with Defaulted Loans?
    - scatterplot with x=term length, y=approved amount, hue by status
- Question 3: What is the Timeline for Default Loans?
    - scatterplot with x=date loan approved, y=loan amount, hue by status
- Question 4: In What Industries do Loan Defaults Occur Most?
    - barplot wit x = naics, y=default count per naics
- Question 5: In What States do Loan Defaults Occur Most by Percentage of Total Loans?
    - barplot with x = state, y = percentage of defaults to total loans per state
- Question 6: Are There More Defaults for Businesses with Less Employees and Less Jobs?
    - scatterplot with x = employ nummber and y = jobs count, hue by loan status
- Question 7: Are There More Defaults with Higher Monthly Debt and/or Lower SBA Coverage Percent?
    - scatterplot with x = SBA Coverage Percent and y = Monthly Debt, hue by loan status

##### Statistical tests (report.ipynb)

- Chi2 Test to determine if Loan Term and Loan Status are Independent of each other
- Chi2 test to determine if NAICS and Loan Status are Independent of each other
- Chi2 test to determin if State and Loan Status are Independent of each other
- Chi2 test to determine if Employee number and loan status are Indendent of each other

##### Summary (report.ipynb)

Identified the following features as drivers of default loans
- Term: 80 months or less
- NAICS: Restaurant and General Automotive
- State: Half the states but top 3 are Florida, Georgia, Nevada
- Employee Number: 10 or less
- Monthly Debt: $5,000 or more

#### Modeling

##### Select Evaluation Metric (Report.ipynb)

- Evaluating classificatoin models on accuracy

##### Evaluate Baseline (Report.ipynb)

- Most frequent value is paid and baseline is at 78% 

##### Develop 3 Models (Report.ipynb)

- Developed 3 models each with a different alogrythm: Decisin Tree, Random Forest, K_nearest neighbor

#### Evaluate on Train (Report.ipynb)

All models evaluated on Train with K-nearest neighbor doing the best

##### Evaluate on Validate (Report.ipynb)
 
All models evalutes on Validate, no model was under/over fit

##### Evaluate Top Model on Test (Report.ipynb)

- K-Nearest Neighbor was top model and performed consistent on Test

## Report (Final Notebook) 

#### code commenting (Report.ipynb)

- code comments were made

#### markdown (Report.ipynb)

- mark down was msade

#### Written Conclusion Summary (Report.ipynb)

The goals of this project was to discover drivers of default for SBA back loans and to build a classfication model that will predict if a loan will default.
The goals were reached. I identifed 5 drivers via exploration that indicated increased risk of default. Those drivers are:
1. Loans with a term of less than 80 months.
2. Loans in the restaurant and general automotive business
3. Loans for businesses in 24 states have higher risk of default. The top 3 states are FL, GA, NV
4. Loans for businesses that have fewer than 10 employees
I tested each variable with Chi2 and confirmed all were groups were linked to defaults. After Feature Engineering two additional variables, I used all capable features for Feature Selection with Select K Best and Recursive Feature Elimination. I went forward with the following five features:
1. Term
2. Jobs Retained
3. Jobs Count
4. SBA Appoved Amount
5. Monthly Debt
I built 3 classification models using Decision Tree, Random Forest, and K-Nearest Neighbor. All three models performed above baseline with K-Nearest Neighbor peforming the best with a 93% accuracy on Train, 89% accuracy on Validate, and 89% accuracy on Test. K-Nearest Neighbor performed the best, is not under or overfit, and will work on new data

#### conclusion recommendations (Report.ipynb)

Recommend model for next phase of testing and to be considered for operational implementation

#### conclusion next steps (Report.ipynb)

Recommend model for next phase of testing and to be considered for operational implementation

#### no errors (Report.ipynb)

- no errors in report

