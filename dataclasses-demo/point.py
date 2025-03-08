from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
    
# __init__
# __repr__
# __eq___ 

p = Point(1, 2)
p2 = Point(1, 2)
print(p)
print(p == p2)