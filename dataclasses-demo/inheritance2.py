from dataclasses  import dataclass

@dataclass
class Rectangle:
    length: int
    width: int
        
@dataclass
class ColoredRectangle(Rectangle):
    color: str

rect = ColoredRectangle(10, 10, "green")