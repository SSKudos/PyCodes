import socket

def portscan(port):     
    try:         
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         
        sock.connect(("127.0.0.1", port))         
        return True     
    except:         
        return False
    
for port in range(15000, 15010):     
    result = portscan(port)
    
    if(result):         
        print("Port {} is open!".format(port))     
    else:         
        print("Port {} is closed!".format(port)) 
