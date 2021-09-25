import time
from web3 import Web3
from ether_scan import ether_base


class Script:

    saved_user_retrieves = {}
    counter = 0

    def __init__(self):
        self.intro()
        self.scripting()
        
    
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
        print('/retrieve_saved_data')
        print("-"*15)
        time.sleep(0.5)
        print("\t"*5)

    def scripting(self):
        print("*Note*: Some commands may not work right away. You may need to run a certain other command for some commands to run")
        time.sleep(0.3)

        while True:
            print("\n")
            prompt = str(input(':'))

            if prompt == '/connect_chain':
                ether_base.infura_url_setter()
                connection_status = ether_base.connection()
                if connection_status == False:
                    print("Connection insuccessful")
                    time.sleep(0.2)
                    print("Read the documentation for help! ") 
                else:
                    print("Connection Successful")               

            elif prompt == '/view_latest_block':
                latest_block = ether_base.get_latest_block()
                self.viewing_block_information(latest_block)


            elif prompt == '/view_multiple_blocks':
                num = int(input('Please type in the number of latest blocks you would like to see: '))
                blocks = ether_base.get_multiple_blocks(number)
                
                for block in blocks:
                    self.viewing_block_information(block)

            elif prompt == '/view_transaction_block':
                try:
                    transaction_number = int(input('Please enter the number of which the transaction occured: '))
                    block_hash = str(input("Do you have a block hash saved already? (type y/n): "))
                    current_hash = None
                    if block_hash == 'y':
                        hashes = []
                        for num in range(0, self.counter):
                            current_hash = self.saved_user_retrieves.get('hash' + str(num), None)
                            if current_hash != None:
                                current_hash = ether_base.web3.toHex(current_hash)
                                hashes.append(current_hash)
                        if len(hashes) == 0:
                            print("You do not have a hash saved")
                        else:
                            for hash_code in range(len(hashes)):
                                print('{}: {}'.format(hash_code, hashes[hash_code]))
                            
                            while True:
                                prompt_index = int(input("Please enter the corresponding number to choose your hash: "))
                                try:
                                    current_hash = hashes[prompt_index]
                                    break
                                except IndexError:
                                    print("That number does not seem valid")
                    else:         
                        hash_prompt = str(input('Please enter your hashcode: '))
                        hash_prompt = hash_prompt.strip(" ")
                        current_hash = hash_prompt 
                    
                    retrieved_information = ether_base.view_transaction_details(current_hash, transaction_number)
                    self.viewing_block_information(retrieved_information)
                except:
                    print("There is an input error that had occured")
                    time.sleep(0.1)
                    print("Please check the documentation for more information")
                

            elif prompt == '/retrieve_saved_data':
                if len(list(self.saved_user_retrieves.values())) == 0:
                    print("You have nothing saved")
                else:
                    for key, value in self.saved_user_retrieves.items():
                        print("{}: {}".format(key, value))

            self.counter += 1

            
    def viewing_block_information(self, block):
        try:
            time.sleep(0.2)
            retrival_options = []
            for heading, information in block.items():
                print('{}:'.format(heading))
                if type(information) != str and type(information) != int and type(information) != list:
                    information_formatted = ether_base.web3.toHex(information)
                    information = information_formatted
                print('{}'.format(information))
                #print(type(information))
                print('-'*24)  
                retrival_options.append(heading) 

            time.sleep(1)
            prompt2 = str(input("Would you like to retrieve something? type(y/n): "))
            if prompt2 == 'y':
                
                time.sleep(0.4)
                print()
                for heading in block.keys():
                    print(heading)
                    print('-'*24)

                info = str(input('What would you like to retrieve? '))
                info = info.lower()
                info = info.strip(" ")
                retrieved_data = block.get(info, None)
                if retrieved_data == None:
                    print('Data not found')
                    print('Read documentation for more information')
                else:
                    self.saved_user_retrieves[info + str(self.counter)] = retrieved_data
                    print("Information succesfully stored ")

        except AttributeError:
            print("Looks like you have connected to the Ethereum Chain yet")
            time.sleep(0.5)
            print('Type /connect_chain to do so!')  





test = Script()
print(test)