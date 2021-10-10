
# Transactions 💳

Users can create transactions right from their terminal either on a simulated chain, or on the real chain. 

*Note*: To create transactions on the real chain, the only prerequisite for the user is to have a fully functioning crypto wallet from any service. However, it is not highly recommended to make transactions on the real chain yet, as this program is still in it's beta version.


# Connecting to the Chain ⛓

In order to start using the commands, it is necessary for the user to connect to the ethereum chain itself. This allows for full functionality of the program. 

In order to connect to the chain, the user will be prompted to type a command into their terminal. In this case, we will assume the user has not connected their account yet. And hence, we will with the `/connect_chain` command, the user will be prompted to type their RPC server.

To connect to the real chain, the users will have to find their rpc server either from their wallet or on a trading platform, such as *EtherScan*. Note that there are unique ways of finding the rpc server link based on the application or service, therefore, the user must take the initative to learn the location of their service using an external resource. We sadly cannot help each user find their rpc link, due to the number of programs and services that help users connect to the chain. However, in future updates, the documentation may update. 

For simulated blockchains users can type their RPC link hosted by their application, such as ganache. All the functions are fully supported with simulated blockchains as long as the user has a live rpc running. Typically, the RPC link can be found very evidently, but if not, the user may need to read the documentation of their simulated blockchain application. 

Syntax: `/connect_chain`

Do note that for simulated blockchains, users must have their live blockchain running in the background for the program to connect successfully. 

# Creating a Transaction 💶

Users can create transactions right from their terminal. This can either be on a simulated blockchain, or on the real chain. 

*If on the real chain, the creator of this program does not take any blame for any accidents regarding any transactions. This may be done at the user's own risk, but is not highly recommended.*

Syntax: `/create_transaction`

When the user types the command above, they will be prompted three times. The first time is to input their account hash. This can be found on the user's wallet, or the listed functions below: 
    - `/view_latest_block`
    - `/view_multiple_blocks`
    - `/view_transaction_block`

For more information about these functions, the user can navigate on `EthScan`'s documentation on the project's Github repository. 

The second input the user will be faced with is the account hash of the account they want to send ether to. Again, similar to how the user can input their account hash, the user can obtain their desired user's hash from either the wallet, or the functions stated above. 

The last input is the private key of the user that is sending the ether. Private keys are confidential and should not be shared with anyone. Note that this program does not save or send any data anywhere but the user's memory, making the program safe and secured. To obtain the private key, the user must navigate to their wallet and go on their *account settings*. From their, they must navigate to where it will most probably state: `Private Key`. For simulated blockchains, the private key can be found easily by just analyzing a block on the chain. 

After the user has inputted all the required connection hashes needed, the user will then be faced to type in an amount (in ether) they would like to send to their desired user. Note that if this is a real connection, make sure that the ether you want to send is reflects the real amount of ether in your wallet. Not having enough money will raise an input error, which will cancel the transaction and may cause problems in the user's wallet. The user should also be sure of the gas price, that can be found online or by inspecting the source code. When making a transaction, the gas price does not pop up, therefore, the user must be aware of the extra expenses when sending ether. 

For the simulated blockchain users, the transaction process works relatively the same. However, there may be no gas price in-effect. Note that just like on the real chain, if the transaction does not reflect the amount of eth that user has initally, this will cause an input error cancelling the transaction as a whole.

After the transaction has been made, the transaction will be automatically be signed using the user's private key, which was inputted. When the transaction has been signed succesfully, the user be faced with a success message, along with the transaction hash, which can be analyzed on  `EthScan` (read EthScan's documentation for more information).

## Input problems 

There are multiple reasons why a user may be faced an input error message, therefore, cancelling the transaction process. The most common one is that the user may have typed their personal account hash and their desired account's account hash incorrect. The only way to fix is this by proof-reading, or going on their wallets, or *EthScan* and copying the account hash. There are possibilities where the user may be mixed up with another type of hash. 

The second common mistake is where the user may not have typed their private key correctly. At times, it may challenging to find their private key, but the easiest method is to find it on their wallet. It is recommended for the user to read their wallet's documentation on where the user's private key is located. For new users, note that private key is formatted differently than a typical hash. 

A hash may start with a `0x...` but a private key will not and may start with a random letter along with some numbers, such as, `d331...`. 

The third mistake users make is the attempt to send more ether than they currently have in their wallet. To fix this issue, it is recommended that the user knows how much ether they have, and must take into consideration the gas-prices. When creating a transacion, the gas-price is not indicated on the program, so it should be assumed that user knows the extra expenses. Therefore, even though the desired amount of ether wanting to be sent falls under the amount in the user's wallet, if the gas price inflates the total price (in ether) for the user at the point where it is greater than the user's total amount in their wallet, the transaction will cancel.


# Viewing Saved Transactions 👀

After a transaction has been successfully made and sent to either the real or the simulated chain, the program will automatically save the transaction for the user to view when needed.

Syntax: `/view_saved_transactions` 

When the user types the command, one will be faced with the transaction hash, and it's block. Note that if there have not been any transactions made, the user will be faced with a message: `"There have not been any transactions made."`. 


# Sources 📝

These sources can be used for reference when there may be a connection error, an input error, or to learn more about how these platforms work.

 - Remix: https://remix.ethereum.org/#optimize=false&runs=200&evmVersion=null&version=soljson-v0.8.7+commit.e28d00a7.js
 - EtherScan: https://etherscan.io
 - Web3: https://web3js.readthedocs.io/en/v1.5.2/
 - Ethereum: https://ethereum.org/en/
