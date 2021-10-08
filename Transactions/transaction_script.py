import time 
from transaction import transaction



class Transaction_Script:
    created_transactions = {}
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
        time.sleep(0.2)
        print("/view_saved_transactions")
        print('-'*15)
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

            elif prompt == '/create_transaction':
                print("If you do not know your desired account hashes, or your private key, please read the documentation")
                time.sleep(0.2)
                
                try:
                    user_address_hash_1 = str(input("Please type in the your account hash: "))
                    user_address_hash_1 = user_address_hash_1.strip(" ")
                    time.sleep(0.3)
                    user_address_hash_2 = str(input("Please type in the user hash of the desired account (receiever): "))
                    user_address_hash_2 = user_address_hash_2.strip(" ")
                    user_private_key = str(input("Please type in your private key (Note: that this private key is not saved anywhere): "))
                    user_private_key = user_private_key.strip(" ")
                    desired_result = self.transaction.create_transaction(user_address_hash_1, user_address_hash_2, user_private_key)
                    signed_tx = self.transaction.sign_transaction(desired_result, user_private_key)
                    time.sleep(0.3)
                    print("Transaction Complete! {} \n".format(signed_tx))
                    time.sleep(0.2)
                    print("You can view your amount or the user's amount using EthScan.")
                    
                    self.created_transactions[signed_tx] = desired_result
                    time.sleep(0.4)
                    print("Transaction has been added to \"saved transactions\" as well")
                except:
                    print("There seems to be an input error. Please read the documentation for more details.")


            elif prompt == '/view_saved_transactions':
                for tx_hash, obj in self.created_transactions.items():
                    print('-'*24)
                    print("Transaction Hash: {}".format(tx_hash))
                    print("Transaction Object: {}".format(obj))
                    time.sleep(0.2)

        
               
                    

    





test = Transaction_Script()
print(test)
            

    