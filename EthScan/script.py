import time
from web3 import Web3
from ether_scan import ether_base


class Script:

    def __init__(self):
        self.intro()
        self.scripting()

    def intro(self):
        print("\t"*5)
        print("To view the blockchain, here are the commands: ")
        print('\n')
        time.sleep(0.5)
        print("/connect_chain")
        print("-"*15)
        time.sleep(0.5)
        print("/view_latest_block")
        print("-"*15)
        time.sleep(0.5)
        print("/view_multiple_blocks")
        print("-"*15)
        time.sleep(0.5)
        print("/view_transaction_block")
        print("-"*15)
        time.sleep(0.5)
        print("\t"*5)

    def scripting(self):
        print("*Note*: Some commands may not work right away. You may need to run a certain other command for some commands to run")
        time.sleep(0.3)

        while True:
            print("\n")
            prompt = str(input(':'))

            if prompt == '/connect_chain':
                ether_base.infura_url_setter()
                connection_status = ether_base.connection()
                if connection_status == False:
                    print("Connection insuccessful")
                    time.sleep(0.2)
                    print("Read the documentation for help! ") 
                else:
                    print("Connection Successful")               

            elif prompt == '/view_latest_block':
                pass
            elif prompt == '/view_multiple_blocks':
                pass 
            elif prompt == '/view_transaction_block':
                pass




test = Script()
print(test)