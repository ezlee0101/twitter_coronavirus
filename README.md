# Coronavirus twitter analysis

This project uses MapReduce to analyze all tweets related to Covid19 by country and language by processing geotagged tweets from a large-scale dataset in 2020. 

**Learning Objectives:**

1. work with large scale datasets
1. work with multilingual text
1. use the MapReduce divide-and-conquer paradigm to create parallel code

## Background

### 1. Mapping Tweets
```map.py``: takes geolocation information from tweets and plot them on a map to visualize where tweets are coming from
Extracted outputs from hashtags : .country and .lang files

### 2. Reduce
```reduce.py``: takes these intermediate outputs and aggregates them

### 3. Visualize
```visualize.py```: creates bar graphs and determines whether the visualization is for countries or languages based on the key
```alternativ_reduce.py```: creates a line graph representing hashtag trends over time


## Final Product

**Count of #coronavirus by language**
![Count of #coronavirus by language] (visualizations/combined.countryry#coronavirus.png)

**Count of #coronavirus by country**
![Count of #coronavirus by country] (visualizations/combined.lang#coronavirus.png)

**Count of #
