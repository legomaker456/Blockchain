import sys, os
import json

import encryption as RSA
import blockchain

testDir = './tests'

# Initialize the System Wallet and main BlockChain
system_public = RSA.load('./Creator_public.key')
system_private = RSA.load('./Creator_private.key')

systemWallet = blockchain.Wallet('Creator', system_public, system_private)
testChain = blockchain.Chain(systemWallet)


test_public = RSA.load(os.path.join(testDir, 'B_public.key'))
test_private = RSA.load(os.path.join(testDir,'B_private.key'))
testWallet = blockchain.Wallet('Tester', test_public, test_private)

testTransaction = blockchain.Transaction(testWallet, 10, systemWallet)
testTransaction2 = blockchain.Transaction(testWallet, 30, systemWallet)
testTransactionArray = [
    testTransaction,
    testTransaction2
]

output = {
    "transactions" : testTransactionArray
}

print(json.dumps(output, indent=2, cls=blockchain.ChainEncoder))