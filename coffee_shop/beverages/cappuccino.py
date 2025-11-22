from .beverage import Beverage

class Cappuccino(Beverage):
    def cost(self) -> float:
        return 8.0

    def description(self) -> str:
        return "Cappuccino"
