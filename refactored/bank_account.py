class BankAccount():
    def __init__(self, owner:str, account:int, balance_account:float):
        self._owner = owner
        self.account = account
        self._balance_account = balance_account

    def __str__(self):
        return self.account

    @property
    def owner(self):
        return print(self._owner)

    @owner.setter
    def owner(self, new_owner):
        if(type(new_owner) == type(str())):
            self._owner = new_owner
        else:
            return print("The owner must be type(str)")

    @property
    def balance_account(self):
        return print(f"Balance account = R${self._balance_account:.2f}")

    @balance_account.setter
    def balance_account(self, value):
        if(type(value) == type(int())):
            self._balance_account = value
        else:
            print("The value must be type(int) or type(float)")

    def set_deposit(self, account):
        if(account.account != self.account):

            value = float(input("Enter the value for to transfer: "))

            if(value <= self._balance_account):
                self._balance_account = self._balance_account - value
                account._balance_account = account._balance_account + value
                return print(f"Balance account = R${self._balance_account:.2f}")

            else:
                return print("The balance account aren't suficient.")

        else:
            return print("You must be enter a diferent account.")