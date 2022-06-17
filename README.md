
# Restaurant Finder

## Overview

Restaurant Finder lets you input your latitude and longitude, and will find you the first restaurant in a 1500 radius. It will then give you the name, rating, and directions to get there.

## Usage 

```python
my_lat = "48.8584"
my_long = "2.2945"


#output should look like this
"""
The restaurant Jules Verne is a great choice with a rating of 4.3.

Head northeast on Rue Jean Rey toward Av. de Suffren
"""
```

## Licensing

This project is using two Google Rest APIs:
Places API, and Directions API. you will need to supply your own Google Authorization Key, and input yours through os.environ. 

## Authors and Contributors

Brendan Wagoner, and Jeremy Rodrigues

## Project Status

Working on this project weekly, with goals to finish and have it work for any location.