from shapely.geometry import Polygon 
from spatial import Point, Parcel

# # Challenge 1
# print("Challenge 1")
# row1 = {"id": "A", "lon": 121.0, "lat": 14.6, "name": "Gate", "tag": "POI"}
# row2 = {"id": "B", "lon": 999, "lat": 14.6, "name": "Gate", "tag": "POI"}

# p1 = Point.from_dict(row1)
# print(p1)
# p2 = Point.from_dict(row2)
# print(p2)


# # Challenge 2
# print("\n\nChallenge 2")
# point_row = {"id": "A", "lon": 121.0, "lat": 14.6, "name": "Gate", "tag": "POI"}
# point = Point.from_dict(point_row)
# print(point.as_dict())

# attrs = { 
#         "area": 50.0, 
#         "zone": "Residential", 
#         "is_active": True 
#     } 
# geom = Polygon([ 
#         (0, 0), 
#         (10, 0), 
#         (10, 5), 
#         (0, 5) 
#     ])
# parcel = Parcel(parcel_id=101, geometry=geom, attributes=attrs) 
# print(parcel.as_dict())


# Challenge 3
print("\n\nChallenge 3")
attrs = { 
        "area": 50.0, 
        "zone": "Residential", 
        "is_active": True 
    } 
geom = Polygon([ 
        (121, 14), 
        (122, 14), 
        (122, 15), 
        (121, 15) 
    ])
parcel = Parcel(parcel_id=101, geometry=geom, attributes=attrs) 

inside_point = Point.from_dict({"id": "A", "lon": 121.5, "lat": 14.6, "name": "Inside", "tag": "POI"})
outside_point = Point.from_dict({"id": "A", "lon": 120.5, "lat": 13.6, "name": "Outside", "tag": "POI"})
print(f"Point Name: {inside_point.name}   Intersects Parcel: {str(inside_point.intersects(parcel))}")
print(f"Point Name: {outside_point.name}   Intersects Parcel: {str(outside_point.intersects(parcel))}")