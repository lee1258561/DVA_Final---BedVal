# Before running the code,please make sure you have installed pandas and sklearn.

#Experiments of prediction
import numpy as np
import pandas as pd
import time

from sklearn.model_selection import cross_val_score, GridSearchCV, cross_validate, train_test_split
from sklearn.metrics import accuracy_score, classification_report, mean_squared_error as MSE
from sklearn.svm import SVC
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler, normalize
from sklearn.neural_network import MLPRegressor

##df1 = pd.read_csv('SF_data.csv',header=0)
##
##df2 = pd.read_csv('SanFran_ALL.csv',header=0)
##
##data= df1.set_index('id').join(df2.set_index('id'))
##
##data.to_csv('combined1.csv')
##
###print(data)

data= pd.read_csv('combined1.csv')

data2 = data.loc[:,['price','Monthly_demand','host_is_superhost','host_listings_count','host_has_profile_pic',
                          'host_identity_verified','apt','house','entire','accommodates',
                          'beds','realbed','WIFI','review_scores_rating','instant_bookable',
                          'require_guest_phone_verification','avg_avail','longitude','latitude','namepos','despos','desneu','top1','top5_avg','total_avg','within_radius_avg']]

#The last two are the new variables that I want to test

data3 = data2.dropna(axis=0)




# Separate out the x_data and y_data.
x_data = data3.loc[:,['host_is_superhost','host_listings_count','host_has_profile_pic',
                          'host_identity_verified','apt','house','entire','accommodates',
                          'beds','realbed','WIFI','review_scores_rating','instant_bookable',
                          'require_guest_phone_verification','avg_avail','longitude','latitude','namepos','despos','desneu','top1','top5_avg','total_avg','within_radius_avg']]
x_baseline = data3.loc[:,['host_is_superhost','host_listings_count','host_has_profile_pic',
                          'host_identity_verified','apt','house','entire','accommodates',
                          'beds','realbed','WIFI','review_scores_rating','instant_bookable',
                          'require_guest_phone_verification']]
Y1 = data3.loc[:,'price']
Y2 = data3.loc[:,'Monthly_demand']
# The random state to use while splitting the data.
random_state = 100

# price prediction
# Baseline model data split

X_base_train, X_base_test, price_train, price_test = train_test_split(x_baseline,Y1,test_size=0.25,random_state=100)

# New model data split
X_train, X_test, price_train1, price_test1 = train_test_split(x_data,Y1,test_size=0.25,random_state=100)

#Demand prediction
X_base_train1, X_base_test1, demand_train, demand_test = train_test_split(x_baseline,Y2,test_size=0.25,random_state=100)

# New model data split
X_train1, X_test1, demand_train1, demand_test1 = train_test_split(x_data,Y2,test_size=0.25,random_state=100)

##print(X_train)
##print(X_base_train)
##print(price_train)
##print(price_train1)

# Price_OLS
# baseline model
OLSest =LinearRegression()
OLSest.fit(X_base_train,price_train)

# OLS out-of-sample accuracy
y_predict_OLS_outsample = OLSest.predict(X_base_test)


OLS_outsample=MSE(price_test,y_predict_OLS_outsample)
print('Baseline model OLS prediction for price out-sample MSE: ',OLS_outsample)

# new model
OLSest1 =LinearRegression()
OLSest1.fit(X_train,price_train1)

# OLS out-of-sample accuracy
y_predict_OLS_outsample1 = OLSest1.predict(X_test)


OLS_outsample1=MSE(price_test1,y_predict_OLS_outsample1)
print('New model OLS prediction for price out-sample MSE: ',OLS_outsample1)

# Demand_OLS
# baseline model

OLSest2 =LinearRegression()
OLSest2.fit(X_base_train1,demand_train)

# OLS out-of-sample accuracy
y_predict_OLS_outsample2 = OLSest2.predict(X_base_test1)


OLS_outsample2=MSE(demand_test,y_predict_OLS_outsample2)
print('Baseline model OLS prediction for demand out-sample MSE: ',OLS_outsample2)

# new model
OLSest3 =LinearRegression()
OLSest3.fit(X_train1,demand_train1)

# OLS out-of-sample accuracy
y_predict_OLS_outsample3 = OLSest3.predict(X_test1)


OLS_outsample3=MSE(demand_test1,y_predict_OLS_outsample3)
print('New model OLS prediction for demand out-sample MSE: ',OLS_outsample3)





#Random forest

#price
#Baseline

rf = RandomForestRegressor(random_state=100,n_estimators=200)
rf.fit(X_base_train,price_train)


rf_predict_outsample = rf.predict(X_base_test)
#print(rf_predict_outsample1)
rf_outsample=MSE(price_test,rf_predict_outsample)
print('Baseline model random forest prediction for price out-sample MSE: ',rf_outsample)

#New model

rf1 = RandomForestRegressor(random_state=100,n_estimators=200)
rf1.fit(X_train,price_train1)


rf_predict_outsample1 = rf1.predict(X_test)
#print(rf_predict_outsample1)
rf_outsample1=MSE(price_test1,rf_predict_outsample1)
print('New model random forest prediction for price out-sample MSE: ',rf_outsample1)

# demand
# Baseline


rf2 = RandomForestRegressor(random_state=100,n_estimators=200)
rf2.fit(X_base_train1,demand_train)


rf_predict_outsample2 = rf2.predict(X_base_test1)
#print(rf_predict_outsample1)
rf_outsample2=MSE(demand_test,rf_predict_outsample2)
print('Baseline model random forest prediction for demand out-sample MSE: ',rf_outsample2)

#New model

rf3 = RandomForestRegressor(random_state=100,n_estimators=200)
rf3.fit(X_train1,demand_train1)


rf_predict_outsample3 = rf3.predict(X_test1)
#print(rf_predict_outsample1)
rf_outsample3=MSE(demand_test1,rf_predict_outsample3)
print('New model random forest prediction for demand out-sample MSE: ',rf_outsample3)




# tunning the parameter
##param_grid = { 
##    'max_depth' : [x for x in range(1,10)],
##    'min_samples_split':[x for x in range(2,6)],
##    'min_samples_leaf':[x for x in range(1,10)]}                   
##
##CV_rf = GridSearchCV(estimator=rf1, param_grid=param_grid, cv= 10, n_jobs = -1)
##CV_rf.fit(X_train,y_train)
##print(CV_rf.best_params_)
##print(CV_rf.best_score_)


# shallow neural network
# Price
# Baseline model

snn = MLPRegressor(
    hidden_layer_sizes=(1,),  activation='relu', solver='adam', alpha=0.001, batch_size='auto',
    learning_rate='constant', learning_rate_init=0.01, power_t=0.5, max_iter=1000, shuffle=True,
    random_state=9, tol=0.0001, verbose=False, warm_start=False, momentum=0.9, nesterovs_momentum=True,
    early_stopping=False, validation_fraction=0.1, beta_1=0.9, beta_2=0.999, epsilon=1e-08)

snn.fit(X_base_train,price_train)


#snn out-of-sample accuracy
y_predict_snn_outsample = snn.predict(X_base_test)
#print(y_predict_OLS_outsample1)
snn_outsample=MSE(price_test,y_predict_snn_outsample)
print('Baseline model SNN prediction for price out-sample MSE: ',snn_outsample)

# New model
snn1 = MLPRegressor(
    hidden_layer_sizes=(1,),  activation='relu', solver='adam', alpha=0.001, batch_size='auto',
    learning_rate='constant', learning_rate_init=0.01, power_t=0.5, max_iter=1000, shuffle=True,
    random_state=9, tol=0.0001, verbose=False, warm_start=False, momentum=0.9, nesterovs_momentum=True,
    early_stopping=False, validation_fraction=0.1, beta_1=0.9, beta_2=0.999, epsilon=1e-08)

snn1.fit(X_train,price_train1)

#snn out-of-sample accuracy
y_predict_snn_outsample1 = snn1.predict(X_test)
#print(y_predict_OLS_outsample1)
snn_outsample1=MSE(price_test1,y_predict_snn_outsample1)
print('New model SNN prediction for price out-sample MSE: ',snn_outsample1)

# Demand
# Baseline model

snn2 = MLPRegressor(
    hidden_layer_sizes=(1,),  activation='relu', solver='adam', alpha=0.001, batch_size='auto',
    learning_rate='constant', learning_rate_init=0.01, power_t=0.5, max_iter=1000, shuffle=True,
    random_state=9, tol=0.0001, verbose=False, warm_start=False, momentum=0.9, nesterovs_momentum=True,
    early_stopping=False, validation_fraction=0.1, beta_1=0.9, beta_2=0.999, epsilon=1e-08)

snn2.fit(X_base_train1,demand_train)


#snn out-of-sample accuracy
y_predict_snn_outsample2 = snn2.predict(X_base_test1)
#print(y_predict_OLS_outsample1)
snn_outsample2=MSE(demand_test,y_predict_snn_outsample2)
print('Baseline model SNN prediction for demand out-sample MSE: ',snn_outsample2)

# New model
snn3 = MLPRegressor(
    hidden_layer_sizes=(1,),  activation='relu', solver='adam', alpha=0.001, batch_size='auto',
    learning_rate='constant', learning_rate_init=0.01, power_t=0.5, max_iter=1000, shuffle=True,
    random_state=9, tol=0.0001, verbose=False, warm_start=False, momentum=0.9, nesterovs_momentum=True,
    early_stopping=False, validation_fraction=0.1, beta_1=0.9, beta_2=0.999, epsilon=1e-08)

snn3.fit(X_train1,demand_train1)

#snn out-of-sample accuracy
y_predict_snn_outsample3 = snn3.predict(X_test1)
#print(y_predict_OLS_outsample1)
snn_outsample3=MSE(demand_test1,y_predict_snn_outsample3)
print('New model SNN prediction for demand out-sample MSE: ',snn_outsample3)


