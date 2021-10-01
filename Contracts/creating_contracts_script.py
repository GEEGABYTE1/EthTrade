import json 
from web3 import Web3
from creating_contracts import cc
import time

class C_Con:
    cc = cc 
    
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

            
            elif prompt == '/set_default_account':
                user_account = str(input("Please insert a user hash: "))
                try:
                    if len(user_account) != len(self.web3.eth.accounts[0]):
                        raise Exception()
                    self.cc.setting_default_account(user_account)
                except:
                    print("There has been a problem setting this account to default status. Check our hash again, or try reading the documentation")
            

c_con = C_Con()

print(c_con)
        

            




    