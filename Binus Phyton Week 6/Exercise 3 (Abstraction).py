from abc import ABC, abstractmethod

# Abstract Class
class PaymentMethod(ABC):
  @abstractmethod
  def pay(self, amount):
    pass

# Concrete Class 1
class CreditCard(PaymentMethod):
  def pay(self, amount):
    print(f"Paid ${amount} using Credit Card")

# Concrete Class 2
class EBanking(PaymentMethod):
  def pay(self, amount):
    print(f"Paid ${amount} using E-Banking")

payments = [CreditCard(), EBanking()]

for payment in payments:
    payment.pay(50)