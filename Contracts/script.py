from reading_contracts import contract 
import time 
from web3 import Web3


class ContractScript:
    
    def __init__(self):
        pass 


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


contract_script = ContractScript()

print(contract_script.intro())