import time
from web3 import Web3


class Script:

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
            prompt = str(input(':'))

            if prompt == '/connect_chain':
                pass
            elif prompt == '/view_latest_block':
                pass
            elif prompt == '/view_multiple_blocks':
                pass 
            elif prompt == '/view_transaction_block':
                pass





