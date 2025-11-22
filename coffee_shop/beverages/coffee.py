from .beverage import Beverage

class Coffee(Beverage):
    def cost(self) -> float:
        return 5.0

    def description(self) -> str:
        return "Café simples"
