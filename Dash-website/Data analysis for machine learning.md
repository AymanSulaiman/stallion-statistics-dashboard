# New data Analytics for tvg_cd_data

This notebook is going to analyse the `tfg_cd_data.csv` file and observe how it can be used for machine learning application


```python
# Importing the required modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import warnings
warnings.filterwarnings('ignore')
%matplotlib inline
```


```python
df = pd.read_csv(os.path.join('tvg_cd_data.csv'))
df.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>racedater</th>
      <th>tvgtrackcode</th>
      <th>race</th>
      <th>bettinginterestnumber</th>
      <th>horsename</th>
      <th>morninglineodds</th>
      <th>currentodds</th>
      <th>tvghorseweight</th>
      <th>tvghorsedamsirename</th>
      <th>tvghorseage</th>
      <th>...</th>
      <th>tvghorsenumberofwins</th>
      <th>tvghorsenumberofstarts</th>
      <th>tvghorsepowerrating</th>
      <th>tvghorseaveragespeed</th>
      <th>tvghorseaverageclassrating</th>
      <th>currentodds.1</th>
      <th>winpayout</th>
      <th>placepayout</th>
      <th>showpayout</th>
      <th>scratched</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2224</th>
      <td>2020-05-29</td>
      <td>cd</td>
      <td>9</td>
      <td>7</td>
      <td>out cold</td>
      <td>20.0</td>
      <td>SC</td>
      <td>123</td>
      <td>northern afleet</td>
      <td>4</td>
      <td>...</td>
      <td>1</td>
      <td>2</td>
      <td>69.8</td>
      <td>75</td>
      <td>81</td>
      <td>SC</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2225</th>
      <td>2020-05-29</td>
      <td>cd</td>
      <td>9</td>
      <td>8</td>
      <td>irish spirit</td>
      <td>3.0</td>
      <td>3</td>
      <td>123</td>
      <td>forest camp</td>
      <td>5</td>
      <td>...</td>
      <td>0</td>
      <td>1</td>
      <td>78.4</td>
      <td>89</td>
      <td>97</td>
      <td>3</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2226</th>
      <td>2020-05-29</td>
      <td>cd</td>
      <td>9</td>
      <td>9</td>
      <td>alex's strike</td>
      <td>8.0</td>
      <td>4</td>
      <td>123</td>
      <td>smart strike</td>
      <td>4</td>
      <td>...</td>
      <td>1</td>
      <td>8</td>
      <td>84.4</td>
      <td>80</td>
      <td>87</td>
      <td>4</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2227</th>
      <td>2020-05-29</td>
      <td>cd</td>
      <td>9</td>
      <td>10</td>
      <td>heros reward</td>
      <td>10.0</td>
      <td>2</td>
      <td>118</td>
      <td>smart strike</td>
      <td>3</td>
      <td>...</td>
      <td>1</td>
      <td>3</td>
      <td>86.1</td>
      <td>77</td>
      <td>90</td>
      <td>2</td>
      <td>6.2</td>
      <td>4.2</td>
      <td>3.8</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2228</th>
      <td>2020-05-29</td>
      <td>cd</td>
      <td>9</td>
      <td>11</td>
      <td>nice of me</td>
      <td>20.0</td>
      <td>19</td>
      <td>123</td>
      <td>allen's prospect</td>
      <td>4</td>
      <td>...</td>
      <td>1</td>
      <td>7</td>
      <td>79.2</td>
      <td>74</td>
      <td>90</td>
      <td>19</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>8.4</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 22 columns</p>
</div>



Going to draw some histograms for this dataset


```python
column_list = [i for i in df.columns]
print(column_list)
```

    ['racedater', 'tvgtrackcode', 'race', 'bettinginterestnumber', 'horsename', 'morninglineodds', 'currentodds', 'tvghorseweight', 'tvghorsedamsirename', 'tvghorseage', 'tvghorsesex', 'tvghorsedaysoff', 'tvghorsenumberofwins', 'tvghorsenumberofstarts', 'tvghorsepowerrating', 'tvghorseaveragespeed', 'tvghorseaverageclassrating', 'currentodds.1', 'winpayout', 'placepayout', 'showpayout', 'scratched']
    


```python
print(df.tvghorseweight.min())
print(max(df.tvghorseweight))
```

    0
    126
    

# Histogram Analysis


```python
fig, ax = plt.subplots()
n_bins = 20
ax.hist(x=df.tvghorseweight, bins=n_bins);
```


![png](output_7_0.png)



```python
fig, ax = plt.subplots()
n_bins = 20
ax.hist(x=df.tvghorseage, bins=n_bins);
```


![png](output_8_0.png)


There appears to be a huge amount of range, After inspecting the data on jupyter labs, there are horse called `(null)` so we shall get rid of them and find the true values


```python
df_copy = df.copy()
```


```python
df_copy = df_copy[df.tvghorsedamsirename != '(null)']
df_copy.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>racedater</th>
      <th>tvgtrackcode</th>
      <th>race</th>
      <th>bettinginterestnumber</th>
      <th>horsename</th>
      <th>morninglineodds</th>
      <th>currentodds</th>
      <th>tvghorseweight</th>
      <th>tvghorsedamsirename</th>
      <th>tvghorseage</th>
      <th>...</th>
      <th>tvghorsenumberofwins</th>
      <th>tvghorsenumberofstarts</th>
      <th>tvghorsepowerrating</th>
      <th>tvghorseaveragespeed</th>
      <th>tvghorseaverageclassrating</th>
      <th>currentodds.1</th>
      <th>winpayout</th>
      <th>placepayout</th>
      <th>showpayout</th>
      <th>scratched</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2224</th>
      <td>2020-05-29</td>
      <td>cd</td>
      <td>9</td>
      <td>7</td>
      <td>out cold</td>
      <td>20.0</td>
      <td>SC</td>
      <td>123</td>
      <td>northern afleet</td>
      <td>4</td>
      <td>...</td>
      <td>1</td>
      <td>2</td>
      <td>69.8</td>
      <td>75</td>
      <td>81</td>
      <td>SC</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2225</th>
      <td>2020-05-29</td>
      <td>cd</td>
      <td>9</td>
      <td>8</td>
      <td>irish spirit</td>
      <td>3.0</td>
      <td>3</td>
      <td>123</td>
      <td>forest camp</td>
      <td>5</td>
      <td>...</td>
      <td>0</td>
      <td>1</td>
      <td>78.4</td>
      <td>89</td>
      <td>97</td>
      <td>3</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2226</th>
      <td>2020-05-29</td>
      <td>cd</td>
      <td>9</td>
      <td>9</td>
      <td>alex's strike</td>
      <td>8.0</td>
      <td>4</td>
      <td>123</td>
      <td>smart strike</td>
      <td>4</td>
      <td>...</td>
      <td>1</td>
      <td>8</td>
      <td>84.4</td>
      <td>80</td>
      <td>87</td>
      <td>4</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2227</th>
      <td>2020-05-29</td>
      <td>cd</td>
      <td>9</td>
      <td>10</td>
      <td>heros reward</td>
      <td>10.0</td>
      <td>2</td>
      <td>118</td>
      <td>smart strike</td>
      <td>3</td>
      <td>...</td>
      <td>1</td>
      <td>3</td>
      <td>86.1</td>
      <td>77</td>
      <td>90</td>
      <td>2</td>
      <td>6.2</td>
      <td>4.2</td>
      <td>3.8</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2228</th>
      <td>2020-05-29</td>
      <td>cd</td>
      <td>9</td>
      <td>11</td>
      <td>nice of me</td>
      <td>20.0</td>
      <td>19</td>
      <td>123</td>
      <td>allen's prospect</td>
      <td>4</td>
      <td>...</td>
      <td>1</td>
      <td>7</td>
      <td>79.2</td>
      <td>74</td>
      <td>90</td>
      <td>19</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>8.4</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 22 columns</p>
</div>




```python
fig, ax = plt.subplots()
n_bins = 20
ax.hist(x=df_copy.tvghorseweight, bins=n_bins);
ax.set(title='horse weight histogram', xlabel='weight (lb)', ylabel='count');
```


![png](output_12_0.png)



```python
fig, ax = plt.subplots()
n_bins = 20
ax.hist(x=df_copy.tvghorseage, bins=n_bins);
ax.set(title='horse age histogram', xlabel='age (years)', ylabel='count');
```


![png](output_13_0.png)



```python
fig, ax = plt.subplots()
n_bins = 20
ax.hist(x=df_copy.tvghorsedaysoff, bins=n_bins);
ax.set(title='horse number of days off histogram', xlabel='Number of days off', ylabel='count');
```


![png](output_14_0.png)



```python
fig, ax = plt.subplots()
n_bins = 20
ax.hist(x=df_copy.tvghorsenumberofwins, bins=n_bins);
ax.set(title='horse number of wins histogram', xlabel='Number of wins', ylabel='count');
```


![png](output_15_0.png)



```python
fig, ax = plt.subplots()
n_bins = 20
ax.hist(x=df_copy.tvghorsepowerrating, bins=n_bins);
ax.set(title='horse power rating', xlabel='horsepower', ylabel='count');
```


![png](output_16_0.png)



```python
fig, ax = plt.subplots()
n_bins = 20
ax.hist(x=df_copy.tvghorseaveragespeed, bins=n_bins);
ax.set(title='horse average speed', xlabel='Speed (Beyer)', ylabel='count');
```


![png](output_17_0.png)



```python
fig, ax = plt.subplots()
n_bins = 20
ax.hist(x=df_copy.tvghorseaverageclassrating, bins=n_bins);
ax.set(title='horse average class rating', xlabel='horse average class rating', ylabel='count');
```


![png](output_18_0.png)


There appears to be a consistant theme here, there is a value of zeros at the same count, lets get rid of them


```python
df_copy = df_copy[df.tvghorseaverageclassrating != 0]
df_copy.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>racedater</th>
      <th>tvgtrackcode</th>
      <th>race</th>
      <th>bettinginterestnumber</th>
      <th>horsename</th>
      <th>morninglineodds</th>
      <th>currentodds</th>
      <th>tvghorseweight</th>
      <th>tvghorsedamsirename</th>
      <th>tvghorseage</th>
      <th>...</th>
      <th>tvghorsenumberofwins</th>
      <th>tvghorsenumberofstarts</th>
      <th>tvghorsepowerrating</th>
      <th>tvghorseaveragespeed</th>
      <th>tvghorseaverageclassrating</th>
      <th>currentodds.1</th>
      <th>winpayout</th>
      <th>placepayout</th>
      <th>showpayout</th>
      <th>scratched</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2224</th>
      <td>2020-05-29</td>
      <td>cd</td>
      <td>9</td>
      <td>7</td>
      <td>out cold</td>
      <td>20.0</td>
      <td>SC</td>
      <td>123</td>
      <td>northern afleet</td>
      <td>4</td>
      <td>...</td>
      <td>1</td>
      <td>2</td>
      <td>69.8</td>
      <td>75</td>
      <td>81</td>
      <td>SC</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2225</th>
      <td>2020-05-29</td>
      <td>cd</td>
      <td>9</td>
      <td>8</td>
      <td>irish spirit</td>
      <td>3.0</td>
      <td>3</td>
      <td>123</td>
      <td>forest camp</td>
      <td>5</td>
      <td>...</td>
      <td>0</td>
      <td>1</td>
      <td>78.4</td>
      <td>89</td>
      <td>97</td>
      <td>3</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2226</th>
      <td>2020-05-29</td>
      <td>cd</td>
      <td>9</td>
      <td>9</td>
      <td>alex's strike</td>
      <td>8.0</td>
      <td>4</td>
      <td>123</td>
      <td>smart strike</td>
      <td>4</td>
      <td>...</td>
      <td>1</td>
      <td>8</td>
      <td>84.4</td>
      <td>80</td>
      <td>87</td>
      <td>4</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2227</th>
      <td>2020-05-29</td>
      <td>cd</td>
      <td>9</td>
      <td>10</td>
      <td>heros reward</td>
      <td>10.0</td>
      <td>2</td>
      <td>118</td>
      <td>smart strike</td>
      <td>3</td>
      <td>...</td>
      <td>1</td>
      <td>3</td>
      <td>86.1</td>
      <td>77</td>
      <td>90</td>
      <td>2</td>
      <td>6.2</td>
      <td>4.2</td>
      <td>3.8</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2228</th>
      <td>2020-05-29</td>
      <td>cd</td>
      <td>9</td>
      <td>11</td>
      <td>nice of me</td>
      <td>20.0</td>
      <td>19</td>
      <td>123</td>
      <td>allen's prospect</td>
      <td>4</td>
      <td>...</td>
      <td>1</td>
      <td>7</td>
      <td>79.2</td>
      <td>74</td>
      <td>90</td>
      <td>19</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>8.4</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 22 columns</p>
</div>



Re-visualising


```python
fig, ax = plt.subplots()
n_bins = 20
ax.hist(x=df_copy.tvghorseweight, bins=n_bins);
ax.set(title='horse weight histogram', xlabel='weight (lb)', ylabel='count');
```


![png](output_22_0.png)



```python
fig, ax = plt.subplots()
n_bins = 20
ax.hist(x=df_copy.tvghorseage, bins=n_bins);
ax.set(title='horse age histogram', xlabel='age (years)', ylabel='count');
```


![png](output_23_0.png)



```python
fig, ax = plt.subplots()
n_bins = 20
ax.hist(x=df_copy.tvghorsedaysoff, bins=n_bins);
ax.set(title='horse number of days off histogram', xlabel='Number of days off', ylabel='count');
```


![png](output_24_0.png)



```python
fig, ax = plt.subplots()
n_bins = 20
ax.hist(x=df_copy.tvghorsenumberofwins, bins=n_bins);
ax.set(title='horse number of wins histogram', xlabel='Number of wins', ylabel='count');
```


![png](output_25_0.png)



```python
fig, ax = plt.subplots()
n_bins = 20
ax.hist(x=df_copy.tvghorsepowerrating, bins=n_bins);
ax.set(title='horse power rating', xlabel='horsepower', ylabel='count');
```


![png](output_26_0.png)



```python
fig, ax = plt.subplots()
n_bins = 20
ax.hist(x=df_copy.tvghorseaveragespeed, bins=n_bins);
ax.set(title='horse average speed', xlabel='Speed (Beyer)', ylabel='count');
```


![png](output_27_0.png)



```python
fig, ax = plt.subplots()
n_bins = 20
ax.hist(x=df_copy.tvghorseaverageclassrating, bins=n_bins);
ax.set(title='horse average class rating', xlabel='horse average class rating', ylabel='count');
```


![png](output_28_0.png)


Data looks a lot cleaner and useable

I will analyse the data further and apply a regression model to measure the, predict and contrast the data.


```python
df_copy.to_csv('cleaned_tvg_cd_data.csv',index=False)
```


```python
x = len([i for i in df_copy.columns])
x
```




    22



# Machine Learning


```python
features = [
    'tvghorseweight', 
    'tvghorseage', 
    'tvghorsedaysoff', 
    'tvghorsenumberofwins', 
    'tvghorsepowerrating', 
    'tvghorseaverageclassrating'
]
target = 'tvghorseaveragespeed'

for i in features:
    x=df_copy[i]
    y=df_copy[target]
    m, c = np.polyfit(x, y, 1)
    plt.plot(x, y, 'o')
    plt.plot(x, m*x + c)
    plt.xlabel(i)
    plt.ylabel(target)
    plt.title(f'{i} and {target}')
    plt.show()
```


![png](output_33_0.png)



![png](output_33_1.png)



![png](output_33_2.png)



![png](output_33_3.png)



![png](output_33_4.png)



![png](output_33_5.png)


### This all looks good for the machine learning model

We decided that the features to be:
* Weight
* Age
* Days Off
* Number of Wins
* Power Rating
* Average Class Rating

We wanted to know the Buyer speed so we have that as the target.


```python
features = [
    'tvghorseweight', 
    'tvghorseage', 
    'tvghorsedaysoff', 
    'tvghorsenumberofwins', 
    'tvghorsepowerrating', 
    'tvghorseaverageclassrating'
]

target = 'tvghorseaveragespeed'

X = df_copy[features]
y = df_copy[target].values.reshape(-1,1)
```


```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
```


```python
# scaling the data

from sklearn.preprocessing import StandardScaler
X_scaler = StandardScaler().fit(X_train)
y_scaler = StandardScaler().fit(y_train)
X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)
y_train_scaled = y_scaler.transform(y_train)
y_test_scaled = y_scaler.transform(y_test)
```


```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train_scaled, y_train_scaled)
```




    LinearRegression()




```python
predictions = model.predict(X_test_scaled)
model.fit(X_train_scaled, y_train_scaled)
plt.scatter(model.predict(X_train_scaled), model.predict(X_train_scaled) - y_train_scaled, c="blue", label="Training Data")
plt.scatter(model.predict(X_test_scaled), model.predict(X_test_scaled) - y_test_scaled, c="orange", label="Testing Data")
plt.legend()
plt.hlines(y=0, xmin=y_test_scaled.min(), xmax=y_test_scaled.max())
plt.title("Residual Plot")
plt.show()
```


![png](output_39_0.png)


Measuring the Linear Model


```python
from sklearn.metrics import mean_squared_error

MSE_linear_regression = mean_squared_error(y_test_scaled, predictions)
r2_linear_regression = model.score(X_test_scaled, y_test_scaled)
### END SOLUTION

print(f"MSE: {MSE_linear_regression}, R2: {r2_linear_regression}")
```

    MSE: 0.16302412817702236, R2: 0.8393376790850877
    

Fitting, predicting and scoreing the Lasso Linear Model


```python
from sklearn.linear_model import Lasso

### BEGIN SOLUTION
lasso = Lasso(alpha=.01).fit(X_train_scaled, y_train_scaled)

predictions = lasso.predict(X_test_scaled)

MSE_lasso = mean_squared_error(y_test_scaled, predictions)
r2_lasso = lasso.score(X_test_scaled, y_test_scaled)
### END SOLUTION

print(f"MSE: {MSE_lasso}, R2: {r2_lasso}")
```

    MSE: 0.164375594141657, R2: 0.8380057924438664
    

Fitting, predicting and scoreing the Ridge Linear Model


```python
from sklearn.linear_model import Ridge

### BEGIN SOLUTION
ridge = Ridge(alpha=.01).fit(X_train_scaled, y_train_scaled)

predictions = ridge.predict(X_test_scaled)

MSE_ridge = mean_squared_error(y_test_scaled, predictions)
r2_ridge = ridge.score(X_test_scaled, y_test_scaled)
### END SOLUTION

print(f"MSE: {MSE_ridge}, R2: {r2_ridge}")
```

    MSE: 0.16302432612175946, R2: 0.8393374840080692
    

Fitting, predicting and scoreing the ElasticNet Model


```python
from sklearn.linear_model import ElasticNet

### BEGIN SOLUTION
elasticnet = ElasticNet(alpha=.01).fit(X_train_scaled, y_train_scaled)

predictions = elasticnet.predict(X_test_scaled)

MSE_elastic = mean_squared_error(y_test_scaled, predictions)
r2_elastic = elasticnet.score(X_test_scaled, y_test_scaled)
### END SOLUTION

print(f"MSE: {MSE_elastic}, R2: {r2_elastic}")
```

    MSE: 0.16379617411249137, R2: 0.8385768181424015
    
