# Ethscan 

Look at all the blockchain information live right from your terminal! 


# Accuracy 🎯


# Program 

## Connecting to the chain 

In order to start using the commands, it is necessary for the user to connect to the ethereum chain itself. This allows for full functionality of the program. 


In order to connect to the chain, the user will be prompted to type a command into their terminal. In this case, we will assume the user has not connected their account yet. And hence, we will with the `/connect_chain` command, the user will be prompted to type their infura url. 

Syntax: `/connect_chain`

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

Users can view all the information about the latest transaction on the Ethereum Chain. The terminal will scrape *EtherScan* for all the information about the latest block. 

Users can view the miner, hash, compleity, nonce, gasprice, and etc, with only one command.

Syntax: `/view_latest_block`

*Note*: This command will only work when the user has succesfully connected to the Ethereum chain.

After running this command, the program will output all the necessary information about the latest block. Depending on the performance of the user's hardware, this process can slow up other processes on the user's platform, and can generally slow the scarpeing process down as well. Note that if there is an input error, for example, not typing a correct data type, the process will end, and the user will be prompted to type the command again.

But in any case, the program does prompt explicitly the type of input it needs.

### Storing Retrieved Data 

After retriving all the data about the latest block, the program will prompt the user to save any peice of data from the latest block. If the user types `y`, they will be prompted to choose a heading that will correspond to the type of informaion they want to save. After successfully typing a desired heading, the information will then be saved in to a local dictionary under the user's account, which can be retrieved with the `/retrieve_saved-data` command. 

Moreover, this dictionary does come in-handy when viewing transaction details as well. For example, one of the benefits of this feature is that users can retrieve hash codes of other accounts very easily, which can make making and studying transactions very easy (you can read the "Viewing Transaction Details" for more information about).

## Viewing Multiple Blocks 

Instead of just viewing one block, users can also look at multiple blocks. This command will work just like when viewing the latest block (read "Viewing the latest block" for more details), but instead, will print multiple blocks from the chain depending on the number of blocks the user wants to see.

Syntax: `/view_multiple_blocks`

The user will be prompted to type in a number of blocks they would like to see. Then the program will scrape information from each block from *latest transaction to oldest transaction* all the way up until the desired number of blocks have been scraped. 

The process of printing and saving information to the user's local variable remains the same as when the user wants to view the latest block. To get more information about the process, you can read the section "Viewing the latest block" on this documentation.

Note that depending on the user's performance and it's background processes, this may affect both the background applications' performance and the program's performance. This is linear to the number of blocks the user wants to see. In other words, the more blocks the user wants to see, the more performance it will take. Some times, connection to the ethereum chain might even be a factor that affects the speed of the scraping. But any case, this process takes a lot of computational power. 

## Viewing Transaction Details



# Sources