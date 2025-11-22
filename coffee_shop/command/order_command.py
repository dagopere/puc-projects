from .command import Command

class OrderCommand(Command):
    def __init__(self, beverage, subject, payment_strategy):
        self.beverage = beverage
        self.subject = subject
        self.payment_strategy = payment_strategy

    def execute(self):
        total = self.beverage.cost()
        # Notifica que o pedido está sendo processado
        self.subject.notify(f"Executando pedido: {self.beverage.description()} — Total R${total:.2f}")
        result = self.payment_strategy.pay(total)
        self.subject.notify(f"Pagamento: {result}")
        return result

class OrderInvoker:
    def __init__(self):
        self.history = []

    def execute_command(self, command: OrderCommand):
        res = command.execute()
        self.history.append((command, res))
        return res
