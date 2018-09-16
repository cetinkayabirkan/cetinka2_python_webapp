#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas
import seaborn as sns
from datetime import datetime
matplotlib.use('TkAgg')


flightsall = pandas.read_csv('flights.csv')
#frames = ['CANCELLATION_REASON']
flights = flightsall.drop('CANCELLATION_REASON',1)
flights = flights.fillna(0)
airports = pandas.read_csv('airports.csv')
#airports = airports.dropna()
airlines = pandas.read_csv('airlines.csv')
#airlines = airlines.dropna()
cancbool = flights['CANCELLED'] == 1
cancflights = flights[cancbool]


# In[2]:


flights.head(3)


# In[3]:


airports.head(3)


# In[4]:


airlines.head(13)


# In[191]:


flights['AIRPORT_TOTAL_DELAYS'] =  flights ['SECURITY_DELAY'] + flights['AIR_SYSTEM_DELAY'] +flights['WEATHER_DELAY'] 
flights['AIRLINE_TOTAL_DELAYS']  = flights ['AIRLINE_DELAY'] + flights['LATE_AIRCRAFT_DELAY']
flights['TOTAL_WEATHER_DELAY'] = flights ['AIR_SYSTEM_DELAY'] + flights['WEATHER_DELAY']

UAbool = flights['AIRLINE'] == 'UA'
UnAir = flights[UAbool]

AAbool = flights['AIRLINE'] == 'AA'
AmAir = flights[AAbool]
DLbool = flights['AIRLINE'] == 'DL'
Delta = flights[DLbool]
SWbool = flights['AIRLINE'] == 'WN'
SoWe = flights[SWbool]

Subool = flights['DAY_OF_WEEK'] == 1
Mbool = flights['DAY_OF_WEEK'] == 2
Tubool = flights['DAY_OF_WEEK'] == 3
Wbool = flights['DAY_OF_WEEK'] == 4
Thbool = flights['DAY_OF_WEEK'] == 5
Fbool = flights['DAY_OF_WEEK'] == 6
Sabool = flights['DAY_OF_WEEK'] == 7

Sunday = flights[Subool]
Monday = flights[Mbool]
Tuesday = flights[Tubool]
Wednesday = flights[Wbool]
Thursday = flights[Thbool]
Friday = flights[Fbool]
Saturday = flights[Sabool]

ORDOAPb = flights['ORIGIN_AIRPORT'] == 'ORD'
ATLOAPb = flights['ORIGIN_AIRPORT'] == 'ATL'
LAXOAPb = flights['ORIGIN_AIRPORT'] == 'LAX'
DFWOAPb = flights['ORIGIN_AIRPORT'] == 'DFW'
JFKOAPb = flights['ORIGIN_AIRPORT'] == 'JFK'
DENOAPb = flights['ORIGIN_AIRPORT'] == 'DEN'
SFOOAPb = flights['ORIGIN_AIRPORT'] == 'SFO'
LASOAPb = flights['ORIGIN_AIRPORT'] == 'LAS'
CLTOAPb = flights['ORIGIN_AIRPORT'] == 'CLT'
SEAOAPb = flights['ORIGIN_AIRPORT'] == 'SEA'

ORDDAPb = flights['DESTINATION_AIRPORT'] == 'ORD'
ATLDAPb = flights['DESTINATION_AIRPORT'] == 'ATL'
LAXDAPb = flights['DESTINATION_AIRPORT'] == 'LAX'
DFWDAPb = flights['DESTINATION_AIRPORT'] == 'DFW'
JFKDAPb = flights['DESTINATION_AIRPORT'] == 'JFK'
DENDAPb = flights['DESTINATION_AIRPORT'] == 'DEN'
SFODAPb = flights['DESTINATION_AIRPORT'] == 'SFO'
LASDAPb = flights['DESTINATION_AIRPORT'] == 'LAS'
CLTDAPb = flights['DESTINATION_AIRPORT'] == 'CLT'
SEADAPb = flights['DESTINATION_AIRPORT'] == 'SEA'

ORDOAP = flights[ORDOAPb]
ATLOAP = flights[ATLOAPb]
LAXOAP = flights[LAXOAPb]
DFWOAP = flights[DFWOAPb]
JFKOAP = flights[JFKOAPb]


ORDDAP = flights[ORDDAPb]
ATLDAP = flights[ATLDAPb]
LAXDAP = flights[LAXDAPb]
DFWDAP = flights[DFWDAPb]
JFKDAP = flights[JFKDAPb]


# In[170]:


sns.boxenplot(flights['AIRLINE_TOTAL_DELAYS'])
print(np.mean(flights['AIRLINE_TOTAL_DELAYS']))


# In[171]:


sns.boxenplot(flights['AIRPORT_TOTAL_DELAYS'])
print(np.mean(flights['AIRPORT_TOTAL_DELAYS']))


# In[183]:


print(np.mean(UnAir['AIRLINE_TOTAL_DELAYS']))
print(np.mean(AmAir['AIRLINE_TOTAL_DELAYS']))
print(np.mean(Delta['AIRLINE_TOTAL_DELAYS']))
print(np.mean(SoWe['AIRLINE_TOTAL_DELAYS']))


# In[185]:


print(np.mean(ORDOAP['AIRPORT_TOTAL_DELAYS']))
print(np.mean(JFKOAP['AIRPORT_TOTAL_DELAYS']))
print(np.mean(LAXOAP['AIRPORT_TOTAL_DELAYS']))
print(np.mean(DFWOAP['AIRPORT_TOTAL_DELAYS']))
print(np.mean(ATLOAP['AIRPORT_TOTAL_DELAYS']))


# In[188]:


print(np.mean(ORDOAP['AIR_SYSTEM_DELAY']))
print(np.mean(JFKOAP['AIR_SYSTEM_DELAY']))
print(np.mean(LAXOAP['AIR_SYSTEM_DELAY']))
print(np.mean(DFWOAP['AIR_SYSTEM_DELAY']))
print(np.mean(ATLOAP['AIR_SYSTEM_DELAY']))


# In[199]:


sns.violinplot(JFKOAP['TOTAL_WEATHER_DELAY'])
print(np.mean(JFKOAP['TOTAL_WEATHER_DELAY']))
plt.xlim(-25, 90)


# In[198]:


sns.violinplot(ORDOAP['TOTAL_WEATHER_DELAY'])
print(np.mean(ORDOAP['TOTAL_WEATHER_DELAY']))
plt.xlim(-25, 90)


# In[71]:


dims = (18,12)
fig, ax = plt.subplots(figsize = dims)
sns.distplot(ORDOAP['DEPARTURE_DELAY'], label = 'ORD')
sns.distplot(ATLOAP['DEPARTURE_DELAY'], label = 'ATL')
sns.distplot(LAXOAP['DEPARTURE_DELAY'], label = 'LAX')
sns.distplot(DFWOAP['DEPARTURE_DELAY'], label = 'DFW')
sns.distplot(JFKOAP['DEPARTURE_DELAY'], label = 'JFK')

plt.legend()


# In[103]:


airline = SoWe
print(np.mean(airline['AIRLINE_DELAY']))
print(np.std(airline['AIRLINE_DELAY']))


# In[146]:



dims = (18,12)
fig, ax = plt.subplots(figsize = dims)
sns.violinplot(ORDOAP['WEATHER_DELAY'])
plt.xlim(-25,100)
print(np.mean(ORDOAP['WEATHER_DELAY']))


# In[147]:


dims = (18,12)
fig, ax = plt.subplots(figsize = dims)
sns.violinplot(LAXOAP['WEATHER_DELAY'])
plt.xlim(-25,100)
print(np.mean(LAXOAP['WEATHER_DELAY']))


# In[148]:


dims = (18,12)
fig, ax = plt.subplots(figsize = dims)
sns.violinplot(DFWOAP['WEATHER_DELAY'])
plt.xlim(-25,100)
print(np.mean(DFWOAP['WEATHER_DELAY']))


# In[149]:


dims = (18,12)
fig, ax = plt.subplots(figsize = dims)
sns.violinplot(JFKOAP['WEATHER_DELAY'])
plt.xlim(-25,100)
print(np.mean(JFKOAP['WEATHER_DELAY']))


# In[150]:


dims = (18,12)
fig, ax = plt.subplots(figsize = dims)
sns.violinplot(ATLOAP['WEATHER_DELAY'])
plt.xlim(-25,100)
print(np.mean(ATLOAP['WEATHER_DELAY']))


# In[110]:


np.mean(ORDOAP['WEATHER_DELAY'])


# In[81]:


airport = JFKOAP
print(np.mean(airport['DEPARTURE_DELAY']))
print(np.std(airport['DEPARTURE_DELAY']))


# In[ ]:





# In[82]:


dims = (18,12)
fig, ax = plt.subplots(figsize = dims)
sns.distplot(ORDDAP['ARRIVAL_DELAY'], label = 'ORD')
sns.distplot(ATLDAP['ARRIVAL_DELAY'], label = 'ATL')
sns.distplot(LAXDAP['ARRIVAL_DELAY'], label = 'LAX')
sns.distplot(DFWDAP['ARRIVAL_DELAY'], label = 'DFW')
sns.distplot(JFKDAP['ARRIVAL_DELAY'], label = 'JFK')

plt.legend()


# In[87]:


OAP = [ORDOAP, ATLOAP, LAXOAP, DFWOAP, JFKOAP]
DAP = [ORDDAP, ATLDAP, LAXDAP, DFWDAP, JFKDAP]
print(np.mean(airport['DEPARTURE_DELAY']))
print(np.std(airport['DEPARTURE_DELAY']))


# In[89]:


sns.boxplot (ORDOAP['DEPARTURE_DELAY'])


# In[37]:


#UnAirArrDel = UnAir.dropna('ARRIVAL_DELAY')
UnAir.head(2)
Sunday.head(2)


# In[7]:


dims = (18,12)
fig, ax = plt.subplots(figsize = dims)
sns.distplot(UnAir['DEPARTURE_DELAY'], ax = ax, label = 'UA')
sns.distplot(AmAir['DEPARTURE_DELAY'], ax = ax, label = 'AA')
sns.distplot(Delta['DEPARTURE_DELAY'], ax = ax, label = 'DL')
sns.distplot(SoWe['DEPARTURE_DELAY'], ax = ax, label = 'SW')
plt.legend()


# In[8]:


dims = (18,12)
fig, ax = plt.subplots(figsize = dims)
sns.distplot(UnAir['ARRIVAL_DELAY'], ax = ax, label = 'UA')
sns.distplot(AmAir['ARRIVAL_DELAY'], ax = ax, label = 'AA')
sns.distplot(Delta['ARRIVAL_DELAY'], ax = ax, label = 'DL')
sns.distplot(SoWe['ARRIVAL_DELAY'], ax = ax, label = 'SW')
plt.legend()


# In[9]:


print(np.mean(SoWe['ARRIVAL_DELAY']))
print(np.std(SoWe['ARRIVAL_DELAY']))


# In[40]:


dims = (18,12)
fig, ax = plt.subplots(figsize = dims)
sns.distplot(Sunday['DEPARTURE_DELAY'], ax = ax, label = 'Sun')
sns.distplot(Monday['DEPARTURE_DELAY'], ax = ax, label = 'Mon')
sns.distplot(Tuesday['DEPARTURE_DELAY'], ax = ax, label = 'Tue')
sns.distplot(Wednesday['DEPARTURE_DELAY'], ax = ax, label = 'Wed')
sns.distplot(Thursday['DEPARTURE_DELAY'], ax = ax, label = 'Thur')
sns.distplot(Friday['DEPARTURE_DELAY'], ax = ax, label = 'Fri')
sns.distplot(Saturday['DEPARTURE_DELAY'], ax = ax, label = 'Sat')

plt.legend()


# In[49]:


day = Saturday
print(np.mean(day['DEPARTURE_DELAY']))
print(np.std(day['DEPARTURE_DELAY']))


# In[50]:


dims = (18,12)
fig, ax = plt.subplots(figsize = dims)
sns.distplot(Sunday['ARRIVAL_DELAY'], ax = ax, label = 'Sun')
sns.distplot(Monday['ARRIVAL_DELAY'], ax = ax, label = 'Mon')
sns.distplot(Tuesday['ARRIVAL_DELAY'], ax = ax, label = 'Tue')
sns.distplot(Wednesday['ARRIVAL_DELAY'], ax = ax, label = 'Wed')
sns.distplot(Thursday['ARRIVAL_DELAY'], ax = ax, label = 'Thur')
sns.distplot(Friday['ARRIVAL_DELAY'], ax = ax, label = 'Fri')
sns.distplot(Saturday['ARRIVAL_DELAY'], ax = ax, label = 'Sat')

plt.legend()


# In[58]:


day = Saturday
print(np.mean(day['ARRIVAL_DELAY']))
print(np.std(day['ARRIVAL_DELAY']))


# In[19]:


plt.scatter(UnAir['DAY_OF_WEEK'],UnAir['ARRIVAL_DELAY'])


# In[20]:


sns.boxplot (y = UnAir['ARRIVAL_DELAY'], x = UnAir['DAY_OF_WEEK'])


# In[21]:


plt.scatter(AmAir['DEPARTURE_DELAY'],AmAir['ARRIVAL_DELAY'])


# In[22]:


plt.scatter(SoWe['DEPARTURE_DELAY'],SoWe['ARRIVAL_DELAY'])


# In[23]:


plt.scatter(Delta['DEPARTURE_DELAY'],Delta['ARRIVAL_DELAY'])


# In[ ]:




