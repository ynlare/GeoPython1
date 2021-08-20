#!/usr/bin/env python
# coding: utf-8

# In[1]:


import folium


# In[2]:


worldmap = folium.Map()
worldmap


# In[3]:


# Canada's Geolocation (default style)
worldmap = folium.Map(location = [50.130,-106.35],zoom_start = 4)
worldmap


# In[4]:


# Canada's Geolocation ( Stamen Toner style)
worldmap = folium.Map(location = [56.130,-106.35],zoom_start = 4 )
worldmap


# In[5]:


# Canada's Geolocation ( Stamen Toner style)
worldmap = folium.Map(location = [56.130,-106.35],zoom_start = 4, tiles ='Stamen Toner')
worldmap


# In[6]:


# Canada's Geolocation ( Stamen Terrain style)
worldmap = folium.Map(location = [56.130,-106.35],zoom_start = 4, tiles ='Stamen Terrain')
worldmap


# In[ ]:




