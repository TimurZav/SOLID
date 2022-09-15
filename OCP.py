# Violation of OCP


# class Discount:
#     """Demo customer discount class"""
#     def __init__(self, customer, price):
#         self.customer = customer
#         self.price = price
#
#     def give_discount(self):
#         """A discount method"""
#         if self.customer == 'normal':
#             return self.price * 0.2
#         elif self.customer == 'vip':
#             return self.price * 0.4


# Solution:


class Discount:
    """Demo customer discount class"""
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def get_discount(self):
        """A discount method"""
        return self.price * 0.2


class VIPDiscount(Discount):
    """Demo VIP customer discount class"""
    def get_discount(self):
        """A discount method"""
        return super().get_discount() * 2


class SuperVIPDiscount(VIPDiscount):
    """Demo super vip customer discount class"""
    def get_discount(self):
        """A discount method"""
        return super().get_discount() * 2
