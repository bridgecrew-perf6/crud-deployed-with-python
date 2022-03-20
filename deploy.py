'''This file is for compiling solidity code'''
import json
import os
from web3 import Web3
from solcx import compile_standard, install_solc
from dotenv import load_dotenv

load_dotenv()

with open('./crud.sol', 'r') as file:
    crud = file.read()
#compiling
print('Installing compiler...')


install_solc('0.8.0')
print('Done!')
compiled_sol = compile_standard({
    'language' : 'Solidity',
    'sources' : {'Storage.sol' : {'content' : crud}},
    'settings' : {
            'outputSelection' :{
                '*' : {
                    '*' : [ 'abi', 'metadate', 'evm.bytecode', 'evm.sourceMap']}
            },

        },
    },
    solc_version = '0.8.0',
)

print('json file created')

with open('compiled_sol.json', 'w') as file:
    json.dump(compiled_sol, file)

#getting the bytecode

bytecode = compiled_sol["contracts"]['Storage.sol']['Storage']['evm']['bytecode']['object']

#getting the abi
abi =compiled_sol['contracts']['Storage.sol']['Storage']['abi']
#print(abi)

#connecting to ganache
w3 = Web3(Web3.HTTPProvider('http://0.0.0.0:8545'))
CHAIN_ID = 1337
MY_ADDRESS = "0xCa7f2A4803e33405Ea85b6Ce356BfCeE46092675"
#using os method
PRIVATE_KEY = os.getenv('PRIVATE_KEY')
print(PRIVATE_KEY)

#creating the contract in python
Storage = w3.eth.contract(abi=abi, bytecode=bytecode)


#get transaction count
nonce = w3.eth.getTransactionCount(MY_ADDRESS)
#Performing transaction
transaction  = Storage.constructor().buildTransaction({
    'chainId': CHAIN_ID,
    "gasPrice": w3.eth.gas_price,
    'from' : MY_ADDRESS,
    'nonce' :nonce
    })


#signing the transaction
signedTransaction = w3.eth.account.sign_transaction(transaction, private_key=PRIVATE_KEY)

#using os method
#PRIVATE_KEY = os.getenv('PRIVATE_KEY')

print("Deploying the contract")
#sending the signed transaction
#and waiting for block confirmation
tnxHash = w3.eth.send_raw_transaction(signedTransaction.rawTransaction)
tnxReceipt = w3.eth.wait_for_transaction(tnxHash)




#Interacting with the contract
#getting the contract
crud =w3.eth.contract(address = tnxReceipt.contractAddress, abi = abi)


#performing transactions
#calling the retrieve function
print(crud.function.retrieve().call())

#calling the Store function

storeFunction = crud.function.retrieve().buildTransaction({
    'chainId' : CHAIN_ID,
    'gasPrice' : w3.eth.gas_price,
    'from' :MY_ADDRESS,
    'nonce' : nonce + 1
    })

# signing the transaction
signedStoredTnx = w3.eth.account.send_raw_transaction(storeFunction, private_key =PRIVATE_KEY)

#sending the transaction
storeTnxHash = w3.eth.send_raw_transaction(signedStoredTnx.rawTransaction)
storeTnsReceipt = w3.eth.wait_for_transaction(storeTnxHash)
