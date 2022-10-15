"""
import json
import requests

rpcPort = 8332
rpcUser = 'username'
rpcPassword = 'password'
rpcIp = '127.0.0.1'
#120.0.0.1:8332
serverURL = 'http://' + str(rpcUser) + ':' + str(rpcPassword)+ '@' + str(rpcIp)+":" + str(rpcPort)

headers = {'content-type: text/plain'}
payload = json.dumps({"method": 'getblockhash', "params": ["0"], "jsonrpc": "2.0"})
payload = json.dumps({"method": 'getblock', "params": ["0000000000005e5fd51f764d230441092f1b69d1a1eeab334c5bb32412e8dc51"]})
response = requests.get(serverURL, headers=headers, data=payload)
print(response)
print(response.json()['result'])
"""
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException 
rpc_connection = AuthServiceProxy("http://%s:%s@192.168.1.14:33333"%("username", "password"))
num_blocks = rpc_connection.getblockcount()

print(num_blocks)

