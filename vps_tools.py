#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Mean depth of tagged JWS equipped with depth sensors, recorded within the array
import numpy as np

def mean_depth(depth_array):
    '''Calculate the mean depth of a shark within the array
    depth array: array of shark depth observations
    mean_d: mean depth'''
    mean_d = np.mean(depth_array)
    return mean_d


# In[5]:


#Residency Index of detections and total days of the array deployment
def residency_index(detection_days, monitored_days):
    '''Calculating residency index based detection data and total days of array deployment
    parameters:
    detection_days: the number of detection in a day from an individual shark
    monitored_days: the total number of monitored days the VPS array was deployed
    return:
    RI: residency index, from 0 to 1'''
    RI = detection_days / monitored_days
    return RI

