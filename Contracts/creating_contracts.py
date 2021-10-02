
from web3 import Web3 
import json 

class Creating_Contract:
    infura_url_contract = None


    def infura_url_setter(self):
        url = str(input("Please enter your RPC Server: "))
        # Include Ganache Simulation Incorporation
        if url == '/help':
            print("Please read the documentation under EthContracts to view how to get an infura url")
        else:
            self.rpc_url = url 

    def connection(self):
        self.web3 = Web3(Web3.HTTPProvider(self.rpc_url))
        status = self.web3.isConnected()
        if status == True:
            return True 
        else:
            return False

    def setting_default_account(self, account):
        self.web3.eth.defaultAccount = account 
        print("Setting default account complete")


    def insert_contract_abi(self, abi):
        abi = json.loads(abi)
        return abi 

    def contract_address(self, address):
        address = self.web3.toChecksumAddress(adress)
        return address 

    def initializing_contract(self, address, abi):
        contract = self.web3.eth.contract(address=address, abi=abi)
        return contract 

    def getting_default_greeting(self, contract):
        greeting = contract.functions.greet().call()
        return greeting 

    def set_new_greeting(self, contract):
        user_greeting = input('Please type in your desired contract information: ')
        user_greeting = user_greeting.strip(" ")
        contract_hash = contract.functions.setGreeting(user_greeting).transact()
        
        self.web3.eth.waitForTransactionReceipt(contract_hash)
        formatted_value = contract.functions.greet().call()
        return formatted_value


cc = Creating_Contract()