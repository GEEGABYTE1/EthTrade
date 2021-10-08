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


    def create_transaction(self, account_1_hash, account_2_hash, private_key):
        transaction_dictionary = {'nonce': None, 'to': None, 'value':None, 'gas':200000, 'gasPrice':self.web3.toWei('50', 'gwei')}
        nonce = self.web3.eth.getTransactionCount(account_1_hash)
        value = int(input("Please enter the amount (*In WEI*) you would like to send: "))
        information = [nonce, account_2_hash, value]
        for header, data in transaction_dictionary.items():
            if len(information) == 0:
                break
            else:
                info = information.pop(0)
                transaction_dictionary[header] = info

        return transaction_dictionary

    def sign_transaction(self, transaction, private_key):
        signed_trans = self.web3.eth.account.signTransaction(transaction, private_key)
        signed_hash = self.web3.eth.sendRawTransaction(signed_trans.rawTransaction)
        signed_hash = self.web3.toHex(signed_hash)
        return signed_hash


transaction = Transaction()
        

            

        
        