


import pandas
from datetime import datetime
import numpy

from math import radians
from sklearn.metrics.pairwise import haversine_distances

dataset = pandas.read_csv("chicago_crime_2018.csv")
dataset = dataset.sample(frac=0.1).reset_index(drop=True)

#relative location, relative to police station

def get_haversine(x):
  lat1 = x['Latitude']
  long1 = x['Longitude']
  lat2 = 41.8889
  long2 = -87.6264
  loc1 =[radians(lat1), radians(long1)]
  loc2 =[radians(lat2), radians(long2)]
  return (haversine_distances([loc1, loc2])*6357000)[0][1]

#merge into data
#dataset['distance_from_downtoan']=dataset.apply(get_haversine, axis = 1)


print(dataset.apply(get_haversine, axis = 1))