import socket
import sys
import datetime

def getOrHeadResponse(requestPath, isGet):
	validPaths = ["/index.html","/home.html","/files/abc.pdf"] 

	if requestPath in validPaths:
		validResponse = ( "HTTP/1.1 200 OK\n"  
			+"Content-Type: text/html\n" 
			+"Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT\n"
			+"Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)\n"  
			+"Accept-Ranges: bytes\n"
			+"Connection: close\n"
			+"\n"
			)

		if isGet:  #Get Response has Message Body while Head does not.
			validResponse += ("<html><body>Serving the link " 
			+ requestPath 
			+ " on time " 
			+ str(datetime.datetime.now()) 
			+  "</body></html>\n")

		connection.sendall(validResponse)
	else:  
		invalidResponse = ("HTTP/1.1 404 NOT FOUND\n" 
			+"Content-Type: text/html\n"
			+"\n")
		if isGet: #Get Response has Message Body while Head does not.
			invalidResponse += "<html><body>PAGE NOT FOUND</body></html>\n"
		connection.sendall(invalidResponse)

def postResponse(rawData):
	if rawData == "" :
		connection.sendall("HTTP/1.1 422 Unprocessable Entity\n")
		return
	processData = rawData.split("&") #And now we can insert this data into a database
	connection.sendall("HTTP/1.1 403 Created\n") 
	

# Create a TCP/IP socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


serverSocket.bind(('localhost', 8081))

serverSocket.listen(1)

while True:
    # Wait for a connection
    print  'waiting for connection'
    connection, client_address = serverSocket.accept()
    try:
        print 'connection from ' +  str(client_address)

        
        data = connection.recv(10000).split("\n") 
       
        #We only fetch the first 10000 characters
        # so if someone sends a never ending rubbish line,
        # the server would just take the first
        # n (10,000) characters and would not crash
        
        

        httpRequest = data[0].split();

        requestMethod = httpRequest[0]
        requestPath = httpRequest[1]
        requestProtocol = httpRequest[2]

        print data
        print "sending data to the client"

        if requestMethod == "GET":
        	getOrHeadResponse(requestPath,True)
    	elif requestMethod == "HEAD":
    		getOrHeadResponse(requestPath,False)
    	elif requestMethod == "POST":
    		postResponse(data[len(data)-1])
    	

    finally:
        # Clean up the connection
        connection.close()


