import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
import os

class splitter:

    def __init__(self, X, y):
        self.X = X
        self.y = y

    def splitting_function(self, test_size=0.2):
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=test_size, random_state=42)
        return X_train, X_test, y_train, y_test

class scaler:

    def X_scaler_function(X_train, X_test):
        from sklearn.preprocessing import StandardScaler
        X_scaler = StandardScaler().fit(X_train)
        X_train_scaled = X_scaler.transform(X_train)
        X_test_scaled = X_scaler.transform(X_test)

        return X_train_scaled, X_test_scaled

    
    def y_scaler_function(y_train, y_test):
        from sklearn.preprocessing import StandardScaler
        y_scaler = StandardScaler().fit(y_train)
        y_train_scaled = y_scaler.transform(y_train)
        y_test_scaled = y_scaler.transform(y_test)
        
        return y_train_scaled, y_test_scaled

class regression_models:
        
    def linear_regression(X_train_scaled, X_test_scaled, y_train_scaled, y_test_scaled):
        from sklearn.linear_model import LinearRegression
        model = LinearRegression().fit(X_train_scaled, y_train_scaled)
        linear_predictions = model.predict(X_test_scaled)
        MSE_linear_regression = mean_squared_error(y_test_scaled, linear_predictions)
        r2_linear_regression = model.score(X_test_scaled, y_test_scaled)
        
        return linear_predictions, MSE_linear_regression, r2_linear_regression


    def lasso(X_train_scaled, X_test_scaled, y_train_scaled, y_test_scaled):
        from sklearn.linear_model import Lasso
        lasso = Lasso(alpha=.01).fit(X_train_scaled, y_train_scaled)
        lasso_predictions = lasso.predict(X_test_scaled)
        MSE_lasso = mean_squared_error(y_test_scaled, lasso_predictions)
        r2_lasso = lasso.score(X_test_scaled, y_test_scaled)

        return lasso_predictions, MSE_lasso, r2_lasso



    def ridge(X_train_scaled, X_test_scaled, y_train_scaled, y_test_scaled):
        from sklearn.linear_model import Ridge
        ridge = Ridge(alpha=.01).fit(X_train_scaled, y_train_scaled)
        ridge_predictions = ridge.predict(X_test_scaled)
        MSE_ridge = mean_squared_error(y_test_scaled, ridge_predictions)
        r2_ridge = ridge.score(X_test_scaled, y_test_scaled)

        return ridge_predictions, MSE_ridge, r2_ridge



    def elastic_net(X_train_scaled, X_test_scaled, y_train_scaled, y_test_scaled):
        from sklearn.linear_model import ElasticNet
        elasticnet = ElasticNet(alpha=.01).fit(X_train_scaled, y_train_scaled)
        elasticnet_predictions = elasticnet.predict(X_test_scaled)
        MSE_elastic = mean_squared_error(y_test_scaled, elasticnet_predictions)
        r2_elastic = elasticnet.score(X_test_scaled, y_test_scaled)

        return elasticnet_predictions, MSE_elastic, r2_elastic
