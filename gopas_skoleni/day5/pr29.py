import xmlrpc.server

def soucet(a,b):
    return a+b

server = xmlrpc.server.SimpleXMLRPCServer(("",8000))
server.register_function(soucet)
server.serve_forever()