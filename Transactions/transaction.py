from web3 import Web3

class Transaction:

    def rpc_setter(self):
            url = str(input("Please enter your RPC Server: "))
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