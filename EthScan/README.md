# Ethscan 💎

Look at all the blockchain information live right from your terminal! 


# Accuracy 🎯

Do note that the program does scrape the most latest block in the ethereum chain in real-time. However, there might be a slight milisecond or second delay due to the Ethereum's network time, EtherScan's connection delay, or due to Ethereum's Mining rate. 

Of course, there might be factors from the user's end (read "Connecting to the chain" for more details), but these are also some blockchain limitations to consider. 


# Program 🔮

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

Users can also view transaction details about a specific block or token. This command works intuitively the same as the processes to retrieve block information as it scrapes a certain token under a specified hash code.

Syntax: `/view_transaction_block`

*Note*: The user must have a hash code of a block for this command to work.

One of the important factors for this command to work is the block hash. There are two ways to retrieve the hash.

### Retrieving it from the local variable 

If the user ran `/view_latest_block` or `/view_multiple_blocks`, the user may have been prompted to save certain bits of information about the block if they wanted to (check "Viewing the latest block" for more details). If the user had saved the block's hash by typing `hash`, then the hash would have been saved under their local variable, which could be used to view the block's transaction details in this case. 
    
For the user to see if they do have any hashes saved, they can type in the command `/retrieve_saved_data` to view all the information that has been saved under their local variable.

This method is one of the most efficient methods to obtain hashes.


### Typing the hash code manually

Of course, if the user has a block hash ready to go, the user can deny the prompt of having a block hash saved, and can enter their hash code manually when the program prompts them to.

After inputting the hash, the program will scrape *EtherScan* for it's information. If it has scraped successfully, the user should see information being outputted in the terminal, which at the end, can be saved similar to when retreiving information about blocks (more details about this under "Viewing latest block").

### Inputting Issues

If the user fails to type in a correct input, the progarm will end the process and will prompt the user to type in the command again.

One of the most common mistakes is to type the wrong number when the program is retreiving hash codes from the user's local varible. *Typing a number that is not listed or a letter* will result in the process ending. 

Another error which is very common is to have the wrong hash code. Make sure it's the block hash, which can be found explicitly under the "block's hash" section on EtherScan when on a block. Do note that different platforms may have different ways to output their block hash, but it's typically very evident to find it as they will most probably have it under a section called "Block hash" or "Block's hash".


### Universal Command

Users can quit the process with the `/quit` command and return to the home page. All their information will be saved on their local memory. Do note that the user should not worry about their performance of the memory as it won't take occupy too much on the user's cpu.


# Sources 📝

These sources can be used for reference when there may be a connection error (more details under the "Connecting to the chain" section) or to learn more about how these platforms work.

 - Infura: https://infura.io
 - EtherScan: https://etherscan.io
 - Web3: https://web3js.readthedocs.io/en/v1.5.2/
