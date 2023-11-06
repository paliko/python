import xmlrpc.client

server = xmlrpc.client.ServerProxy("http://127.0.0.1:8000") #ip serveru pripadne localhostu

print(server.soucet(5,3))