class bank:
    def transaction(self):
        print("tranction done")
    def deposit(self):
        print("deposit done")
    def account_opening(self):
        print("account oppening satus")
class hdfc_bank(bank):
    def hdfc_to_icici(self):
        print("transaction from hdfc to icici")

class icici_bank(hdfc_bank):
    pass

i=icici_bank()
i.transaction()
i.deposit()
i.hdfc_to_icici()
i.account_opening()