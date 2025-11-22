from .beverage import Beverage

class Latte(Beverage):
    def cost(self) -> float:
        return 7.0

    def description(self) -> str:
        return "Latte"
