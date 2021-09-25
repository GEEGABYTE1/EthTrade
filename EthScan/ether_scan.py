from web3 import Web3

class Scan:
    infura_url = None 
    

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
    
    def get_latest_block(self):
        latest = self.web3.eth.blockNumber
        latest_block = self.web3.eth.getBlock(latest)
        return latest_block 

    def get_multiple_blocks(self, number):
        blocks = []
        for block in range(0, number):
            current_block = self.web3.eth.getBlock(latest - block)
            bocks.append(current_block)
    
        return blocks 

    def view_transaction_details(self, block_hash, trans_number):
        transaction_details = self.web3.eth.getTransactionByBlock(block_hash, trans_number)
        return transaction_details



ether_base = Scan()

