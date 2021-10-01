import json 
from web3 import Web3
from creating_contracts import cc

class C_Con:
    
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
        print("/create_contract")
        print("-"*15)
        time.sleep(0.5)
        print("/get_default_message")
        print("-"*15)
        time.sleep(0.5)
        print("/set_default_message")
        print("-"*15)
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
        

            




    