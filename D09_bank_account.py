class BankAccount:
    def __init__(self, id, pin, name):
        self.name = name
        self._id = id
        self.__pin = pin

    def get_pin(self):
        return self.__pin

    def set_pin(self, pin):
        self.__pin = pin


bank_account = BankAccount(111, 1234, "Ivan")
print(bank_account._BankAccount__pin)  # accessing private member - possible, but should not be done! Name moungling
print(bank_account._id)
# print(bank_account.__pin)

bank_account.set_pin(2222)
print(bank_account.get_pin())
