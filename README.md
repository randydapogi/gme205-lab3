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

### Part B. Refactor Point to Use Shapely

1. What changed in the internal representation of Point?

- Instead of storing the coordinate of the Point object as lat and lon, we used the shapely library Point object to represent the geomtry of our Point class.

2. What did not change in the external behavior?

- We still initialize a Point object the same way by providing id, lat and lon. We also still expect the same output for the instance method to_tuple and distance_to. One thing to consider for distance_to is because we initialize Shapely Point with degrees as coordinates, the distance that is returned by the distance_to method is in degrees and not in meters.

3. Where does spatial computation now live?

- Spatial computation now live in the Point object of shapely.

### Part C. Designing a Spatial Hierarchy (Inheritance)

1. Why is SpatialObject considered an abstraction, and what real-world idea does it represent in your system?

- SpatialObject is considered an abstraction since all spatial state and functionality of Point and Parcel class is abstracted to them and placed in Spatial Object. This represents the idea that a more advance object can inheret properties from a primative object, like parcel and building both have primative property of footprint.

2. How does inheritance reduce duplication between classes like Point, Parcel, or Building?

- Since classes like Point, Parcel or Building will inherit the class of SpatialObject since they all have geometry, we can write all the method and calculations related to geometry for all the classes in one class SpatialObject instead of writing those same method and calculations on each class Point, Parcel or Building.

3. Why is storing parcel attributes in a dictionary a structural decision rather than a behavioral one?

- It is structural decision because we set the storage of attributes state with the structure of a dictionary with key value pair without considering the behaviour of the class with the attribute state.

4. If you add a new method (e.g., distance_to()) in SpatialObject, what happens to all subclasses — and why?

- Adding a new method to a class, SpatialObject, will add the same method to all its subclasses. This is because subclasses inherit all states and methods from its parent class.

5. How does this hierarchical design make your spatial system more scalable compared to defining each class independently?

- Hierarchical design makes it so that each class can have a contained set of states and responsibilities that are relevant to that class and that sets of states and methods that will be similar for multiple subclasses can be packaged to a class so that the state or method will not be duplicated and there is just one source of truth for the state or method of that class.
