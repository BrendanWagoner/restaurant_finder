class Effiel:
pass
# Restaurant Finder

## Overview

Restaurant Finder lets you input Name or Address of your current location, and will find you the first restaurant in a 1500 radius. It will then give you the name, rating, and directions to get there.

## Usage

```python
# input
"""Enter a location: Effiel Tower"""

# output should look like this
"""
The restaurant Jules Verne is a great choice with a rating of 4.3.

Head north on Quai Branly toward Pont dIéna
Merge onto Quai Branly
Make a U-turn at Prom. dAustralie Destination will be on the right

"""
```

## Licensing

This project is using two Google Rest APIs:
Places API, and Directions API. you will need to supply your own Google Authorization Key, and input yours through os.environ. 

## Authors and Contributors

Brendan Wagoner, and Jeremy Rodrigues

## Project Status

Working on this project weekly, now can enter any location and recieve a response. 