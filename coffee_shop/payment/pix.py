from .payment_strategy import PaymentStrategy

class PixPayment(PaymentStrategy):
    def pay(self, amount: float) -> str:
        return f"Pagamento de R${amount:.2f} realizado via Pix!"
