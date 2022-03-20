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
MY_ADDRESS = "0x6Feed4d8593291B1d10146A3947213B89d367d5F"
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
signedTransaction = w3.eth.sign_transaction(transaction, PRIVATE_KEY)

#using os method
#PRIVATE_KEY = os.getenv('PRIVATE_KEY')

print("Deploying the contract")
#sending the signed transaction
TnxHash = w3.eth.send_raw_transaction(signedTransaction.rawTransaction)
