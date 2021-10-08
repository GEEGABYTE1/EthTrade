import time 
from transaction import transaction



class Transaction_Script:
    created_transactions = [] 
    transaction = transaction

    def __init__(self):
        self.greeter()
        self.prompting()

    def greeter(self):
        print("\t"*5)
        print("To make a transaction: ")
        print('\n')
        time.sleep(0.5)
        print("/connect_chain")
        print("-"*15)
        time.sleep(0.5)
        print("/create_transaction")
        print("-"*15)
        time.sleep(0.5)
        print("/sign_transaction")
        print("-"*15)
        print("\t"*5)

    def prompting(self):
        while True:
            print("\n")
            prompt = str(input(':'))

            if prompt == '/connect_chain':
                self.transaction.rpc_setter()
                connection_status = self.transaction.connection()
                if connection_status == False:
                    print("Connection Unsuccessful")
                    time.sleep(0.2)
                    print("Read the documentation for help!")
                else:
                    print("Connection Successful")





test = Transaction_Script()
print(test)
            

    