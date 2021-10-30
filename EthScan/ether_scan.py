from web3 import Web3
import hashlib

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
            current_block = self.web3.eth.getBlock('latest')
            blocks.append(current_block)
    
        return blocks 

    def view_transaction_details(self, block_hash, trans_number):
        transaction_details = self.web3.eth.getTransactionByBlock(block_hash, trans_number)
        return transaction_details

    def mining(self, block_num, from_account_hash, transaction_hash, previous_hash, difficulty):
        nonce_limit = self.web3.eth.getTransactionCount(from_account_hash)
        for nonce in range(nonce_limit):
            base_text = str(block_num) + str(transaction_hash) + str(previous_hash) + str(nonce)
            hash_try = haslib.sha256(base_text.encode()).hexdigest()
            string = '0' * difficulty
            if hash_try[:difficulty] == string:
                print("Found hash with nonce: {}".format(nonce))
                return hash_try 

        return None        


ether_base = Scan()