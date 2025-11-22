from .payment_strategy import PaymentStrategy

class CardPayment(PaymentStrategy):
    def __init__(self, card_number: str):
        self.card_number = card_number

    def pay(self, amount: float) -> str:
        # Simula validação de cartão
        return f"Pagamento de R${amount:.2f} cobrado no cartão {self.card_number}."
