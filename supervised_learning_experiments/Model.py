import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score, classification_report, mean_squared_error as MSE
from sklearn.model_selection import cross_val_score, GridSearchCV, cross_validate, train_test_split
from sklearn.linear_model import LinearRegression

###!!!!!!! Before predicting, an initialization is required. e.g md1 = Model()
###!!!!!!! After initialization, use md1.Price_Predict(record) to predict the price. It will return a float.

class Model(object):
    def __init__(self):
        data = pd.read_csv('combined1.csv')
        data2 = data.loc[:,['price','Monthly_demand','host_is_superhost','host_listings_count','host_has_profile_pic',
                          'host_identity_verified','apt','house','entire','accommodates',
                          'beds','realbed','WIFI','review_scores_rating','instant_bookable',
                          'require_guest_phone_verification','avg_avail','longitude','latitude','top1','top5_avg','total_avg','within_radius_avg']]
        data3 = data2.dropna(axis=0)
        x_data = data3.loc[:,['host_is_superhost','host_listings_count','host_has_profile_pic',
                          'host_identity_verified','apt','house','entire','accommodates',
                          'beds','realbed','WIFI','review_scores_rating','instant_bookable',
                          'require_guest_phone_verification','avg_avail','longitude','latitude','top1','top5_avg','total_avg','within_radius_avg']]
        Y1 = data3.loc[:,'price']
        Y2 = data3.loc[:,'Monthly_demand']

        random_state = 100

        #Splitting for price

        X_train, X_test, price_train, y_test = train_test_split(x_data,Y1,test_size=0.2,random_state=100)

        X_train1, X_test1, demand_train1, demand_test1 = train_test_split(x_data,Y2,test_size=0.25,random_state=100)

        # For price, linear regression seems better

        OLS_P =LinearRegression()
        OLS_P.fit(X_train,price_train)
        self.Price = OLS_P

        # For demand, random forest seems better

        RF_P = RandomForestRegressor(random_state=100,max_depth=9,min_samples_split=5,min_samples_leaf=2,n_estimators=200)
        RF_P.fit(X_train1,demand_train1)
        self.Demand = RF_P

    #!!!!! you may choose to return or print the prediction!!!!! the default is to return

    #!!!!! The input must be a row of pandas dataframe!!!!!!!!!!!!!!!!!!

    def Price_Predict(self,record):
        record2 = np.asarray(record).reshape(1,-1)
        #print(self.Price.predict(record2)[0])
        return self.Price.predict(record2)[0]

    def Demand_Predict(self,record):
        record3 = np.asarray(record).reshape(1,-1)
        #print(self.Demand.predict(record3)[0])
        return int(self.Demand.predict(record3)[0])


##---------------------For debugging only-----------------------------------
##
##if __name__=="__main__":
##    md1 = Model()
##    print(md1.Price)
##    print(md1.Demand)
##
##    data = pd.read_csv('combined1.csv')
##    data2 = data.loc[:,['price','Monthly_demand','host_is_superhost','host_listings_count','host_has_profile_pic',
##                          'host_identity_verified','apt','house','entire','accommodates',
##                          'beds','realbed','WIFI','review_scores_rating','instant_bookable',
##                          'require_guest_phone_verification','avg_avail','longitude','latitude','top1','top5_avg','total_avg','within_radius_avg']]
##    data3 = data2.dropna(axis=0)
##    x_data = data3.loc[:,['host_is_superhost','host_listings_count','host_has_profile_pic',
##                          'host_identity_verified','apt','house','entire','accommodates',
##                          'beds','realbed','WIFI','review_scores_rating','instant_bookable',
##                          'require_guest_phone_verification','avg_avail','longitude','latitude','top1','top5_avg','total_avg','within_radius_avg']]
##    Y1 = data3.loc[:,'price']
##    Y2 = data3.loc[:,'Monthly_demand']
##
##    random_state = 100
##
##        #Splitting for price
##
##    X_train, X_test, price_train, y_test = train_test_split(x_data,Y1,test_size=0.2,random_state=100)
##
##    X_train1, X_test1, demand_train1, demand_test1 = train_test_split(x_data,Y2,test_size=0.25,random_state=100)
##
##    Ptest1 = X_test.iloc[8,:]
##    Dtest1 = X_test1.iloc[8,:]
##    DtestY = demand_test1.iloc[8]
##    PtestY = y_test.iloc[8]
##    print(Ptest1)
##    print(md1.Price_Predict(Ptest1))
##    print(md1.Demand_Predict(Dtest1))
##    print(DtestY)
##    print(PtestY)
