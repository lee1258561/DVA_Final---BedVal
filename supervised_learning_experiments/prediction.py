import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score, classification_report, mean_squared_error as MSE
from sklearn.model_selection import cross_val_score, GridSearchCV, cross_validate, train_test_split
from sklearn.linear_model import LinearRegression


data= pd.read_csv('combined1.csv')

data2 = data.loc[:,['price','Monthly_demand','host_is_superhost','host_listings_count','host_has_profile_pic',
                          'host_identity_verified','apt','house','entire','accommodates','monthly_available',
                          'beds','realbed','WIFI','review_scores_rating','instant_bookable','longitude','latitude',
                          'require_guest_phone_verification','top1','top5_avg','total_avg','within_radius_avg']]

#The last two are the new variables that I want to test

data3 = data2.dropna(axis=0)
x_data = data3.loc[:,['host_is_superhost','host_listings_count','host_has_profile_pic',
                          'host_identity_verified','apt','house','entire','accommodates','monthly_available',
                          'beds','realbed','WIFI','review_scores_rating','instant_bookable','longitude','latitude',
                          'require_guest_phone_verification','top1','top5_avg','total_avg','within_radius_avg']]

Y1 = data3.loc[:,'price']
Y2 = data3.loc[:,'Monthly_demand']

random_state = 100

#Splitting for price

X_train, X_test, price_train, y_test = train_test_split(x_data,Y1,test_size=0.2,random_state=100)

X_train1, X_test1, demand_train1, demand_test1 = train_test_split(x_data,Y2,test_size=0.25,random_state=100)

# For price, linear regression seems better

OLS_P =LinearRegression()
OLS_P.fit(X_train,price_train)

# For demand, random forest seems better

RF_P = RandomForestRegressor(random_state=100,max_depth=9,min_samples_split=5,min_samples_leaf=2,n_estimators=200)
RF_P.fit(X_train1,demand_train1)

####tunning the parameter
##param_grid = { 
##    'max_depth' : [x for x in range(1,10)],
##    'min_samples_split':[x for x in range(2,6)],
##    'min_samples_leaf':[x for x in range(1,10)]}                   
##
##CV_rf = GridSearchCV(estimator=RF_P, param_grid=param_grid, cv= 10, n_jobs = -1)
##CV_rf.fit(X_train1,demand_train1)
##print(CV_rf.best_params_)
##print(CV_rf.best_score_)
P_test = np.asarray(X_test.iloc[1,:]).reshape(1,-1)
D_test = np.asarray(X_test1.iloc[1,:]).reshape(1,-1)

print(y_test.iloc[1])
print(demand_test1.iloc[1])

def predict_price(record):
    print(OLS_P.predict(record))

def predict_demand(record):
    print(RF_P.predict(record))

 
