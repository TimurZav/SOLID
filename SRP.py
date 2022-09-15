# Violation of SRP


# class Account:
#
#     def __init__(self, account_no: str):
#         self.account_no = account_no
#
#     def get_account_number(self):
#         return self.account_no
#
#     def save(self):
#         pass


# Solution

class AccountDB:
    """Account DB management class """

    def get_account_number(self, _id):
        """Get account number"""
        pass

    def account_save(self, obj):
        """Save account number into DB"""
        pass


class Account:
    """Demo bank account class """

    def __init__(self, account_no: str):
        self.account_no = account_no
        self._db = AccountDB()

    def get_account_number(self):
        """Get account number"""
        return self.account_no

    def get(self, _id):
        """
        :param _id:
        :return:
        """
        return self._db.get_account_number(_id=_id)

    def save(self):
        """account save"""
        self._db.account_save(obj=self)
