# TP : NY Taxi Fare Prediction
We will work on the kaggle challenge
[New York City Taxi Fare Prediction](https://www.kaggle.com/c/new-york-city-taxi-fare-prediction).

You will have to use what you have learned during this course.



## Part 1

### A. Data exploration

1. Download the data from https://www.kaggle.com/c/new-york-city-taxi-fare-prediction/data (Download All button)
or from https://filesender.renater.fr/?s=download&token=22621daf-b2b3-4d36-806c-811b7bc69315


Unzip the data in your working directory.


1. Start a new notebook

2. Load the data from `train.csv` using pandas.
Hint: I recommend you to use an option to limit the number of rows (e.g. to 100.000) loaded at first so you will have less trouble handling the data.

1. Explore the data to understand what it is made of. What are the columns names? What do they represent?

2. What is the data type of each column?
Is this consistent? If not, fix it.

1. What is the mean cost of a taxi ride in NY?

2. Make histograms for each column of the dataframe.

3. From a web search, find the latitude and longitude of New-York.    
Is this consistent with what you can see in the data?

1. What are the min and max of `pickup_longitude`, `pickup_latitude`, `dropoff_longitude`, `dropoff_latitude`?
Does that seem consistent with a taxi ride within the city?    
Select data that have longitude between (-74.3, -73.7) and latitudes between (40.5, 40.9). We use only this data for the rest of the project.

1. Is there some inconsistent or missing data?   
Explain what and why.
Remove it.


### B. Data visualisation

- Make a scatter plot of the pickup locations
- Make a scatter plot of the dropoff locations
- plot on top of the NY map


### C. Data engineering

1. What do you think would be the most powerful feature to predict a taxi fare?

2. Propose a way to compute that feature (use the web). Compute it.

3. Plot the relation between that feature and the taxi fares.    
Does it still seem like a good feature?
By eye, what is the cost of a 10km ride?

## Part 2 - Machine Learning

This part will start with an introduction to machine learning.

1. Make a linear regression the taxi fare from that feature.
You can use the `LinearRegression` function:
```
from sklearn.linear_model import LinearRegression
```

What is the prediction of the linear regressor for a 10km ride?

2. Plot that linear regression on top of the scatter plot

3. Train Random Forests

4. Propose a way to compute the performance of the Random Forests model

5. Compare the performance of the linear regression and the Random Forests model



## Appendix

### Useful functions

```
def display_ny_map():
    nyc_map_zoom = plt.imread('NY_taxi_fare/nyc_-74.3_-73.7_40.5_40.9.png')
    BB = (-74.3, -73.7, 40.5, 40.9)
    ax = plt.imshow(nyc_map_zoom, zorder=0, extent=BB)
    return ax.axes
```

```
def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(np.deg2rad, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arcsin(np.sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r
 ```

1. Make a linear regression the taxi fare from that feature
