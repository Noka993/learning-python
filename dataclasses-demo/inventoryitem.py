from dataclasses import dataclass, field

@dataclass
class InventoryItem:
    """Class for keeping track of an item in inventory."""
    name: str
    unit_price: float
    quantity_on_hand: int = 0
    sizes: list[str] = field(default_factory=list, init=False)
        
    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand
    
    # def __init__(self, name: str, unit_price: float, quantity_on_hand: int = 0):
    #     self.name = name
    #     self.unit_price = unit_price
    #     self.quantity_on_hand = quantity_on_hand
    
def func(lst=[]):
    lst.append(1)
    print(lst)
    
func()
func()