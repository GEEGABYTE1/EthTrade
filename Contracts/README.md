# Contract Information 🏗

In EthScan, users can create, deploy, and read contracts right from their terminal. 

# Reading Contracts 🔎

## Connecting to the chain 

In order to start using the commands, it is necessary for the user to connect to the ethereum chain itself. This allows for full functionality of the program. 

In order to connect to the chain, the user will be prompted to type a command into their terminal. In this case, we will assume the user has not connected their account yet. And hence, we will with the `/connect_chain` command, the user will be prompted to type their RPC server.

To connect to the real chain, the users will have to find their rpc server either from their wallet or on a trading platform, such as *EtherScan*. Note that there are unique ways of finding the rpc server link based on the application or service, therefore, the user must take the initative to learn the location of their service using an external resource. We sadly cannot help each user find their rpc link, due to the number of programs and services that help users connect to the chain. However, in future updates, the documentation may update. 

For simulated blockchains users can type their RPC link hosted by their application, such as ganache. All the functions are fully supported with simulated blockchains as long as the user has a live rpc running. Typically, the RPC link can be found very evidently, but if not, the user may need to read the documentation of their simulated blockchain application. 

Syntax: `/connect_chain`

Do note that for simulated blockchains, users must have their live blockchain running in the background for the program to connect successfully. 

## Setting Default Account

Users can change their default account for easy access to communicate with the chain if they wish to do so. The only parameter the user must have is the user hash of their desired user. They can do this right from our program (read section under "Storing Retrieved Data" under the directory EthScan), or can obtain it manually from an external program. 

### Default Account Problems

The most common problem with setting a new default account is that some hashes may have expired with deleted accounts, or the user has entered an incorrect hash. In either case, the user must make sure that their desired account is up-to-date and is correlated with the user, and not any other information, such as transactions.

### Connection Problems

At times there might be connection problems, which will print to the user `Connection unsuccessful`. There are a few reasons why this may happen. This can be due to bugs in the `*Web3* library, a disconnection between the library to the chain, a simulated blockchain connection problem, or a network problem from the user's end. 


In the case that the user's network is working perfectly, they might need a vpn to connect to a region that has a stronger Ethereum Chain connection (one with less network time), or can change ports depending on their knowledge on networks. If that does not work, the user may need to reset their computer, or their wifi.

Sometimes, there might even be a bug in on of the platforms, and in that case, nothing from the user's end can be done. In this case, the user has to keep up with the background platforms, which can be found under the "sources" section of this documentation.

Another very common mistake with simulated blockchains is that the user does not have their simulation running in the background. This is like the Etherereum blockchain not being active, and hence, the users must have that running for the program to connect.

Of course, if the connection of the user to their network is unstable, this might affect the connection to the chain itself. In this case, the most effective solution is for them to rest their wifi, or move to a region with a stronger connection. 

However, do note that when creating a contract or deploying on simulated blockchains, a network connection problem should not be issue, since the program is connected with the user's local host.


# Creating/Deploying Contracts 🛠

Users can also create and deploy their contracts right from their terminal. The only pre-requisite is that the user must have a contract programmed in solidity, and must have the abi when compiled. 

If the user has failed to do so, then we definitely recommend compiling the contract on Ethereum's Remix IDE (under the sources section) as it allows for easy contract analysis.

Syntax: `/initialize_contract`

For the user to succesfully have their contract deployed, they must have their contract fully functional with no bugs nor errors. The only parameters this process needs is the abi and the contract address. Note that both of these pieces of information can be found when the contract has been compiled on Ethereum's Remix. 

After successfully creating a contract, the user can either modify, or view their contracts. 

To modify, please read the section "Updating Contracts" for more information. However, to view all the contracts, 
type `/view_contracts` to view all the contracts. The user will be informed if they have not created any contracts yet and wish to view some sort of contract.

## Creation Issues

In the case the user is faced with the message `"There seems to be an input error"`, the user may entered either the incorrect abi or address, or have entered an inactive one that may not match. In both cases, the user must make sure that when they compile their contract, they have the right information about their contract. 

If the user is on Remix, they can immediately find the abi by clicking on `"Compiliation Details"`, and going under `"WEB3DEPLOY"`. Under that, the user will copy the *array* only in the variable `var ContractName`. Make sure that at the end of the abi, the user must remove the semi-colon and the closing bracket like this: `);` in order to avoid any errors in the program.

To obtain the contract hash, the user will find it when the contract has been compiled succesfully. They can either find that under their simulated blockchain or on Remix under `"Compilation Details"`. If the user still struggles to find their contract hash, they can deploy their contract successfully on Remix, which will then be faced with the contract address either on their blockchain (simulated or real), or under the `"Deployed Contracts"` section under the `"Deploy and Run Transactions"` tab on Remix. 

# Retrieving Contract Contents 🪛

Users can both update and retrieve the contract message right from their terminal with ease. In terms of retrieving the contract message, the user can easily do so with one command:

Syntax: `/get_default_message`

The user may need a contract hash (read section "Setting Default Account" for more information) in order for the program to reference the content of a desired contract. After successfully inputting a relevant contract hash, the user will have the contract's message in constant time. 

## Obtaining Contract Information Problems 

The user may be faced with an error due to the contract hash not being able to direct the program to the contract object itself. There are two main reasons for that; one, being that the user may have typed the contract has wrong, or has entered another hash of a different type of info, such as a transaction hash. In both cases, the user must be careful and certain that their hash is *relevant* to the contract they want.

The one exception is that the user may have entered a contract that is either old, or has not been deployed to the chain. In that case, the user must contact the contract creator or owner, or has to deploy the contract iself by themselves.

# Updating Contract Contents 🔩

The user can also update the contents of a contract that has already been *deployed* to the chain. The only pre-requisite is that the user must have the contract hash with them (read section "Obtaining Contract Information Problems" for more information).

Syntax: `/set_default_message`

When the user types this command, the user will be prompted to type in a new message. After the user input, the program will set the message as the default greeting and will return the message to the user's locahost to confirm the update. 

## Creation Problems

If the user has an input error, then there are two possible reasons why.

The first one being the incorrect contract hash. In this case, read scetion "Obtaining Contract Information Problems" for more information.

The second reason why is may be due to bugs in the library, or the blockchain technology being to advacned for the library. These cases are very rare, and if so present at any time, the user is recommended to the read the documentation of *Web3* and *Ethereum* (these sources will be under the "Sources" section) for updates.

### Universal Command

Users can quit the process with the `/quit` command and return to the home page. All their information will be saved on their local memory. Do note that the user should not worry about their performance of the memory as it won't take occupy too much on the user's cpu.

Also note that the contract processing time is based on the Ethereum Blockchain or on the user's simulated blockchain application if connected to a simulated rpc. 


# Sources 📝

These sources can be used for reference when there may be a connection error, an input error, or to learn more about how these platforms work.

 - Remix: https://remix.ethereum.org/#optimize=false&runs=200&evmVersion=null&version=soljson-v0.8.7+commit.e28d00a7.js
 - EtherScan: https://etherscan.io
 - Web3: https://web3js.readthedocs.io/en/v1.5.2/
 - Ethereum: https://ethereum.org/en/


