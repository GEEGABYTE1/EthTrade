
from web3 import Web3 
import json 

class Creating_Contract:
    infura_url_contract = None


    def infura_url_setter(self):
        url = str(input("Please enter your RPC Server: "))
        if url == '/help':
            print("Please read the documentation under EthContracts to view how to get an infura url")
        else:
            self.infura_url = url 

    def connection(self):
        self.web3 = Web3(Web3.HTTPProvider(self.infura_url))
        status = self.web3.isConnected()
        if status == True:
            return True 
        else:
            return False