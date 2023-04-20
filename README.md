# Webserver
It is solution for Webserver task with python in https://gaia.cs.umass.edu/kurose_ross/programming.php 
to use server.py code;
-->find your ip address 
    -type ipconfig in cmd (for windows) 
    -type ifconfig in cmd (for linux) 
--> write this ip address in here serverSocket.bind(('', serverPort))  (you can run without ip address with your local server)
--> run the code
--> open any browser and type in this format: ip_adress:serverPort/your_html_file_name
    it is a example for that: 192.13.1.134:6789/helloWorld.html
 to use client.py;
 --> run the server.py file
 --> To run the client.py file in cmd, write the required information in the following format to cmd
     -python3 client.py server_host server_port filename
 
