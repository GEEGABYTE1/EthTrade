from reading_contracts import contract 
import time 
from web3 import Web3


class ContractScript:
    
    def __init__(self):
        self.intro() 
        self.contracting()

    def intro(self):
        print("\t"*5)
        print("To view a certain contract, here are the commands: ")
        print('\n')
        time.sleep(0.5)
        print("/connect_chain")
        print("-"*15)
        time.sleep(0.5)
        print("/verify_contract")
        print("-"*15)
        time.sleep(0.5)
        print("/view_total_supply")
        print("-"*15)
        time.sleep(0.5)
        print("/get_name")
        print("-"*15)
        time.sleep(0.5)
        print("/get_symbol")
        print("-"*15)
        time.sleep(0.5)
        print("/view_holder_balance")
        print("-"*15)
        time.sleep(0.5)
        print("\t"*5)
    
    def contracting(self):
        print("*Note*: Some commands may not work right away. You may need to run a certain other command for some commands to run")
        time.sleep(0.3)

        while True:
            print("\n")
            prompt = str(input(':'))

            if prompt == '/connect_chain':
                contract.infura_url_setter()
                connection_status = contract.connection()
                if connection_status == False:
                    print("Connection unsuccessful")
                    time.sleep(0.2)
                    print("Read the documentation for help! ") 
                else:
                    print("Connection Successful")
            
            elif prompt == '/verify_contract':
                user_address = str(input("Please enter the contract address: "))
                user_address = user_address.strip(" ")
                user_abi = str(input('''Please enter the abi of the contract: '''))
                user_abi = user_abi.strip(" ")
                try:
                    user_contract = contract.checking_contract(user_abi, user_address)
                    if user_contract:
                        print("Contract has been verified: {}".format(user_contract))
                except:
                    print("There seems to be an input error")
                    time.sleep(0.3)
                    print("Read the documentation for help if the error continues")

            


        

    


contract_script = ContractScript()

print(contract_script.intro())