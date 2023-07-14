#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

data=pd.read_csv("Banknote-authentication-dataset-.csv")
data


# In[2]:


V1d=data['V1']
V2d=data['V2']

V1_mean=np.mean(V1d)
print("the mean is " + str(V1_mean))

V1_std = np.std(V1d)
print("the std is " + str(V1_std))

V1_max = V1d.max()
print("the max is " + str(V1_max))

V1_min=V1d.min()
print("the min is " + str(V1_min))


# In[3]:


V2_mean=np.mean(V2d)
print("the mean is " + str(V2_mean))

V2_std = np.std(V2d)
print("the std is " + str(V2_std))

V2_max = V2d.max()
print("the max is " + str(V2_max))

V2_min=V2d.min()
print("the min is " + str(V2_min))


# In[4]:


import matplotlib.pyplot as plt

plt.xlabel('V1')
plt.ylabel('V2')
plt.scatter(V1d,V2d)


# In[9]:


from sklearn.cluster import KMeans

import seaborn as sns; sns.set()

V1_V2 = np.column_stack((V1d,V2d))

km_res = KMeans(n_clusters=3,n_init=50).fit(V1_V2)

clusters=km_res.cluster_centers_
y_kmeans = km_res.predict(V1_V2)

plt.scatter(V1d,V2d,c=y_kmeans,cmap='viridis')
plt.scatter(clusters[:,0],clusters[:,1],s=100)
plt.xlabel('V1')
plt.ylabel('V2')

data['kmean'] = km_res.labels_
data['kmean'].value_counts()


# In[ ]:




