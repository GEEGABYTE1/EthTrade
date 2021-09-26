import json 
from web3 import Web3 

class Contract:
    infura_url_contract = None


    def infura_url_setter(self):
        url = str(input("Please enter your infura_url: "))
        if url == '/help':
            print("Please read the documentation under EthScan to view how to get an infura url")
        else:
            self.infura_url = url 

    def connection(self):
        self.web3 = Web3(Web3.HTTPProvider(self.infura_url))
        status = self.web3.isConnected()
        if status == True:
            return True 
        else:
            return False

    def checking_contract(self, abi, address):
        self.contract = self.web3.eth.contract(address=address, abi=abi)
        return self.contract 

    def view_tokens(self):
        totalsupply = self.contract.functions.totalSupply().call()
        ethered_supply = self.web3.fromWei(totalsupply, 'ether')
        return ethered_supply 
    
    def get_name(self):
        name = self.contract.functions.name.call()
        return name 

    def get_symbol(self):
        symbol = self.contract.functions.symbol().call()
        return symbol 

    def balance_of_contract_holder(self, token_hash):
        get_balance = self.contract.functions.balanceOf(token_hash)
        get_balance_ether = self.web3.fromWei(get_balance, 'ether')
        return get_balance_ether



    

    


contract = Contract()
