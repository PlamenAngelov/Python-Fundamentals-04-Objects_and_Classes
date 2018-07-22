class BankAccount:
    def __init__(self, accountName, bank, accountBalance):
        self.accountName = accountName
        self.bank = bank
        self.accountBalance = accountBalance


data = input()

account_list = []

while data != "end":

    temp_list = list(map(str,data.split(" | ")))
    account = temp_list[1]
    bank = temp_list[0]
    balance = float(temp_list[2])
    account_list.append(BankAccount(account, bank, balance))
    data = input()


sorted_list = sorted(account_list, key = lambda BankAccount: (- BankAccount.accountBalance, len(BankAccount.bank)))

for item in sorted_list:
    print(f"{item.accountName} -> {item.accountBalance:.2f} ({item.bank})")