from .payment_strategy import PaymentStrategy

class CashPayment(PaymentStrategy):
    def pay(self, amount: float) -> str:
        return f"Pagamento de R${amount:.2f} em dinheiro (pagar na entrega)."
