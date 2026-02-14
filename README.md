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

### Challenge Exercises

1. Why should from_dict() delegate validation to the constructor instead of validating manually inside the method?

- Placing the validation in the constructor makes it so that validation is applied to all methods calling the class constructor and not just to the from_dict method.

2. Why is as_dict() implemented inside the object rather than in demo.py or run_lab3.py?

- Placing the as_dict code inside the class makes the code tied to the class instead of the script importing the class. This makes the as_dict code reusable for all scripts importing the class.

3. Why must as_dict() return only primitive data types and not Shapely geometry objects?

- For our case, we wanted to return a dictionary representation of the object we have. We do not care what library that object needed to construct the dictionary. If we replaced the Shapely library for representing the geometry of our object, the response of the as_dict method will still be the same.

4. Why does intersects() belong in the base class instead of being duplicated in Point and Parcel?

- The intersects method is placed on the SpatialObject base class since its computation needs the state of the base class and the method is used by both the Point and Parcel class. Placing the method in the base class makes it so that we do not have to duplicate the code.

5. If you add a new spatial subclass tomorrow (e.g., Building), what changes are required for it to support intersects() — and why?

- Since intersects method of SpatialObject only needs the geometry of the instance object and compares it to another object with geometry, for a Building class to support intersects, it needs to inherit from SpatialObject making the Building class have a geometry state.
