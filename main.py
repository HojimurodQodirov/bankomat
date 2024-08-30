class Bankomat:
    def __init__(self, balance=0):
        self.balance = balance

    def pilus(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"shuncha pul soldingiz {amount} . hozirgi balans: {self.balance}.")

    def minus(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"shuncha pul echdingiz: {amount} . hozirgi balans: {self.balance}.")
            else:
                print(f"balansda pul kam: {self.balance}.")

    def check_balance(self):
        print(f" hozirgi balans: {self.balance}.")

client = Bankomat()

client.pilus(1000)

client.minus(500)

client.check_balance()
