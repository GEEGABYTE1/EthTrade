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
                try:
                    latest_block = ether_base.get_latest_block()
                    time.sleep(0.2)
                    
                    retrival_options = []
                    for heading, information in latest_block.items():
                        print('{}:'.format(heading))
                        if type(information) != str and type(information) != int:
                            information_formatted = ether_base.web3.toHex(information)
                            information = information_formatted
                        print('{}'.format(information))
                        print(type(information))
                        print('-'*24)  
                        retrival_options.append(heading) 

                    prompt2 = str(input("Would you like to retrieve something? type(y/n): "))
                    if prompt2 == 'y':
                        info = str(input('What would you like to retrieve? '))
                        info = info.lower()
                        info = info.strip(" ")
                        retrieved_data = latest_block.get(info, None)
                        if retrival_data == None:
                            print('Data not found')
                            print('Read documentation for more information')
                        else:
                            self.saved_user_retrieves[info + str(self.counter)] = retrieved_data
                            print("Information succesfully stored ")
        
                except AttributeError:
                    print("Looks like you have connected to the Ethereum Chain yet")
                    time.sleep(0.5)
                    print('Type /connect_chain to do so!')  


            elif prompt == '/view_multiple_blocks':
                num = int(input('Please type in the number of latest blocks you would like to see: '))
                blocks = ether_base.get_multiple_blocks(number)
                
                for block in blocks:
                    pass

            elif prompt == '/view_transaction_block':
                pass

            elif prompt == '/saved_information':
                pass

            self.counter += 1




test = Script()
print(test)