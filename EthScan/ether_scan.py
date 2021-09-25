from web3 import Web3

class Scan:
    infura_url = None 
    web3 = Web(Web3.HTTPProvider(infura_url))

    def infura_url_setter(self, url):
        url = str(input("Please enter your infura_url"))
        if url == '/help':
            print("Please read the documentation under EthScan to view how to get an infura url")
        else:
            infura_url = url 

    def connection(self):
        status = web3.isConnected()
        if status == True:
            return True 
        else:
            return 'Connection not successful'

    
    def get_latest_block(self):
        latest = web3.eth.blockNumber
        latest_block = web3.eth.getBlock(latest)
        return latest_block 

    def get_multiple_blocks(self, number):
        blocks = []
        for block in range(0, number):
            current_block = web3.eth.getBlock(latest - block)
            bocks.append(current_block)
    
        return blocks 

    def view_transaction_details(self, block_hash, trans_number):
        transaction_details = web3.eth.getTransactionByBlock(block_hash, trans_number)
        return transaction_details

    








ether_base = Scan()

