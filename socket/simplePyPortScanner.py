import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = 'kaskus.co.id'

def portScan(port):
	s.connect((server,port))
	try:
		s.connect((server,port))
		return True
	except:
		return False

for portNum in range(1,26):
	if portScan(portNum):
		print('Port',protNum,'is open')
	else:
		print('Port',portNum,'is closed')
