from hashmap import HashMap
from etherscan_script  import Script  # Reading EthTrade
from contracts_script import ContractScript # Reading Contracts 
from creating_contracts_script import C_Con # Creating Contracts 
from transaction_script import Transaction_Script # Creating Transaction 
import time 
from os import system



class Introduction:

    account_database = HashMap(10000)
    def __init__(self):
        self.intro()
        self.prompting()

    def intro(self):
        print("Welcome to EthTrade")
        time.sleep(0.2)
        print("Your local platform to connect and interact with the Ethereum chain! ")
        print("\t"*5)
        print("To get started, here are the commands: ")
        print('\n')
        time.sleep(0.5)
        print("/analyze_the_chain")
        print("-"*15)
        time.sleep(0.5)
        print("/read_contracts")
        print("-"*15)
        time.sleep(0.5)
        print("/create_contract")
        print("-"*15)
        time.sleep(0.5)
        print("/create_transaction")
        print("-"*15)
        time.sleep(0.5)
        print('/create_account')
        print("-"*15)
        time.sleep(0.5)
        print('/log_in')
        time.sleep(0.5)
        print("\t"*5)

    def prompting(self):
        while True:
            time.sleep(0.2)
            init_prompt = str(input(':'))

            if init_prompt == '/create_account':
                user = str(input("Please type in your username: "))
                password = str(input("Please type in a password: "))
                node_class = Node()
                self.account_database.setter(user, [password, node_class])
                print("You can now log in with your new account. ")
            
            elif init_prompt == '/log_in':
                while True:
                    user_user = str(input("Please enter your username: "))
                    time.sleep(0.2)
                    user_password = str(input("Please type in you password: "))
                    try:
                        retrieved_value_from_base = self.account_database.retrieve(user_user)
                        if user_password == retrieved_value_from_base[0]:
                            print("You have successfully logged in! ")
                            system('clear')
                            retrieved_value_from_base[1].data()
                            break
                        else:
                            print("Seems like the password does not match")
                    except:
                        print('User: {} has not been found in our database '.format(user_user))
                        time.sleep(0.2)
                        print("You may need to create a new account. ")
                        time.sleep(0.2)
                        print("If you still need help, check out our documentation for more information")

        
                print("You have successfully quit the program")
                break



class Node:

    log = []

    def data(self):
        time.sleep(0.2)
        print("\t"*5)
        print("To get started, here are the commands: ")
        print('\n')
        time.sleep(0.5)
        print("/analyze_the_chain")
        print("-"*15)
        time.sleep(0.5)
        print("/read_contracts")
        print("-"*15)
        time.sleep(0.5)
        print("/create_contract")
        print("-"*15)
        time.sleep(0.5)
        print("/create_transaction")
        print("-"*15)
        time.sleep(0.5)
        print("\t"*5)
        print('\n')
        while True:
            primary_prompt = str(input(':'))

            if primary_prompt == '/analyze_the_chain':
                self.log.append(primary_prompt)
                prompt_script = Script()
                print(prompt_script)
            
            elif primary_prompt == '/read_contracts':
                self.log.append(primary_prompt)
                prompt_read = ContractScript()
                print(prompt_read)
            
            elif primary_prompt == '/create_contract':
                self.log.append(primary_prompt)
                prompt_creation = C_Con()
                print(prompt_creation)
            
            elif primary_prompt == '/create_transaction':
                self.log.append(primary_prompt)
                prompt_transaction = Transaction_Script()
                print(prompt_transaction)
            elif primary_prompt == '/quit':
                break 
            else:
                print("That command is not valid")                


running = Introduction()

print(running)