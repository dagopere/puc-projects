from .beverage import Beverage

class BeverageDecorator(Beverage):
    def __init__(self, beverage: Beverage):
        self._beverage = beverage

class Milk(BeverageDecorator):
    def cost(self) -> float:
        return self._beverage.cost() + 1.5

    def description(self) -> str:
        return self._beverage.description() + " + leite"

class Chocolate(BeverageDecorator):
    def cost(self) -> float:
        return self._beverage.cost() + 2.0

    def description(self) -> str:
        return self._beverage.description() + " + chocolate"

class WhippedCream(BeverageDecorator):
    def cost(self) -> float:
        return self._beverage.cost() + 2.5

    def description(self) -> str:
        return self._beverage.description() + " + chantilly"
