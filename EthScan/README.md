# Ethscan 

Look at all the blockchain information live right from your terminal! 


# Accuracy 🎯


# Program 

## Connecting to the chain 

In order to start using the commands, it is necessary for the user to connect to the ethereum chain itself. This allows for full functionality of the program. 


In order to connect to the chain, the user will be prompted to type a command into their terminal. In this case, we will assume the user has not connected their account yet. And hence, we will with the `/connect_chain` command, the user will be prompted to type their infura url. 

*Infura* is a blockchain suite that servers APIs and Developer tools very quickly. If you want to learn more, you could always go on their website:

<a href="https://infura.io">Infura</a>

In the case of the user, all they need to do is make an account and make a project. From there they will need to find their infura end point under the *keys* section. *Note* that the link with `https://` will be the right one to choose to avoid any errors.

After the user has obtained the infura link, they will paste it into their terminal and the program will test it's connection to the chain. 

### Connection Problems

At times there might be connection problems, which will print to the user `Connection unsuccessful`. There are a few reasons why this may happen. This can be due to bugs in the `*Web3* library, a disconnection between the library to the chain, infura disconnection, or a network problem from the user's end. 

In the case that the user's network is working perfectly, they might need a vpn to connect to a region that has a stronger Ethereum Chain connection (one with less network time), or can change ports depending on their knowledge on networks. If that does not work, the user may need to reset their computer, or their wifi.

Sometimes, there might even be a bug in on of the platforms, and in that case, nothing from the user's end can be done. In this case, the user has to keep up with the background platforms, which can be found under the "sources" section of this documentation.

Another very common mistake is the infura url. It should be in `https://` format and must be obtained under the `keys` section of your new project. The format of the link should be follow something similar: `https://mainnet.infura.io/v3/dwadj38nm91010a0102`. 

Of course, if the connection of the user to their network is unstable, this might affect the connection to the chain itself. In this case, the most effective solution is for them to rest their wifi, or move to a region with a stronger connection.

## Viewing the latest block

## Viewing Multiple Blocks 

## Viewing Transaction Details


# Sources