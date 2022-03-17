'''This file is for compiling solidity code'''
#from web3 import web3
from solcx import compile_standard, install_solc

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

print(compiled_sol)
