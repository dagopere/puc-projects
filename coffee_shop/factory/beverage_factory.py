from beverages.coffee import Coffee
from beverages.latte import Latte
from beverages.cappuccino import Cappuccino

class BeverageFactory:
    def create(self, drink_type: str):
        mapping = {
            "coffee": Coffee,
            "latte": Latte,
            "cappuccino": Cappuccino
        }
        cls = mapping.get(drink_type.lower())
        if cls is None:
            raise ValueError(f"Tipo de bebida desconhecido: {drink_type}")
        return cls()
