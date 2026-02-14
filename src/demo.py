from spatial import Point 

p1 = Point("P1", 121.0, 14.6) 
print(p1.id, p1.geometry.x, p1.geometry.y)

point_tuple = p1.to_tuple()
print(point_tuple)

p2 = Point("P1", 121.4, 14.23)
print(f"Point {p1.id} is {p1.distance_to(p2)} degrees to {p2.id}.")
