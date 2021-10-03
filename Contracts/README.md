# Contract Information

In EthScan, users can create, deploy, and read contracts right from their terminal. 

# Reading Contracts 

## Connecting to the chain 

In order to start using the commands, it is necessary for the user to connect to the ethereum chain itself. This allows for full functionality of the program. 

In order to connect to the chain, the user will be prompted to type a command into their terminal. In this case, we will assume the user has not connected their account yet. And hence, we will with the `/connect_chain` command, the user will be prompted to type their RPC server.

For simulated blockchains users can type their RPC link from ganache. All the functions are fully supported with simulated blockchains as long as the user has a live rpc running. Typically, the RPC link can be found very evidently, but if not, the user may need to read the documentation of their simulated blockchain application. 

Syntax: `/connect_chain`

Do note that for simulated blockchains, users must have their live blockchain running in the background for the program to connect successfully. 

### Connection Problems

At times there might be connection problems, which will print to the user `Connection unsuccessful`. There are a few reasons why this may happen. This can be due to bugs in the `*Web3* library, a disconnection between the library to the chain, a simulated blockchain connection problem, or a network problem from the user's end. 


In the case that the user's network is working perfectly, they might need a vpn to connect to a region that has a stronger Ethereum Chain connection (one with less network time), or can change ports depending on their knowledge on networks. If that does not work, the user may need to reset their computer, or their wifi.

Sometimes, there might even be a bug in on of the platforms, and in that case, nothing from the user's end can be done. In this case, the user has to keep up with the background platforms, which can be found under the "sources" section of this documentation.

Another very common mistake with simulated blockchains is that the user does not have their simulation running in the background. This is like the Etherereum blockchain not being active, and hence, the users must have that running for the program to connect.

Of course, if the connection of the user to their network is unstable, this might affect the connection to the chain itself. In this case, the most effective solution is for them to rest their wifi, or move to a region with a stronger connection. 

However, do note that when creating a contract or deploying on simulated blockchains, a network connection problem should not be issue, since the program is connected with the user's local host.



# Creating Contracts 

* Don't forget to add this into documentation: "You can use any contract as long as you have the abi in string format".*


# Deploying Contracts