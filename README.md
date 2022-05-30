# Project Overview
You work at Rossmann Pharmaceuticals as a Machine Learning Engineer. The finance team wants to forecast sales in all their stores across several cities six weeks ahead of time. Managers in individual stores rely on their years of experience as well as their personal judgment to forecast sales. 

The data team identified factors such as promotions, competition, school and state holidays, seasonality, and locality as necessary for predicting the sales across the various stores.

# Business Objective
Your job is to build and serve an end-to-end product that delivers this prediction to analysts in the finance team. 

# Skills implemented in the project:
* Advanced use of scikit-learn 
* Feature Engineering
* ML Model building and fine-tuning
* CI/CD deployment of ML models  
* Python logging
* Unit testing  
* Building dashboards


# Manual Installation
### Step 1: Downloading source code
```
git clone https://github.com/tutorialcreation/pharm_sales.git
```
### Step 2: Installation of dependencies
```
pip install -r requirements.txt
```
### Step 3: Check notebook
```
jupyter notebook
```
### Step 4: Visualize ML Pipeline
```
dvc dag
```

# Automatic Installation
### Step 1: Docker
```
docker-compose up --build -d
```

# The tests from the modularized scripts are run in the following notebooks
* EDA analysis ==> notebooks/EDA.ipynb
* Preprocessing and Feature Engineering ==> notebooks/Preprocessing.ipynb
* Machine learning ==> notebooks/Forecasting.ipynb
* Deep learning ==> notebooks/DeepLearning.ipynb

# Dataset Column description
* Id - an Id that represents a (Store, Date) duple within the test set
* Store - a unique Id for each store
* Sales - the turnover for any given day (this is what you are predicting)
* Customers - the number of customers on a given day
* Open - an indicator for whether the store was open: 0 = closed, 1 = open
* StateHoliday - indicates a state holiday. Normally all stores, with few exceptions, are closed on state holidays. Note that all schools are closed on public holidays and weekends. a = public holiday, b = Easter holiday, c = Christmas, 0 = None
* SchoolHoliday - indicates if the (Store, Date) was affected by the closure of public schools
* StoreType - differentiates between 4 different store models: a, b, c, d
* Assortment - describes an assortment level: a = basic, b = extra, c = extended. Read more about assortment here
* CompetitionDistance - distance in meters to the nearest competitor store
* CompetitionOpenSince[Month/Year] - gives the approximate year and month of the time the nearest competitor was opened
* Promo - indicates whether a store is running a promo on that day
* Promo2 - Promo2 is a continuing and consecutive promotion for some stores: 0 = store is not participating, 1 = store is participating
* Promo2Since[Year/Week] - describes the year and calendar week when the store started participating in Promo2
* PromoInterval - describes the consecutive intervals Promo2 is started, naming the months the promotion is started anew. E.g. "Feb,May,Aug,Nov" means each round starts in February, May, August, November of any given year for that store

