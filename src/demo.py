from shapely.geometry import Polygon 
from spatial import Point, Parcel


# p1 = Point("P1", 121.0, 14.6) 
# print(p1.id, p1.geometry.x, p1.geometry.y)

# point_tuple = p1.to_tuple()
# print(point_tuple)

# p2 = Point("P1", 121.4, 14.23)
# print(f"Point {p1.id} is {p1.distance_to(p2)} degrees to {p2.id}.")


# p = Point("A", 121.0, 14.6) 
# print("BBox:", p.bbox()) 
# print("Tuple:", p.to_tuple())


# a simple rectangle polygon sample 
geom = Polygon([ 
        (0, 0), 
        (10, 0), 
        (10, 5), 
        (0, 5) 
    ])

# Dictionary for added structure 
attrs = { 
        "area": 50.0, 
        "zone": "Residential", 
        "is_active": True 
    } 
parcel = Parcel(parcel_id=101, geometry=geom, attributes=attrs) 
print("Parcel BBox:", parcel.bbox())
print("Parcel Zone:", parcel.attributes["zone"])