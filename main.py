class People():
    def __init__(self, name, age, identity, address):
        self.__name = name
        self.__age = age 
        self.__identity = identity
        self.__address = address

    def __str__(self):
        return self.__name

    def get_name(self):
        return print(self.__name)

class Bank_Account():
    def __init__(self, owner:str, account:int, balance_account:float):
        self.owner = owner
        self.account = account
        self.__balance_account = balance_account

    def __str__(self):
        return self.account

    def get_owner(self):
        return print(self.owner)

    def get_balance_account(self):
        return print(f"O seu saldo é de: R${self.__balance_account:.2f}")

    def set_deposit(self, account):

        value = float(input("Digite o valor que deseja tranferir: "))

        if(value <= self.__balance_account):
            self.__balance_account = self.__balance_account - value
            account.__balance_account = account.__balance_account + value
            return print(f"O seu saldo agora é de R${self.__balance_account:.2f}")

        else:
            return print("O saldo é insuficiente.")