# EthTrade 🌃

Interact with the real and simulated ethereum blockchain right from your terminal! Users can create and analyze contracts, interact with the ethereum chain, and create transactions right from their own memory. 

With the help of the `Web3` library, this program was fully engineered in Python. The solidity files are sample contracts the users can use to analyze and create other contracts on our platform if desired (read "Contracts" documentation under the *Contracts* directory).

# General/Important Information 📚

For the main script, `script.py` to work, all the `.py` files must be outside their directories. All the `.py` files should be under one universal directory. The files were originally organized like this to make the documentation navigation and code-analysis much more easier and efficient.

## Universal Command 🔮

To quit any process or part of the program including the `sign_up` or `log_in` page, the user can type: `/quit`, to quit the page they are currently on.


# Logging In and Account Creation 👔

EthTrade is comprised of a fully secured sha-256 database. Everytime the user signs up on our platform, the account will be secured under a hash code, therefore, reducing any pirating actions. Moreover, all the program's logs are saved under the user's memory including the database itself, keeping the program fully localized to the user. One should also note that the program does not take too much space on their computer's memory.

After signing up on the platform using the syntax: `/sign_up` (which is also outputted on the terminal when ran), the user can log in using the `/log_in` command to be faced with all the program features. If the user fails to log in, the program will prompt the same two commands again, until the user can log in successfully. 

The maximum amount of accounts that can be created are 10,000. Therefore, for people who have multiple users on their device, all their data is saved on a separate array and log on the database keepng it personalized.

# Analyzing The Chain 🔎

One of the biggest features of EthTrade is it's ability to scrape *EtherScan* and output all the desired information to the user with just one command. These commands can be found under the *EthScan*'s documentation under the directory; *EthScan*. With EthScan, users can study the chain in real-time right from their localhost with ease. With the abiltiy to analyze the chain, they can create contracts (read section "Creating Contracts" for more information) and transactions (read section "Creating Transactions" for more information) quickly all from their terminal. 

Syntax: `/analyze_the_chain`

*Note*: This command does not work for simulated blockchains. 

When the user types the command, they will be faced with a new set of commands relative to analyzing the chain. These commands can be found under the documentation under the *`EthScan`'s Directory*. 


# Reading Contracts 👓

From analyzing the chain, users can also read contracts with ease right from their terminal with a few commands. The only prerequisite is that they have contract ready to be analyzed. 

Syntax: `/read_contracts`

When the user types the command, they will be faced with a new set of commands relative to analyzing the contract. These set of commands can be found under the documentation for contracts under the *Contracts* directory.

# Creating Contracts 🛠

Along with reading the contracts, users can create their own contracts right from their terminal. The only prerequisite is that the user must have their contract compiled on Ethereum's *Remix* developed in *Solidity*. If you don't know what that is, you can checkout their links under the *Resources* section of this documentation.

Syntax: `/create_contract` 

When the user has successfully created and developed their contract on our program, they will have the option to *deploy* their contract to either the real chain or their simulated chain, making the contract process simplified than even before. 

When the command is typed, the user will be outputted with a new set of commands relative to creating a contract. The user can learn more about these commands under the documentaion under the *Contracts* directory. 


# Creating Transactions 🔃

Transaction creation can be a hassel sometimes, but now it's not. With the ability to create transactions with just one command, users can create transactions in just seconds. Transaction creation is fully supported for simulated and the real chain, therefore, having it's use in other experimental projects that use Ethereum as a main source.

Syntax: `/create_transaction`

To create a transaction, users will be faced with a set of commands when they type the command above. It is *recommended* that the user reads through the documentation under the *Transactions* directory for safety precautions and more information about how to create a transaction safely from their localhost, and being aware of how the transaction fees work.

# Resources 🔖

These sources can be used for reference to learn more about how the project was made, or if the user needs help with an error they have faced in the program.

 - Infura: https://infura.io
 - EtherScan: https://etherscan.io
 - Web3: https://web3js.readthedocs.io/en/v1.5.2/
 - Remix: https://remix.ethereum.org/#optimize=false&runs=200&evmVersion=null&version=soljson-v0.8.7+commit.e28d00a7.js
 - Ethereum: https://ethereum.org/en/



Made with 🧠 and ❤️ by Jaival Patel

