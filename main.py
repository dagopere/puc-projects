from factory.beverage_factory import BeverageFactory
from beverages.decorators import Milk, Chocolate, WhippedCream
from payment.pix import PixPayment
from payment.card import CardPayment
from observer.subject import Subject
from observer.observers import ConsoleNotifier, LoggerNotifier
from command.order_command import OrderCommand, OrderInvoker

def demo():
    factory = BeverageFactory()
    notifier = Subject()
    notifier.attach(ConsoleNotifier())
    notifier.attach(LoggerNotifier())

    # Cria um pedido: café com leite, chocolate e chantilly
    pedido = factory.create("coffee")
    pedido = Milk(pedido)
    pedido = Chocolate(pedido)
    pedido = WhippedCream(pedido)

    total = pedido.cost()
    notifier.notify(f"Pedido pronto: {pedido.description()} — Total R${total:.2f}")

    # Pagamento via Pix
    pix = PixPayment()
    print(pix.pay(total))

    # Outro pedido usando Card
    pedido2 = factory.create("cappuccino")
    from beverages.decorators import Milk
    pedido2 = Milk(pedido2)
    total2 = pedido2.cost()

    card = CardPayment(card_number="1234-****-****-5678")
    print(card.pay(total2))

    # Usando Command para executar um pedido
    invoker = OrderInvoker()
    cmd = OrderCommand(pedido2, notifier, card)
    invoker.execute_command(cmd)

if __name__ == '__main__':
    demo()
