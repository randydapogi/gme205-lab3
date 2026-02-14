# GmE 205 – Laboratory Exercise 3

## Overview

GmE 205 Lab Exercise 3

---

## Environment Setup

- Python 3.x

---

## How to Run

1. Activate the virtual environment

---

## Outputs

---

## Reflection

### Refactor Point to Use Shapely

1. What changed in the internal representation of Point?

- Instead of storing the coordinate of the Point object as lat and lon, we used the shapely library Point object to represent the geomtry of our Point class.

2. What did not change in the external behavior?

- We still initialize a Point object the same way by providing id, lat and lon. We also still expect the same output for the instance method to_tuple and distance_to. One thing to consider for distance_to is because we initialize Shapely Point with degrees as coordinates, the distance that is returned by the distance_to method is in degrees and not in meters.

3. Where does spatial computation now live?

- Spatial computation now live in the Point object of shapely.
