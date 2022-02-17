# surfs_up challenge

## Overview of the statistical analysis:

While gathering information on weather data in relation to opening an ice cream shop, we wanted to look further into the average temperatures for both June and Decemeber in Oahu. Performing this analysis will help determine if the surf and ice cream shop business is sustainable year-round.

## Results:

Three key differnece in weather between June and December:
- The count of temperatures in June is slighlty higher than December. June had 1,700 counts of temperature while December had 1,517. 
- The minimum temperature between June and December have a 8 degree difference. June's minimum temperature is 64 degrees while December's is 56 degrees. 
- The max temperature was only off by 2 degrees. For June the max temperature is 85 and for December the max temperature is 83.

## Summary:

In conclusion, I would want to gather the same count of temperature data to get a more accurate picture but with the analysis we have currently I can say that the weather is on average warm enough for year-round ice cream sales. The mean temperature for June is  74.9 degrees and for December it is only three degrees less at 71 degrees. 

Two additional queries we could perform is to see weather in spring and autumn for a comprehensive year-round weather analysis. I would choose April and October months and the queries would look like the following:

Spring (April):
```
april_str = "04"
april_results = session.query(Measurement.date, Measurement.tobs).\
    filter(func.strftime("%m", Measurement.date) == apr_str).all()
```

Fall (October):
```
oct_str = "10"
oct_results = session.query(Measurement.date, Measurement.tobs).\
    filter(func.strftime("%m", Measurement.date) == oct_str).all()
```   
