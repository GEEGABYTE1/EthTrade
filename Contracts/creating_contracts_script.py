import json 
from web3 import Web3
from creating_contracts import cc
import time

class C_Con:
    cc = cc 
    created_ccs = [] 
    
    def __init__(self):
        self.intro() 
        self.creating_contracting()

    def intro(self):
        print("\t"*5)
        print("To view a certain contract, here are the commands: ")
        print('\n')
        time.sleep(0.5)
        print("/connect_chain")
        print("-"*15)
        time.sleep(0.5)
        print("/set_default_account")
        print("-"*15)
        time.sleep(0.5)
        print("/initialize_contract")
        print("-"*15)
        time.sleep(0.5)
        print("/get_default_message")
        print("-"*15)
        time.sleep(0.5)
        print("/set_default_message")
        print("-"*15)
        time.sleep(0.5)
        print("/view_contracts")
        time.sleep(0.5)

    def error(self):
        print("There seems to be an input error")
        time.sleep(0.3)
        print("Read the documentation for help if the error continues")

    def creating_contracting(self):
        print("*Note*: Some commands may not work right away. You may need to run a certain other command for some commands to run")
        time.sleep(0.3)

        while True:
            print("\n")
            prompt = str(input(':'))

            if prompt == '/connect_chain':
                self.cc.infura_url_setter()
                connection_status = self.cc.connection()
                if connection_status == False:
                    print("Connection Unsuccessful")
                    time.sleep(0.2)
                    print("Read the documentation for help!")
                else:
                    print("Connection Successful")

            
            elif prompt == '/set_default_account':
                user_account = str(input("Please insert a user hash: "))
                user_account = user_account.strip(' ')
                try:
                    if len(user_account) != len(self.web3.eth.accounts[0]):
                        raise Exception()
                    self.cc.setting_default_account(user_account)
                except:
                    print("There has been a problem setting this account to default status. Check our hash again, or try reading the documentation")

            elif prompt == '/initialize_contract':
                user_abi = str(input('Please enter the abi of your contract: '))
                user_abi = user_abi.strip(" ")
                try:
                    abi = self.cc.insert_contract_abi(user_abi)
                    user_address = str(input('Please enter the hash address of your contract: '))
                    user_address = user_address.strip(' ')
                    contract_address = self.cc.contract_address(user_address)

                    new_contract = self.cc.initializing_contract(contract_address,abi)
                    time.sleep(0.3)
                    print("Contract: {} has been initialized succesfully. ".format(user_address))
                    self.created_ccs.append(new_contract)
            
                except:
                    print("There seems to be an input error. ")
                    time.sleep(0.2)
                    print("Read the Documentation for more details on how to resolve this problem. ")

            elif prompt == '/get_default_message':
                if len(self.created_ccs) == 0:
                    print("There is no contract to look at")
                else:
                    print('\n')
                    for contract in range(len(self.created_ccs)):
                        print('{}: {}'.format(contract, self.created_ccs[contract]))
                        print('-'*24)
                        time.sleep(0.1)
                    
                    try:
                        user_index = int(input("Please input a corresponding index: "))
                        corresponding_contract = self.created_ccs[user_index]
                        contract_greeting = self.cc.getting_default_greeting(corresponding_contract)
                        time.sleep(0.1)
                        print(contract_greeting)
                    except:
                        print("There seems to be an input error.")
                        time.sleep(0.2)
                        print("Read the Documentation for more details on how to resolve this problem. ")

            elif prompt == '/set_default_message':
                if len(self.created_ccs) == 0:
                    print("There is no contract to modify")
                else:
                    print('\n')
                    for contract in range(len(self.created_ccs)):
                        print('{}: {}'.format(contract, self.created_ccs[contract]))
                        print('-'*24)
                        time.sleep(0.1)
                    
                    try:
                        user_index = int(input("Please input a corresponding index: "))
                        corresponding_contract = self.created_ccs[user_index]
                        setting_default_greeting = self.cc.set_new_greeting(corresponding_contract)
                        time.sleep(0.1)
                    except:
                        print("There seems to be an input error.")
                        time.sleep(0.2)
                        print("Read the Documentation for more details on how to resolve this problem. ")

            elif prompt == '/view_contracts':
                if len(self.created_ccs) == 0:
                    print("You have not created any contracts yet")
                else:
                    for contract in self.created_ccs:
                        print('-'*24)
                        print(contract)
                        time.sleep(0.2)
            
            elif prompt == '/quit':
                break





                    

            
            


            

c_con = C_Con()

print(c_con)
        

            




    