import numpy as np
import pandas as pd
import time
from sklearn.linear_model import LinearRegression as lm
import statsmodels.api as sm 

data = pd.read_csv('combined1.csv')

# independent variables from the previous research

data2 = data.loc[:,['price','Monthly_demand','host_is_superhost','host_listings_count','host_has_profile_pic',
                          'host_identity_verified','apt','house','entire','accommodates',
                          'beds','realbed','WIFI','review_scores_rating','instant_bookable',
                          'require_guest_phone_verification','top1_attr','top5_avg_attr','within_radius_avg_attr','total_avg_attr',
                    'within_radius_count_attr']]
                          
#The last two are the new variables that I want to test

data3 = data2.dropna(axis=0)


#dependents
Y1 = data3.loc[:,'price']
Y2 = data3.loc[:,'Monthly_demand']

# 'top1_attr','top5_avg_attr','within_radius_avg_attr','total_avg_attr','within_radius_count_attr'
# 'top1_attr','top5_avg_attr','within_radius_avg_attr','total_avg_attr','within_radius_count_attr'
#independents for 1st regression on price
independent1 = data3.loc[:,['host_is_superhost','host_listings_count','host_has_profile_pic',
                          'host_identity_verified','apt','house','entire','accommodates',
                          'beds','realbed','WIFI','review_scores_rating','instant_bookable',
                          'require_guest_phone_verification','within_radius_count_attr']]

independent2 = data3.loc[:,['host_is_superhost','host_listings_count','host_has_profile_pic',
                          'host_identity_verified','apt','house','entire','accommodates',
                          'beds','realbed','WIFI','review_scores_rating','instant_bookable',
                          'require_guest_phone_verification','within_radius_count_attr']]




# Add in intercepts
indep2 = sm.add_constant(independent1)
indep3 = sm.add_constant(independent2)

# reg1
est1 = sm.OLS(Y1,indep2)
est2 = est1.fit()
print(est2.summary())

# reg2
est3 = sm.OLS(Y2,indep3)
est4 = est3.fit()
print(est4.summary())

data = pd.read_csv('combined1.csv')

# independent variables from the previous research

data2 = data.loc[:,['price','Monthly_demand','host_is_superhost','host_listings_count','host_has_profile_pic',
                          'host_identity_verified','apt','house','entire','accommodates',
                          'beds','realbed','WIFI','review_scores_rating','instant_bookable',
                          'require_guest_phone_verification','top1_attr','top5_avg_attr','within_radius_avg_attr','total_avg_attr',
                    'within_radius_count_attr']]
                          
#The last two are the new variables that I want to test

data3 = data2.dropna(axis=0)


#dependents
Y1 = data3.loc[:,'price']
Y2 = data3.loc[:,'Monthly_demand']

independent1 = data3.loc[:,['host_is_superhost','host_listings_count','host_has_profile_pic',
                          'host_identity_verified','apt','house','entire','accommodates',
                          'beds','realbed','WIFI','review_scores_rating','instant_bookable',
                          'require_guest_phone_verification','top5_avg_attr']]

independent2 = data3.loc[:,['host_is_superhost','host_listings_count','host_has_profile_pic',
                          'host_identity_verified','apt','house','entire','accommodates',
                          'beds','realbed','WIFI','review_scores_rating','instant_bookable',
                          'require_guest_phone_verification','top5_avg_attr']]




# Add in intercepts
indep2 = sm.add_constant(independent1)
indep3 = sm.add_constant(independent2)

# reg1
est1 = sm.OLS(Y1,indep2)
est2 = est1.fit()
print(est2.summary())

# reg2
est3 = sm.OLS(Y2,indep3)
est4 = est3.fit()
print(est4.summary())






